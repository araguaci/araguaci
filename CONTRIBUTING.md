# Como contribuir

Este repositório é o README do perfil [github.com/araguaci](https://github.com/araguaci). O miolo é a lista de projetos públicos.

## O que cabe aqui

- Link quebrado de site, badge ou cartão do perfil.
- Projeto público seu que sumiu do catálogo, desde que esteja na lista [My stack](https://github.com/stars/araguaci/lists/my-stack) e não seja privado nem fork.
- Erro de texto no `README.md`, no código de conduta ou neste guia.

## O que não entra

- Repositório privado. A lista pode contê-lo; o perfil público não.
- Fork de outro autor, salvo se eu mesmo o deixar fixado no destaque.
- Anotação solta na raiz. Material de referência vai para [`notes/`](notes/).

## Atualizar o catálogo

Com o [GitHub CLI](https://cli.github.com/) autenticado, na raiz:

```bash
python scripts/sync_public_stack.py
```

O script reescreve [`docs/projetos.md`](docs/projetos.md) e o bloco entre `<!-- stack:start -->` e `<!-- stack:end -->` no README. Não edite esse bloco à mão.

## Cartões do perfil

| Cartão | Endereço |
| --- | --- |
| Pins e estatísticas | `github-readme-stats.vercel.app` (HTTPS) |
| Sequência de contribuições | `streak-stats.demolab.com` |
| Texto animado | `readme-typing-svg.demolab.com` |
| Visitas | `komarev.com/ghpvc` |

O endereço antigo `github-readme-streak-stats.herokuapp.com` não é mais a instância de referência. O cartão de resumo em HTTP (`github-profile-summary-cards`) saiu do perfil para reduzir dependência duplicada.

## Fluxo de RSS

O workflow `.github/workflows/main.yml` só roda quando alguém dispara manualmente e informa a URL do feed. A action `araguaci/rss-feed-to-markdown` declara `node16`, runtime que o GitHub aposentou. O substituto é `scripts/rss-to-markdown.mjs`, em Node atual.

O endereço que estava fixo no workflow era o canal de exemplo da action (Game Dev Happy Hour), não um canal deste perfil. Ele gerava arquivos e os descartava, porque o job não fazia commit. Agora o feed entra como parâmetro do disparo manual. Os Markdown saem em `_posts/events/` no runner e continuam sem commit automático.
