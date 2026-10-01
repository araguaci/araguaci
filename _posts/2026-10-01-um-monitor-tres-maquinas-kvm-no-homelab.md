---
layout: post
title: "Um monitor, três máquinas: como alternar entre Raspberry Pi, notebook e miniPC no homelab"
date: 2026-10-01 20:00:00 -0300
description: "Passo a passo para operar Raspberry Pi, notebook e miniPC com um só monitor de duas entradas HDMI e um só teclado/mouse: KVM por software (Deskflow / Input Leap), acesso remoto (SSH, NoMachine, xrdp) e quando vale comprar um KVM switch físico."
categories: [homelab, dev-env]
tags: [homelab, raspberry-pi, minipc, kvm, deskflow, input-leap, nomachine, ssh, linux]
---

# Um monitor, três máquinas

> **Diário dev, 01/10/2026.** O miniPC chegou e o lab passou a ter três máquinas: um **Raspberry Pi**, um **notebook** e um **miniPC**. O problema é que só existe **um monitor, com duas entradas HDMI**. Este post registra a solução que montei, do zero ao fluxo diário, para quem estiver no mesmo cenário.

## TL;DR

| Camada | Solução | Custo |
|---|---|---|
| Vídeo | Notebook usa a própria tela. miniPC no **HDMI 1** e Pi no **HDMI 2** | R$ 0 |
| Teclado/mouse | **Deskflow** (ou Input Leap): um teclado e um mouse para as três máquinas, movendo o cursor entre as telas | R$ 0 |
| Plano B | **SSH** para o dia a dia e **NoMachine/xrdp** quando precisar de interface gráfica | R$ 0 |
| Upgrade opcional | **KVM switch HDMI + USB** com emulação de EDID, para BIOS, boot e rede fora do ar | R$ 300–1.000+ |

A sacada é simples: **o notebook já tem tela**. Então o "problema de três máquinas" vira um problema de **duas máquinas no monitor**, e o monitor já resolve isso sozinho com o botão de *input*. O que falta é não precisar de três teclados e três mouses.

---

## Sumário

1. [Arquitetura do setup](#1-arquitetura-do-setup)
2. [Preparação: rede, hostnames e IPs fixos](#2-preparação-rede-hostnames-e-ips-fixos)
3. [Ligação física](#3-ligação-física)
4. [KVM por software com Deskflow](#4-kvm-por-software-com-deskflow)
5. [Alternativa: Input Leap](#5-alternativa-input-leap)
6. [Acesso remoto: SSH, NoMachine e xrdp](#6-acesso-remoto-ssh-nomachine-e-xrdp)
7. [Quando comprar um KVM switch físico](#7-quando-comprar-um-kvm-switch-físico)
8. [Bônus: PiKVM](#8-bônus-pikvm)
9. [Troubleshooting](#9-troubleshooting)
10. [Fluxo diário final](#10-fluxo-diário-final)

---

## 1. Arquitetura do setup

```
                 ┌──────────────────────────┐
                 │        MONITOR           │
                 │  HDMI 1        HDMI 2    │
                 └────┬──────────────┬──────┘
                      │              │
               ┌──────┴─────┐  ┌─────┴──────┐
               │   miniPC   │  │ Raspberry  │
               │  (client)  │  │ Pi (client)│
               └──────┬─────┘  └─────┬──────┘
                      │   rede LAN   │
                      └──────┬───────┘
                             │
                    ┌────────┴────────┐
                    │    NOTEBOOK     │  ← teclado + mouse físicos
                    │ (server Deskflow│     tela própria
                    │  + tela própria)│
                    └─────────────────┘
```

- **Notebook = servidor** do Deskflow. É nele que ficam o teclado e o mouse físicos.
- **miniPC e Pi = clientes**. Eles recebem teclado e mouse pela rede.
- **Vídeo**: o monitor alterna entre miniPC e Pi pelo botão de *input*, e o notebook fica sempre na própria tela.

Na prática você trabalha com o monitor ao lado do notebook. Para usar o miniPC, basta "empurrar" o mouse para a borda da tela do notebook e o cursor aparece no monitor.

---

## 2. Preparação: rede, hostnames e IPs fixos

Todo o resto depende de as máquinas se acharem na rede. Vale gastar 10 minutos aqui.

### 2.1 Dê nomes claros às máquinas

No Linux (miniPC e Pi):

```bash
sudo hostnamectl set-hostname minipc     # no miniPC
sudo hostnamectl set-hostname rpi        # no Raspberry
```

No Raspberry Pi também dá para fazer isso via `sudo raspi-config` → *System Options* → *Hostname*.

### 2.2 Ative o mDNS para acessar por `nome.local`

```bash
sudo apt install -y avahi-daemon
sudo systemctl enable --now avahi-daemon
```

A partir daí, `ssh usuario@minipc.local` e `ssh usuario@rpi.local` funcionam sem você decorar IPs. O Raspberry Pi OS já vem com o avahi.

### 2.3 Fixe os IPs no roteador

No painel do roteador, procure **DHCP Reservation** / **Reserva de IP** / **IP estático por MAC** e reserve um endereço para cada máquina. Exemplo:

| Máquina | IP |
|---|---|
| notebook | 192.168.0.10 |
| minipc | 192.168.0.20 |
| rpi | 192.168.0.30 |

Para descobrir o MAC e o IP atual de cada máquina:

```bash
ip -br addr        # IPs
ip -br link        # MACs
```

> 💡 Se puder, ligue miniPC e Pi **por cabo**. O Deskflow funciona via Wi-Fi, mas a latência do mouse fica bem melhor no cabo.

---

## 3. Ligação física

1. **miniPC** → cabo HDMI → **HDMI 1** do monitor.
2. **Raspberry Pi** → cabo micro-HDMI/HDMI (conforme o modelo) → **HDMI 2** do monitor.
3. **Notebook** → usa a própria tela. Teclado e mouse externos (se você usa) ficam conectados **nele**.
4. Os três na mesma rede (cabo ou Wi-Fi).

> ⚠️ No **Raspberry Pi 4/5**, use a porta **HDMI0** (a mais próxima da entrada de energia). Algumas configurações só mandam imagem por ela no boot.

Teste: ligue tudo e alterne o *input* do monitor. As duas imagens precisam aparecer. Por enquanto, um teclado USB temporário no miniPC e no Pi ajuda nas configurações iniciais.

---

## 4. KVM por software com Deskflow

O [**Deskflow**](https://github.com/deskflow/deskflow) é o projeto open source que virou o *upstream* oficial do Synergy. Ele compartilha **teclado, mouse e área de transferência** entre computadores pela rede, em Linux, Windows e macOS.

### 4.1 Instalação

**Linux (miniPC, notebook Linux), via Flatpak:**

```bash
sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install -y flathub org.deskflow.deskflow
flatpak run org.deskflow.deskflow
```

**Windows (se o notebook ou o miniPC rodar Windows):**

```powershell
winget install Deskflow.Deskflow
```

Ou baixe o instalador em [github.com/deskflow/deskflow/releases](https://github.com/deskflow/deskflow/releases).

**macOS:**

```bash
brew install --cask deskflow
```

**Raspberry Pi (ARM64):** primeiro confira se existe pacote para a sua versão do sistema:

```bash
apt search deskflow
```

Se não tiver, use o Flatpak (o Flathub publica builds `aarch64`) ou um `.deb` ARM64 da página de releases, se houver. Se nada disso funcionar no Pi, pule para o [Input Leap](#5-alternativa-input-leap).

> 📌 Os nomes de pacote e os canais de distribuição mudam com frequência. Antes de instalar, confira a página de releases do projeto.

### 4.2 ⚠️ Raspberry Pi OS e Wayland

O Raspberry Pi OS recente usa **Wayland** (labwc) por padrão. KVMs por software dependem de injetar eventos de entrada, e o suporte a isso no Wayland ainda varia por compositor. Se o cliente conectar mas o mouse não se mexer no Pi, troque para **X11**:

```bash
sudo raspi-config
# Advanced Options → Wayland → X11 → Finish → reboot
```

O mesmo vale para o miniPC, se ele rodar uma distro com Wayland e o compositor não suportar as APIs necessárias. Na tela de login do GNOME, por exemplo, você pode escolher a sessão **"GNOME on Xorg"** pelo ícone de engrenagem.

### 4.3 Configurar o servidor (notebook)

1. Abra o Deskflow no **notebook**.
2. Selecione **"Use this computer's keyboard and mouse" (Server)**.
3. Clique em **Configure Server** (ou *Configure screens*).
4. Na grade, arraste ícones de monitor para montar o layout físico real. Exemplo, com o monitor à direita do notebook:

```
┌────────────┐ ┌────────────┐
│  notebook  │ │   minipc   │
└────────────┘ └────────────┘
               ┌────────────┐
               │    rpi     │   ← "abaixo" do minipc
               └────────────┘
```

5. **Os nomes de cada tela precisam ser exatamente o *screen name* do cliente** (por padrão, o hostname: `minipc`, `rpi`).
6. Salve e clique em **Start**.

> 💡 **Por que colocar o Pi "abaixo" do miniPC?** Os dois disputam o mesmo monitor. Na prática você só olha para um de cada vez, então tanto faz onde o "outro" fica no layout. Colocar um abaixo do outro evita que o cursor vá parar numa tela que não está visível só porque você passou da borda sem querer.

### 4.4 Configurar os clientes (miniPC e Pi)

Em cada cliente:

1. Abra o Deskflow.
2. Selecione **"Use another computer's keyboard and mouse" (Client)**.
3. Em **Server IP**, coloque `192.168.0.10` (o IP fixo do notebook) ou `notebook.local`.
4. Confira o **Screen name**. Ele precisa bater com o nome configurado no servidor.
5. Clique em **Start**.

Na primeira conexão, o Deskflow mostra o **fingerprint TLS** do servidor. Compare com o que aparece no notebook e aceite. Essa é a proteção para que ninguém da rede capture o que você digita.

### 4.5 Firewall

O Deskflow usa a porta **TCP 24800**. Ela precisa estar aberta **no servidor (notebook)**:

```bash
# Linux com ufw
sudo ufw allow from 192.168.0.0/24 to any port 24800 proto tcp
```

No Windows, aceite o aviso do Firewall do Windows na primeira execução, liberando **apenas redes privadas**.

### 4.6 Iniciar automaticamente

- **No notebook (servidor)**, ative *Start on login* / *Iniciar com o sistema* nas configurações do Deskflow.
- **Nos clientes Linux**, faça o mesmo. Se ele não aparecer na tela de login, configure o *autologin* da sessão gráfica (no Pi: `raspi-config` → *System Options* → *Boot / Auto Login* → *Desktop Autologin*).

Faça o teste: reinicie o miniPC e verifique se, ao chegar na área de trabalho, o mouse do notebook já o controla.

### 4.7 Atalhos úteis

Na configuração do servidor (*Hotkeys*), crie atalhos para pular direto de tela, sem arrastar o mouse:

| Atalho | Ação |
|---|---|
| `Ctrl+Alt+1` | switchToScreen(notebook) |
| `Ctrl+Alt+2` | switchToScreen(minipc) |
| `Ctrl+Alt+3` | switchToScreen(rpi) |

Junto com o botão de *input* do monitor, isso dá uma troca de contexto em dois gestos.

---

## 5. Alternativa: Input Leap

O [**Input Leap**](https://github.com/input-leap/input-leap) é o fork comunitário do Barrier, que por sua vez veio do Synergy. A configuração é praticamente idêntica (servidor, clientes, layout e porta 24800). Ele é uma boa saída quando o Deskflow não tem build para alguma das máquinas, principalmente o Pi.

```bash
# Debian/Ubuntu/Raspberry Pi OS, se o pacote existir na sua versão
sudo apt install input-leap

# ou via Flatpak
flatpak install flathub io.github.input_leap.input-leap
```

> ⚠️ **Use o mesmo software em todas as máquinas.** Deskflow e Input Leap têm origem comum, mas não garanto compatibilidade entre versões e protocolos de projetos diferentes. Escolha um e mantenha nos três.

---

## 6. Acesso remoto: SSH, NoMachine e xrdp

Num lab, Pi e miniPC passam a maior parte do tempo rodando serviços: Home Assistant, Docker, bancos, n8n. Para a maior parte do trabalho você nem precisa da tela deles.

### 6.1 SSH (o padrão de tudo)

Nos clientes:

```bash
sudo apt install -y openssh-server
sudo systemctl enable --now ssh
```

No notebook, gere uma chave e copie para as máquinas:

```bash
ssh-keygen -t ed25519 -C "notebook-lab"
ssh-copy-id usuario@minipc.local
ssh-copy-id usuario@rpi.local
```

Crie atalhos em `~/.ssh/config`:

```
Host minipc
    HostName minipc.local
    User usuario

Host rpi
    HostName rpi.local
    User usuario
```

Agora basta digitar `ssh minipc` ou `ssh rpi`. Bônus: o **VS Code Remote-SSH** abre pastas do miniPC direto no editor do notebook.

> 🔒 Depois de confirmar que o login por chave funciona, desative o login por senha em `/etc/ssh/sshd_config` (`PasswordAuthentication no`) e rode `sudo systemctl restart ssh`.

### 6.2 NoMachine (área de trabalho remota fluida)

O [NoMachine](https://www.nomachine.com/) tem builds para x86_64 e ARM (Raspberry Pi), com bom desempenho até para vídeo.

1. Baixe o pacote `.deb` adequado em nomachine.com/download (**x86_64** para o miniPC, **ARMv8/ARM64** para o Pi).
2. Instale com `sudo dpkg -i nomachine_*.deb`.
3. Instale o cliente no notebook e as máquinas aparecem automaticamente na rede local.

### 6.3 xrdp (RDP nativo)

Se o notebook roda Windows, o **Conexão de Área de Trabalho Remota** já vem instalado. Nos clientes Linux:

```bash
sudo apt install -y xrdp
sudo systemctl enable --now xrdp
```

Conecte em `minipc.local` pela porta 3389.

> ⚠️ O xrdp abre uma **sessão nova**, separada da que está na tela física. Se você estiver logado no monitor com o mesmo usuário, pode dar conflito. Nesse caso, faça logout local ou use NoMachine, que espelha a sessão existente.

### 6.4 Modo headless no Raspberry

Se o Pi virar servidor puro, você pode até liberar o HDMI 2 do monitor para outra coisa:

```bash
sudo raspi-config
# System Options → Boot / Auto Login → Console Autologin
```

---

## 7. Quando comprar um KVM switch físico

O KVM por software tem um limite claro: **ele só funciona com o sistema operacional rodando e a rede de pé.** Ele não serve para:

- entrar na **BIOS/UEFI** do miniPC;
- escolher kernel no **GRUB**;
- consertar uma máquina **sem rede** ou com a interface gráfica quebrada;
- instalar um sistema do zero.

Se isso acontece com frequência, um **KVM switch HDMI + USB** resolve. Ele troca vídeo, teclado e mouse juntos, por botão ou por atalho.

### Checklist de compra

| Item | Por que importa |
|---|---|
| **3 ou 4 portas** | Se quiser incluir o notebook via HDMI, ou deixar uma porta sobrando para o próximo equipamento |
| **Resolução / Hz do seu monitor** | Ex.: 4K@60Hz exige switch HDMI 2.0. Os mais baratos ficam em 4K@30Hz |
| **Emulação de EDID** | **O mais importante.** Sem ela, o SO "perde" o monitor a cada troca e reorganiza janelas e resolução |
| **USB 2.0/3.0 para teclado e mouse** | Alguns têm portas "emuladas" (que suportam hotkey) e portas "passthrough" (para pendrive). Veja qual é qual |
| **Troca por hotkey** | `Scroll Lock` + `Scroll Lock` + número, por exemplo. Evita ter que alcançar o botão |
| **Cabos inclusos** | Cada máquina precisa de **1 HDMI + 1 USB** até o switch. Com 3 máquinas, são 6 cabos |
| **Fonte de alimentação própria** | Switches alimentados só pelo USB costumam falhar com 4K e periféricos mais exigentes |

**Marcas com boa reputação:** TESmart, UGREEN, Aten e Level1Techs (topo de linha). Os genéricos sem marca costumam economizar justamente no EDID e no hotkey.

### Topologia com KVM físico

```
miniPC ──HDMI+USB──┐
rpi    ──HDMI+USB──┼──► KVM ──HDMI──► Monitor
notebook─HDMI+USB──┘     │
                         └──USB──► Teclado + Mouse
```

Nesse caso, o monitor fica numa entrada só e a segunda entrada HDMI sobra para outro uso.

---

## 8. Bônus: PiKVM

O [**PiKVM**](https://pikvm.org/) transforma um Raspberry Pi num **KVM over IP**: você vê a tela do miniPC (inclusive a BIOS) **pelo navegador** e controla teclado e mouse remotamente. Ele pode até montar ISOs para reinstalar o sistema.

- **Prós:** gerenciar o miniPC como um servidor de datacenter, de qualquer lugar da rede.
- **Contras:** exige hardware extra (placa de captura HDMI-CSI ou USB, além de um cabo USB-C OTG) e **o Pi fica dedicado** a essa função.

Isso faz sentido quando o miniPC virar servidor crítico e ficar longe da bancada.

---

## 9. Troubleshooting

| Sintoma | Causa provável | Correção |
|---|---|---|
| Cliente não conecta | Firewall no servidor / IP errado | Liberar TCP 24800 no notebook; testar com `nc -zv 192.168.0.10 24800` no cliente |
| Conecta, mas o mouse não aparece no cliente | Nome da tela diferente no layout | O *screen name* do cliente tem que ser idêntico ao do servidor |
| Conecta, mas nada se mexe no Pi | Sessão Wayland | Trocar para X11 (`raspi-config` → Advanced → Wayland → X11) |
| Cursor "some" | Ele foi para a tela que não está selecionada no monitor | Use os hotkeys `switchToScreen` ou reorganize o layout |
| Teclado com acentos errados no cliente | Layout diferente entre máquinas | Igualar o layout (ex.: ABNT2 `br`) em todas: `sudo dpkg-reconfigure keyboard-configuration` |
| Mouse com atraso | Wi-Fi congestionado | Cabo nos clientes ou banda de 5 GHz |
| Monitor demora a trocar de input | Detecção automática de sinal | Desative *Auto Input* no OSD do monitor e troque manualmente |
| Pi sem imagem no boot | Porta HDMI errada | No Pi 4/5, usar a **HDMI0** |
| Copiar e colar não funciona | Clipboard desativado / Wayland | Verifique a opção de clipboard sharing; em Wayland é comum falhar |

---

## 10. Fluxo diário final

1. **Ligo o notebook.** O Deskflow server sobe sozinho.
2. **miniPC e Pi** sobem com autologin e o cliente Deskflow se conecta.
3. **Trabalho no notebook** normalmente, na tela dele.
4. **Preciso do miniPC?** `Ctrl+Alt+2` (ou empurro o mouse para a direita) e confirmo que o monitor está no **HDMI 1**.
5. **Preciso do Pi?** `Ctrl+Alt+3` e troco o monitor para **HDMI 2**.
6. **Tarefas de terminal** vão por `ssh minipc` / `ssh rpi`, sem sair do notebook.
7. **Deu pau na BIOS/rede?** Teclado USB direto na máquina. Se isso começar a acontecer com frequência, é a hora do KVM físico.

Custo total da solução: **zero**. O único investimento futuro, se fizer falta, é um KVM switch com EDID.

---

### Referências

- [Deskflow (GitHub)](https://github.com/deskflow/deskflow)
- [Input Leap (GitHub)](https://github.com/input-leap/input-leap)
- [NoMachine](https://www.nomachine.com/)
- [xrdp](https://www.xrdp.org/)
- [PiKVM](https://pikvm.org/)
- [Raspberry Pi: documentação do raspi-config](https://www.raspberrypi.com/documentation/computers/configuration.html)
