← Back

CLI tools you can't live without 🔧
===================================

Thursday 19 Jan 2023

Published by Alicia's Notes 🚀, View [original](https://notes.aliciasykes.com/41983/cli-tools-you-can-t-live-without "Read: CLI tools you can't live without 🔧")

As developers, we spend a lot of our time in the terminal. There's a lot of helpful CLI tools, which can make your life in the command line easier, faster and generally more fun.

This post outlines my top 50 must-have CLI tools, which I've come to rely on. If there's anything I'm missing - do let me know in the comments :)

At the end of the article, I've included some scripts to help you automate the installation and updating of these tools on various systems/ distros.

Utils
-----

### [thefuck](https://github.com/nvbn/thefuck) - Auto-correct miss-typed commands

> `thefuck` is one of those utilities you won't be able to live without once you've tried it. Whenever you mis-type a command and get an error, just run `fuck` and it'll auto-correct it. Use up/down to choose a correction, or just run `fuck --yeah` to just execute the most likely immediately.

![the-fuck-example-usage](https://i.ibb.co/J55hWKX/thefuck.gif)

[![View thefuck on GitHub](https://img.shields.io/github/stars/nvbn/thefuck?color=232323&label=thefuck&logo=github&labelColor=232323)](https://github.com/nvbn/thefuck)[![Author nvbn](https://img.shields.io/badge/nvbn-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/nvbn) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install thefuck
# Arch Linux
sudo pacman -S thefuck
# FreeBSD
pkg install thefuck
``` 

* * *

### [zoxide](https://github.com/ajeetdsouza/zoxide) - Easy navigation _(better cd)_

> `z` lets you jump to any directory without needing to remember or specify its full path. It remembers which directories you've visited, so you can jump around quickly - you don't even need to type the full folder name. It also has an interactive selection option, using `fzf` so you can live-filter directory results

![zoxide-example-usage](https://i.ibb.co/6Z960jq/zoxide.gif)

[![View zoxide on GitHub](https://img.shields.io/github/stars/ajeetdsouza/zoxide?color=232323&label=zoxide&logo=github&labelColor=232323)](https://github.com/ajeetdsouza/zoxide)[![Author ajeetdsouza](https://img.shields.io/badge/ajeetdsouza-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/ajeetdsouza) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install zoxide
# Arch Linux
sudo pacman -S zoxide
# Debian / Ubuntu
sudo apt install zoxide
# FreeBSD
pkg install zoxide
# Other (via Rust Creates)
cargo install zoxide --locked 
``` 

* * *

### [tldr](https://github.com/tldr-pages/tldr) - Community-maintained docs _(better `man`)_

> `tldr` is a huge collection of community-maintained man pages. Unlike traditional man pages, they're summarized, contain useful usage examples and nicely colourized for easy reading

![tldr-example-usage](https://i.ibb.co/jTW9knx/tlfr.gif)

[![View tldr on GitHub](https://img.shields.io/github/stars/tldr-pages/tldr?color=232323&label=tldr&logo=github&labelColor=232323)](https://github.com/tldr-pages/tldr)[![Author tldr-pages](https://img.shields.io/badge/tldr-pages-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/tldr-pages)

```Install bash
# MacOS (via Homebrew)
brew install tldr
# Other (via NPM)
npm install -g tldr
``` 

* * *

### [scc](https://github.com/boyter/scc) - Count lines of code _(better `cloc`)_

> `scc` gives you a breakdown of number of lines of code written in each language for a specific directory. It also shows some fun stats, like estimated cost to develop and complexity info. It's incredibly fast, very accurate and has support for a wide range of languages

![scc-example-usage](https://i.ibb.co/NygHWXt/scc.png)

[![View scc on GitHub](https://img.shields.io/github/stars/boyter/scc?color=232323&label=scc&logo=github&labelColor=232323)](https://github.com/boyter/scc)[![Author boyter](https://img.shields.io/badge/boyter-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/boyter) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install scc
# Other (via go)
go install github.com/boyter/scc/v3@latest 
``` 

* * *

### [exa](https://github.com/ogham/exa) - Listing Files _(better `ls`)_

> `exa` is a modern Rust-based replacement for the `ls` command, for listing files. It can display file-type icons, colors, file/folder info and has several output formats - tree, grid or list

![exa-example-usage](https://i.ibb.co/cTs0wQ5/exa.png)

[![View exa on GitHub](https://img.shields.io/github/stars/ogham/exa?color=232323&label=exa&logo=github&labelColor=232323)](https://github.com/ogham/exa)[![Author ogham](https://img.shields.io/badge/ogham-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/ogham) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install exa
# Arch Linux
sudo pacman -S exa
# Debian / Ubuntu
sudo apt install exa 
``` 

* * *

### [duf](https://github.com/muesli/duf) - Disk Usage _(better `df`)_

> `duf` is great for showing info about mounted disks and checking free space. It produces a clear and colorful output, and includes options for sorting and customizing results.

![duf-example-usage](https://i.ibb.co/sP59DKd/duf.png)

[![View duf on GitHub](https://img.shields.io/github/stars/muesli/duf?color=232323&label=duf&logo=github&labelColor=232323)](https://github.com/muesli/duf)[![Author muesli](https://img.shields.io/badge/muesli-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/muesli) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install duf
# Arch Linux
sudo pacman -S duf
# Debian / Ubuntu
sudo apt install duf
# FreeBSD
pkg install duf
``` 

* * *

### [aria2](https://github.com/aria2/aria2) - Download Utility _(better `wget`)_

> `aria2` is a lightweight, multi-protocol, resuming download utility for HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink, with support for controlling via an RPC interface. It's incredibly [feature rich](https://aria2.github.io/manual/en/html/README.html), and has tons of [options](https://aria2.github.io/manual/en/html/aria2c.html). There's also [ziahamza/webui-aria2](https://github.com/ziahamza/webui-aria2) - a nice web interface companion.

![aria2c-example-usage](https://i.ibb.co/pJkkX6x/aria2c.png)

[![View aria2 on GitHub](https://img.shields.io/github/stars/aria2/aria2?color=232323&label=aria2&logo=github&labelColor=232323)](https://github.com/aria2/aria2)[![Author aria2](https://img.shields.io/badge/aria2-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/aria2) ![Written in C++](https://img.shields.io/static/v1?label=&message=C++&color=00599C&logo=cplusplus&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install aria2
# Arch Linux
sudo pacman -S aria2
# Debian / Ubuntu
sudo apt install aria2 
``` 

* * *

### [bat](https://github.com/sharkdp/bat) - Reading Files _(better `cat`)_

> `bat` is a clone of `cat` with syntax highlighting and git integration. Written in Rust, it's very performant, and has several options for customizing output and theming. There's support for automatic piping and file concatenation

![bat-example-usage](https://i.ibb.co/VND3Y9s/bat.png)

[![View bat on GitHub](https://img.shields.io/github/stars/sharkdp/bat?color=232323&label=bat&logo=github&labelColor=232323)](https://github.com/sharkdp/bat)[![Author sharkdp](https://img.shields.io/badge/sharkdp-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/sharkdp) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

```Install bash
# MacOS (via Homebrew)
brew install bat
# Arch Linux
sudo pacman -S bat
# Debian / Ubuntu
sudo apt install bat
```

* * *

### [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) - File Comparisons _(better `diff`)_

> `diff-so-fancy` gives you better looking diffs for comparing strings, files, directories and git changes. The change highlighting makes spotting changes much easier, and you can customize the output layout and colors

![diff-so-fancy-example-usage](https://i.ibb.co/RGKLhQk/diff-so-fancy.png)

[![View diff-so-fancy on GitHub](https://img.shields.io/github/stars/so-fancy/diff-so-fancy?color=232323&label=diff-so-fancy&logo=github&labelColor=232323)](https://github.com/so-fancy/diff-so-fancy)[![Author so-fancy](https://img.shields.io/badge/so-fancy-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/so-fancy) ![Written in Perl](https://img.shields.io/static/v1?label=&message=Perl&color=39457E&logo=perl&logoColor=FFFFFF)

```Install bash 
# MacOS (via Homebrew)
brew install diff-so-fancy
# Arch Linux
sudo pacman -S diff-so-fancy
# Debian / Ubuntu
sudo apt install diff-so-fancy
``` 

* * *

### [entr](https://github.com/eradman/entr) - Watch for changes

> `entr` lets you run an arbitrary command whenever file changes. You can pass a file, directory, symlink or regex to specify which files it should watch. It's really useful for automatically rebuilding projects, reacting to logs, automated testing, etc. Unlike similar projects, it uses kqueue(2) or inotify(7) to avoid polling, and improve performance

![entr-example-usage](https://i.ibb.co/HHKQx2H/entr.png)

[![View entr on GitHub](https://img.shields.io/github/stars/eradman/entr?color=232323&label=entr&logo=github&labelColor=232323)](https://github.com/eradman/entr)[![Author eradman](https://img.shields.io/badge/eradman-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/eradman) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

```Install bash 
# MacOS (via Homebrew)
brew install entr
# Arch Linux
sudo pacman -S entr
# Debian / Ubuntu
sudo apt install entr
``` 

* * *

### [exiftool](https://github.com/exiftool/exiftool) - Reading + writing metadata

> ExifTool is handy utility for reading, writing, stripping and creating meta information for a wide variety of file types. Never accidentally leak your location when sharing a photo again!

![exiftool-example-usage](https://i.ibb.co/Gv5PN6v/exiftool.png)

[![View exiftool on GitHub](https://img.shields.io/github/stars/exiftool/exiftool?color=232323&label=exiftool&logo=github&labelColor=232323)](https://github.com/exiftool/exiftool)[![Author exiftool](https://img.shields.io/badge/exiftool-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/exiftool) ![Written in Perl](https://img.shields.io/static/v1?label=&message=Perl&color=39457E&logo=perl&logoColor=FFFFFF)

* * *

### [fdupes](https://github.com/jbruchon/jdupes) - Duplicate file finder

> `jdupes` is used for identifying and/or deleting duplicate files within specified directories. It's useful for freeing up disk space when you've got two or more identical files

![fdupes-example-usage](https://i.ibb.co/jhSY2Nn/fdupes.png)

[![View jdupes on GitHub](https://img.shields.io/github/stars/jbruchon/jdupes?color=232323&label=jdupes&logo=github&labelColor=232323)](https://github.com/jbruchon/jdupes)[![Author jbruchon](https://img.shields.io/badge/jbruchon-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/jbruchon) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [fzf](https://github.com/junegunn/fzf) - Fuzzy file finder _(better `find`)_

> `fzf` is an extremely powerful, and easy to use fuzzy file finder and filtering tool. It lets you search for a string or pattern across files. fzf also has [plugins](https://github.com/junegunn/fzf/wiki/Related-projects) available for most shells and IDEs, for showing instant results while searching. This [post](https://www.freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff/) by Alexey Samoshkin highlights some of it's use cases.

![fzf-example-usage](https://i.ibb.co/LNcwjWm/fzf.gif)

[![View fzf on GitHub](https://img.shields.io/github/stars/junegunn/fzf?color=232323&label=fzf&logo=github&labelColor=232323)](https://github.com/junegunn/fzf)[![Author junegunn](https://img.shields.io/badge/junegunn-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/junegunn) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

```Install bash 
# MacOS (via Homebrew)
brew install fzf
# Arch Linux
sudo pacman -S fzf
# Debian / Ubuntu
sudo apt install fzf
``` 

* * *

### [hyperfine](https://github.com/sharkdp/hyperfine) - Command benchmarking

> `hyperfine` makes it easy to accurately benchmark and compare arbitrary commands or scripts. It takes care of warm-up runs, clearing the cache for accurate results and preventing interference from other programs. It can also export results as raw data and generate charts.

![hyperfine-example-usage](https://i.ibb.co/tKNR5gr/hyperfine.png)

[![View hyperfine on GitHub](https://img.shields.io/github/stars/sharkdp/hyperfine?color=232323&label=hyperfine&logo=github&labelColor=232323)](https://github.com/sharkdp/hyperfine)[![Author sharkdp](https://img.shields.io/badge/sharkdp-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/sharkdp) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

```Install bash 
# MacOS (via Homebrew)
brew install hyperfine
# Arch Linux
sudo pacman -S hyperfine
# Debian / Ubuntu
sudo apt install hyperfine
``` 

* * *

### [just](https://github.com/casey/just) - Modern command runner _(better `make`)_

> `just` is similar to `make` but with some nice additions. It let's you group your projects commands together into recopies, which can be easily listed and run. Supports aliases, positional arguments, different shells, dot env integration, string interprulation, and pretty much everything else you could need

[![View just on GitHub](https://img.shields.io/github/stars/casey/just?color=232323&label=just&logo=github&labelColor=232323)](https://github.com/casey/just)[![Author casey](https://img.shields.io/badge/casey-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/casey) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

```Install bash 
# MacOS (via Homebrew)
brew install just
# Arch Linux
sudo pacman -S just
# Debian / Ubuntu
sudo apt install just
``` 

* * *

### [jq](https://github.com/stedolan/jq) - JSON processor

> `jq` is like `sed`, but for JSON - you can use it to slice and filter and map and transform structured data with ease. It can be used to write complex queries to extract or manipulate JSON data. There's also a [jq playground](https://jqplay.org/) that you can use to try it out, or formulate queries with live feedback

[![View jq on GitHub](https://img.shields.io/github/stars/stedolan/jq?color=232323&label=jq&logo=github&labelColor=232323)](https://github.com/stedolan/jq)[![Author stedolan](https://img.shields.io/badge/stedolan-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/stedolan) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [most](https://www.jedsoft.org/most/) - Multi-window scroll pager _(better less)_

> `most` is a pager, for reading through long files or command outputs. `most` supports multi-windows and has the option to not wrap text

[![Author Jed](https://img.shields.io/badge/jed-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://www.jedsoft.org/aboutme.html) ![Written in S-Lang](https://img.shields.io/static/v1?label=&message=S_Lang&color=000000&logo=simkl&logoColor=FFFFFF)

* * *

### [procs](https://github.com/dalance/procs) - Process viewer _(better ps)_

> `procs` is an easy to navigate process viewer, it has colored highlighting, makes sorting and searching for processes easy, has tree view and updates in real-time

![procs-example-usage](https://i.ibb.co/y6qhgDX/procs-demo.gif)

[![View procs on GitHub](https://img.shields.io/github/stars/dalance/procs?color=232323&label=procs&logo=github&labelColor=232323)](https://github.com/dalance/procs)[![Author dalance](https://img.shields.io/badge/dalance-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/dalance) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [rip](https://github.com/nivekuil/rip) - Deletion tool _(better rm)_

> `rip` is a safe, ergonomic and performant deletion tool. It let's you intuitively remove files and directories, and easily restore deleted files

![rip-example-usage](https://i.ibb.co/10DTvT2/rip.gif)

[![View rip on GitHub](https://img.shields.io/github/stars/nivekuil/rip?color=232323&label=rip&logo=github&labelColor=232323)](https://github.com/nivekuil/rip)[![Author nivekuil](https://img.shields.io/badge/nivekuil-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/nivekuil) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [ripgrep](https://github.com/BurntSushi/ripgrep) - Search within files _(better `grep`)_

> `ripgrep` is a line-oriented search tool that recursively searches the current directory for a regex pattern. It can ignore the contents of `.gitignore` and skip binary files. It's able to search within compressed archives, or only search specific extension, and understands files using various encoding methods

![ripgrep-example-usage](https://i.ibb.co/qkMgQm9/ripgrep.png)

[![View ripgrep on GitHub](https://img.shields.io/github/stars/BurntSushi/ripgrep?color=232323&label=ripgrep&logo=github&labelColor=232323)](https://github.com/BurntSushi/ripgrep)[![Author BurntSushi](https://img.shields.io/badge/BurntSushi-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/BurntSushi) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [rsync](https://rsync.samba.org/) - Fast, incremental file transfer

> `rsync` lets you copy large files locally or to or from remote hosts or external drives. It can be used to keep files across multiple locations synced, and is perfect for creating, updating and restoring backups

[![View rsync on GitHub](https://img.shields.io/github/stars/WayneD/rsync?color=232323&label=rsync&logo=github&labelColor=232323)](https://github.com/WayneD/rsync)[![Author WayneD](https://img.shields.io/badge/WayneD-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/WayneD) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [sd](https://github.com/chmln/sd) - Find and replace _(better `sed`)_

> `sd` is an easy, fast and intuitive find and replace tool, based on string literals. It can be executed on a file, an entire directory, or any piped text

![sd-example-usage](https://i.ibb.co/G9CfcGS/sd.png)

[![View sd on GitHub](https://img.shields.io/github/stars/chmln/sd?color=232323&label=sd&logo=github&labelColor=232323)](https://github.com/chmln/sd)[![Author chmln](https://img.shields.io/badge/chmln-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/chmln) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [tre](https://github.com/dduan/tre) - Directory hierarchy _(better `tree`)_

> `tre` outputs a tree stye list of files for your current or a specified directory, with colors. When running with the `-e` option, it numbers each item, and creates a temporary alias that you can use to quickly jump to that location

![tre-example-usage](https://i.ibb.co/CmMrZLB/tre.png)

[![View tre on GitHub](https://img.shields.io/github/stars/dduan/tre?color=232323&label=tre&logo=github&labelColor=232323)](https://github.com/dduan/tre)[![Author dduan](https://img.shields.io/badge/dduan-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/dduan) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [xsel](https://github.com/kfish/xsel) - Access the clipboard

> `xsel` let's you read and write to the X Selection clipboard via the command line. It's useful for piping command output to the clipboard, or a copied data into a command

[![View xsel on GitHub](https://img.shields.io/github/stars/kfish/xsel?color=232323&label=xsel&logo=github&labelColor=232323)](https://github.com/kfish/xsel)[![Author kfish](https://img.shields.io/badge/kfish-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/kfish) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

* * *

CLI Monitoring and Performance Apps
-----------------------------------

### [bandwhich](https://github.com/imsnif/bandwhich) - Bandwidth utilization monitor

> Show bandwidth usage, connection information, outgoing hosts and DNS queries in real-time

![bandwhich-example-usage](https://i.ibb.co/8jHHBD3/Screenshot-from-2023-01-18-22-45-32.png)

[![View bandwhich on GitHub](https://img.shields.io/github/stars/imsnif/bandwhich?color=232323&label=bandwhich&logo=github&labelColor=232323)](https://github.com/imsnif/bandwhich)[![Author imsnif](https://img.shields.io/badge/imsnif-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/imsnif) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [ctop](https://github.com/bcicen/ctop) - Container metrics and monitoring

> Like `top`, but for monitoring resource usage for running (Docker and runC) containers. It shows real-time CPU, memory and network bandwidth as well as the name, status and ID of each container. There's also a built-in log viewer, and options to manage (stop, start, exec, etc) containers

![ctop-example-usage](https://i.ibb.co/xGjyzZ2/ctop.gif)

[![View ctop on GitHub](https://img.shields.io/github/stars/bcicen/ctop?color=232323&label=ctop&logo=github&labelColor=232323)](https://github.com/bcicen/ctop)[![Author bcicen](https://img.shields.io/badge/bcicen-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/bcicen) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [bpytop](https://github.com/aristocratos/bpytop) - Resource monitoring _(better `htop`)_

> `bpytop` is a fast, interactive, visual resource monitor. It shows top running processes, recent CPU, mem, disk and network history. From the interface you can navigate, sort and search - there's also support for custom color themes

![bpytop-example-usage](https://i.ibb.co/nj9jrhr/bpytop.gif)

[![View bpytop on GitHub](https://img.shields.io/github/stars/aristocratos/bpytop?color=232323&label=bpytop&logo=github&labelColor=232323)](https://github.com/aristocratos/bpytop)[![Author aristocratos](https://img.shields.io/badge/aristocratos-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/aristocratos) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [glances](https://github.com/nicolargo/glances) - Resource monitor + web and API

> `glances` is another resource monitor, but with a different feature set. It includes a fully responsive web view, a REST API and historical monitoring. It's easily extendable, and can be integrated with other services

![glances-example-usage](https://i.ibb.co/6g65Qy4/glances.gif)

[![View glances on GitHub](https://img.shields.io/github/stars/nicolargo/glances?color=232323&label=glances&logo=github&labelColor=232323)](https://github.com/nicolargo/glances)[![Author nicolargo](https://img.shields.io/badge/nicolargo-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/nicolargo) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [gping](https://github.com/orf/gping) - Interactive ping tool _(better `ping`)_

> `gping` can run ping tests on multiple hosts, while showing results in real-time graph. It can also be used to monitor execution time, when used with the `--cmd` flag

![gping-example-usage](https://i.ibb.co/CvG6xt0/gping.gif)

[![View gping on GitHub](https://img.shields.io/github/stars/orf/gping?color=232323&label=gping&logo=github&labelColor=232323)](https://github.com/orf/gping)[![Author orf](https://img.shields.io/badge/orf-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/orf) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [dua-cli](https://github.com/Byron/dua-cli) - Disk usage analyzer and monitor _(better `du`)_

> `dua-cli` let's you interactively view used and available disk space for each mounted drive, and makes freeing up storage easy

![dua-cli-usage-example](https://i.ibb.co/x3NbDLR/dua.gif)

[![View dua-cli on GitHub](https://img.shields.io/github/stars/Byron/dua-cli?color=232323&label=dua-cli&logo=github&labelColor=232323)](https://github.com/Byron/dua-cli)[![Author Byron](https://img.shields.io/badge/Byron-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/Byron) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [speedtest-cli](https://github.com/sivel/speedtest-cli) - Command line speed test utility

> `speedtest-cli` just runs an internet speed test, via speedtest.net - but straight from the terminal :)

![speedtest-cli-example-usage](https://i.ibb.co/25QCbdF/speedtest-cli.gif)

[![View speedtest-cli on GitHub](https://img.shields.io/github/stars/sivel/speedtest-cli?color=232323&label=speedtest-cli&logo=github&labelColor=232323)](https://github.com/sivel/speedtest-cli)[![Author sivel](https://img.shields.io/badge/sivel-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/sivel) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [dog](https://github.com/ogham/dog) - DNS lookup client _(better `dig`)_

> `dog` is an easy-to-use DNS lookup client, with support for DoT and DoH, nicely coloured outputs and the option to emit JSON

![dog-example-usage](https://i.ibb.co/48n617Q/dog.png)

[![View dog on GitHub](https://img.shields.io/github/stars/ogham/dog?color=232323&label=dog&logo=github&labelColor=232323)](https://github.com/ogham/dog)[![Author ogham](https://img.shields.io/badge/ogham-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/ogham) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

* * *

CLI Productivity Apps
---------------------

> Surf the web, play music, check emails, manage calendars, read the news and more, all without leaving the terminal!

### [browsh](https://github.com/browsh-org/browsh) - CLI web browser

> `browsh` is a fully interactive, real-time, and modern text-based browser rendered to TTYs and browsers. It supports both mouse and keyboard navigation, and is surprisingly feature rich for a purely terminal based application. It also mitigates battery drain issues that plague modern browsers, and with support for MoSH, you can experience faster load times due to reduced bandwidth

![browsh-example-usage](https://i.ibb.co/S7nLFX5/browsh.gif)

[![View browsh on GitHub](https://img.shields.io/github/stars/browsh-org/browsh?color=232323&label=browsh&logo=github&labelColor=232323)](https://github.com/browsh-org/browsh)[![Author browsh-org](https://img.shields.io/badge/browsh-org-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/browsh-org) ![Written in JavaScript](https://img.shields.io/static/v1?label=&message=JavaScript&color=F7DF1E&logo=javascript&logoColor=FFFFFF)

* * *

### [buku](https://github.com/jarun/buku) - Bookmark manager

> `buku` is a terminal-based bookmark manager, with tons of configuration, storage and usage options. There's also an optional [web UI](https://github.com/jarun/buku/tree/master/bukuserver#screenshots) and [browser plugin](https://github.com/samhh/bukubrow-webext#installation), for accessing your bookmarks outside of the terminal

![buku-example-usage](https://i.ibb.co/CWQsf1x/buku.png)

[![View buku on GitHub](https://img.shields.io/github/stars/jarun/buku?color=232323&label=buku&logo=github&labelColor=232323)](https://github.com/jarun/buku)[![Author jarun](https://img.shields.io/badge/jarun-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/jarun) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [cmus](https://github.com/cmus/cmus) - Music browser / player

> `cmus` is terminal music player, controlled with keyboard shortcuts. It has support for a wide range of audio formats and codecs, and allows organising tracks into playlists and applying playback settings

![cmus-example-usage](https://i.ibb.co/dP6b3bd/cmus.png)

[![View cmus on GitHub](https://img.shields.io/github/stars/cmus/cmus?color=232323&label=cmus&logo=github&labelColor=232323)](https://github.com/cmus/cmus)[![Author cmus](https://img.shields.io/badge/cmus-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/cmus) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [cointop](https://github.com/cointop-sh/cointop) - Track crypto prices

> `cointop` show current crypto prices, and track the price history of your portfolio. Supports price alerts, historical charts, currency conversion, fuzzy searching, and much more. You can try the demo via the web at [cointop.sh](https://cointop.sh/), or by running `ssh cointop.sh`

![cointop-example-usage](https://i.ibb.co/JBf9y4y/cointop.png)

[![View cointop on GitHub](https://img.shields.io/github/stars/cointop-sh/cointop?color=232323&label=cointop&logo=github&labelColor=232323)](https://github.com/cointop-sh/cointop)[![Author cointop-sh](https://img.shields.io/badge/cointop-sh-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/cointop-sh) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [ddgr](https://github.com/jarun/ddgr) - Search the web from the terminal

> `ddgr` is like [googler](https://github.com/jarun/googler), but for DuckDuckGo. It's fast, clean and easy, with support for instant answers, search completion, search bangs, and advanced search. It respects your privacy by default, and also has HTTPS proxy support, and works with Tor

![dggr-example-usage](https://i.ibb.co/S0H21QH/dggr.png)

[![View ddgr on GitHub](https://img.shields.io/github/stars/jarun/ddgr?color=232323&label=ddgr&logo=github&labelColor=232323)](https://github.com/jarun/ddgr)[![Author jarun](https://img.shields.io/badge/jarun-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/jarun) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [khal](https://github.com/pimutils/khal) - Calendar client

> `khal` is a terminal calendar app, which shows upcoming events, month and agenda views. You can sync it with any CalDAV calendar, and add, edit and remove events directly

![khal-example-usage](https://i.ibb.co/hLCdjZW/khal.png)

[![View khal on GitHub](https://img.shields.io/github/stars/pimutils/khal?color=232323&label=khal&logo=github&labelColor=232323)](https://github.com/pimutils/khal)[![Author pimutils](https://img.shields.io/badge/pimutils-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/pimutils) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [mutt](https://gitlab.com/muttmua/mutt) - Email client

> `mut` is a classic, a terminal based mail client for sending, reading and managing emails. It supports all mainstream email protocols and mailbox formats, allows for attachments, BCC/CC, threads, mailing lists and delivery status notifications

![mutt-example-usage](https://i.ibb.co/zVVsG3s/mutt.webp)

[![View mutt on GitHub](https://img.shields.io/github/stars/muttmua/mutt?color=232323&label=mutt&logo=github&labelColor=232323)](https://gitlab.com/muttmua/mutt)[![Author muttmua](https://img.shields.io/badge/muttmua-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/muttmua) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [newsboat](https://github.com/newsboat/newsboat) - RSS / ATOM news reader

> `newsboat` is an RSS feed reader and aggregator, for reading the news, blogs and following updates directly from the terminal

![newsboat-example-usage](https://i.ibb.co/fvT4YzD/newsboat.png)

[![View newsboat on GitHub](https://img.shields.io/github/stars/newsboat/newsboat?color=232323&label=newsboat&logo=github&labelColor=232323)](https://github.com/newsboat/newsboat)[![Author newsboat](https://img.shields.io/badge/newsboat-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/newsboat) ![Written in C++](https://img.shields.io/static/v1?label=&message=C++&color=00599C&logo=cplusplus&logoColor=FFFFFF)

* * *

### [rclone](https://github.com/rclone/rclone) - Manage cloud storage

> `rclone` is a handy utility for syncing files and folders to various cloud storage providers. It can be either invoked directly from the command line, or easily integrated into a script as a replacement for heavy desktop sync apps

[![View rclone on GitHub](https://img.shields.io/github/stars/rclone/rclone?color=232323&label=rclone&logo=github&labelColor=232323)](https://github.com/rclone/rclone)[![Author rclone](https://img.shields.io/badge/rclone-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/rclone) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [taskwarrior](https://github.com/GothenburgBitFactory/taskwarrior) - Todo + task management

> `task` is a CLI task management/ todo app. It's both simple and unobtrusive, but also incredibly powerful and scalable, with advanced organisation and query features built in. There's also a lot (700+!) of extra [plugins](https://taskwarrior.org/tools/) for extending it's functionality and integrating with third-party services

![task-warrior-example-usage](https://i.ibb.co/7k6M37g/taskwarrior.jpg)

[![View taskwarrior on GitHub](https://img.shields.io/github/stars/GothenburgBitFactory/taskwarrior?color=232323&label=taskwarrior&logo=github&labelColor=232323)](https://github.com/GothenburgBitFactory/taskwarrior)[![Author GothenburgBitFactory](https://img.shields.io/badge/GothenburgBitFactory-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/GothenburgBitFactory) ![Written in C++](https://img.shields.io/static/v1?label=&message=C++&color=00599C&logo=cplusplus&logoColor=FFFFFF)

* * *

### [tuir](https://gitlab.com/ajak/tuir) - Terminal UI for Reddit

> `tuir` is a great one if you want to look like you're working, while actually browsing Reddit! It's got intuitive keybindings, custom themes, and can render images and multi-media content too. There's also [haxor](https://github.com/donnemartin/haxor-news) for hacker news

![tuir-example-usage](https://i.ibb.co/vzSw7s5/tuir.png)

[![View tuir on GitLab](https://img.shields.io/gitlab/stars/ajak/tuir?color=fc6d26&label=tuir&logo=gitlab&labelColor=232323)](https://gitlab.com/ajak/tuir)[![Author ajak](https://img.shields.io/badge/ajak-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/ajak) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

* * *

CLI Dev Suits
-------------

### [httpie](https://github.com/httpie/httpie) - HTTP / API testing testing client

> `httpie` is a HTTP client, for testing, debugging and using APIs. It supports everything you'd expect - HTTPS, proxies, authentication, custom headers, persistent sessions, JSON parsing. Usage is simple with an expressive syntax and colourized output. Like other HTTP clients (Postman, Hopscotch, Insomnia, etc) HTTPie also includes a web UI

![httpie-example-usage](https://i.ibb.co/Wk5S19g/httpie.png)

[![View httpie on GitHub](https://img.shields.io/github/stars/httpie/httpie?color=232323&label=httpie&logo=github&labelColor=232323)](https://github.com/httpie/httpie)[![Author httpie](https://img.shields.io/badge/httpie-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/httpie) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [lazydocker](https://github.com/jesseduffield/lazydocker) - Full Docker management app

> `lazydocker` is a Docker management app, that lets you view all containers and images, manage their state, read logs, check resource usage, restart/ rebuild, analyse layers, prune unused containers, images and volumes, and so much more. It saves you from needing remember, type and chain multiple Docker commands.

![lazy-docker-example-usage](https://i.ibb.co/MD8MWNH/lazydocker.png)

[![View lazydocker on GitHub](https://img.shields.io/github/stars/jesseduffield/lazydocker?color=232323&label=lazydocker&logo=github&labelColor=232323)](https://github.com/jesseduffield/lazydocker)[![Author jesseduffield](https://img.shields.io/badge/jesseduffield-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/jesseduffield) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [lazygit](https://github.com/jesseduffield/lazygit) - Full Git management app

> `lazygit` is a visual git client, on the command line. Easily add, commit and puch files, resolve conflicts, compare diffs, manage logs, and do complex operations like squashes and rewinds. There's keybindings for everything, colors, and it's easily configurable and extenable

![lazy-git-example-usage](https://i.ibb.co/KLF3C6s/lazygit.png)

[![View lazygit on GitHub](https://img.shields.io/github/stars/jesseduffield/lazygit?color=232323&label=lazygit&logo=github&labelColor=232323)](https://github.com/jesseduffield/lazygit)[![Author jesseduffield](https://img.shields.io/badge/jesseduffield-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/jesseduffield) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [kdash](https://github.com/kdash-rs/kdash/) - Kubernetes dashboard app

> `kdash` is an all-in-one Kubernetes management tool. View node metrics, watch resources, stream container logs, analyse contexts and manage nodes, pods and namespaces

[![View kdash on GitHub](https://img.shields.io/github/stars/kdash-rs/kdash?color=232323&label=kdash&logo=github&labelColor=232323)](https://github.com/kdash-rs/kdash/)[![Author kdash-rs](https://img.shields.io/badge/kdash-rs-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/kdash-rs) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [gdp-dashboard](https://github.com/cyrus-and/gdb-dashboard) - Visual GDP debugger

> `gdp-dashboard` adds a visual element to the GNU Debugger, for debugging C and C++ programs. Easily analyse memory, step through breakpoints, and view registers

![gdp-dashboard-example-usage](https://i.ibb.co/2g2hVLh/gdp-dashboard.png)

[![View gdb-dashboard on GitHub](https://img.shields.io/github/stars/cyrus-and/gdb-dashboard?color=232323&label=gdb-dashboard&logo=github&labelColor=232323)](https://github.com/cyrus-and/gdb-dashboard)[![Author cyrus-and](https://img.shields.io/badge/cyrus-and-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/cyrus-and) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

* * *

CLI External Sercvices
----------------------

### [ngrok](https://ngrok.com/) - Reverse proxy for sharing localhost

> `ngrok` safely\* exposes your localhost to the internet behind a unique URL. This lets you share what you're working on with you're remote colleagues, in real-time. Usage is [very simple](https://notes.aliciasykes.com/p/RUi22QSyWe), but it's also got a lot of advanced features for things like authentication, webhooks, firewalls, traffic inspection, custom/ wildcard domains and much more

![ngrok-example-usage](https://i.ibb.co/4WPZNGx/ngrok.png)

[![View ngrok on GitHub](https://img.shields.io/github/stars/inconshreveable/ngrok?color=232323&label=ngrok&logo=github&labelColor=232323)](https://github.com/inconshreveable/ngrok)[![Author inconshreveable](https://img.shields.io/badge/inconshreveable-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/inconshreveable) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [tmate](https://tmate.io/) - Share a terminal session via internet

> `tmate` let's you instantly share a live terminal session with someone elsewhere in the world. It works across different systems, supports access control/ auth, can be self-hosted, and has all the features of Tmux

[![View tmate on GitHub](https://img.shields.io/github/stars/tmate-io/tmate?color=232323&label=tmate&logo=github&labelColor=232323)](https://github.com/tmate-io/tmate)[![Author tmate-io](https://img.shields.io/badge/tmate-io-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/tmate-io) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [asciinema](https://asciinema.org/) - Recording + sharing terminal sessions

> `asciinema` is very useful for easily recording, sharing and embedding a terminal session. Great to showcase something you've built, or to show the command-line steps for a tutorial. Unlike screenrecording videos, the user can copy-paste the content, change the theme on the fly and control playback

{% embed [https://asciinema.org/a/335480?speed=3](https://asciinema.org/a/335480?speed=3) %}

[![View asciinema on GitHub](https://img.shields.io/github/stars/asciinema/asciinema?color=232323&label=asciinema&logo=github&labelColor=232323)](https://github.com/asciinema/asciinema)[![Author asciinema](https://img.shields.io/badge/asciinema-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/asciinema) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

### [navi](https://github.com/denisidoro/navi) - Interactive cheat sheet

> `navi` allows you to browse through cheatsheets and execute commands. Suggested values for arguments are dynamically displayed in a list. Type less, reduce mistakes and save yourself from having to memorise thousands of commands. It integrates with [tldr](https://github.com/tldr-pages/tldr) and [cheat.sh](https://github.com/chubin/cheat.sh) to get content, but you can also import other cheatsheets, or even write your own

{% embed [https://asciinema.org/a/406461?speed=2](https://asciinema.org/a/406461?speed=2) %}

[![View navi on GitHub](https://img.shields.io/github/stars/denisidoro/navi?color=232323&label=navi&logo=github&labelColor=232323)](https://github.com/denisidoro/navi)[![Author denisidoro](https://img.shields.io/badge/denisidoro-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/denisidoro) ![Written in Rust](https://img.shields.io/static/v1?label=&message=Rust&color=e86243&logo=rust&logoColor=FFFFFF)

* * *

### [transfer.sh](https://github.com/dutchcoders/transfer.sh/) - Fast file sharing

> `transfer` makes uploading and sharing files really easy, directly from the command line. It's free, supports encryption, gives you a unique URL, and can also be self-hosted.  
> I've written a Bash helper function to make usage a bit easier, you can [find it here](https://github.com/Lissy93/dotfiles/blob/master/utils/transfer.sh) or try it out by running `bash <(curl -L -s https://alicia.url.lol/transfer)`

![transfer-sh-example-usage](https://i.ibb.co/cCqDb1k/transfer-sh.png)

[![View transfer.sh on GitHub](https://img.shields.io/github/stars/dutchcoders/transfer.sh?color=232323&label=transfer.sh&logo=github&labelColor=232323)](https://github.com/dutchcoders/transfer.sh)[![Author dutchcoders](https://img.shields.io/badge/dutchcoders-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/dutchcoders) ![Written in Go](https://img.shields.io/static/v1?label=&message=Go%20Lang&color=00ADD8&logo=go&logoColor=FFFFFF)

* * *

### [surge](https://surge.sh/) - Deploy a site in seconds

> `surge` is a free static hosting provider, that you can deploy to directly from the terminal in a single command, just run `surge` from within your `dist` directory! It supports custom domains, auto SSL certs, pushState support, cross-origin resource support - and it's free!

![surge-sh-example-usage](https://i.ibb.co/NynprxZ/surge-sh.png)

* * *

### [wttr.in](https://github.com/chubin/wttr.in) - Check the weather

> `wttr.in` is a service that displays the weather in a format that's digestible in the command line. Just run `curl wttr.in` or `curl wttr.in/London` to try it out. There's URL parameters to customise what data is returned, as well as the format

![wrrt-in-example-usage](https://i.ibb.co/J2JWnYT/Screenshot-from-2023-01-18-21-10-54.png)

[![View wttr.in on GitHub](https://img.shields.io/github/stars/chubin/wttr.in?color=232323&label=wttr.in&logo=github&labelColor=232323)](https://github.com/chubin/wttr.in)[![Author chubin](https://img.shields.io/badge/chubin-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/chubin) ![Written in Python](https://img.shields.io/static/v1?label=&message=Python&color=3C78A9&logo=python&logoColor=FFFFFF)

* * *

* * *

CLI Fun
-------

### [cowsay](https://en.wikipedia.org/wiki/Cowsay) - Have an ASCII cow say your message

> `cowsay` is a configurable talking cow. It's based off the [original](https://github.com/tnalpgge/rank-amateur-cowsay) by Tony Monroe

![cowsay-example-usage](https://i.ibb.co/TRqW3jD/cowsay.png)

[![View cowsay on GitHub](https://img.shields.io/github/stars/piuccio/cowsay?color=232323&label=cowsay&logo=github&labelColor=232323)](https://github.com/piuccio/cowsay)[![Author piuccio](https://img.shields.io/badge/piuccio-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/piuccio) ![Written in JavaScript](https://img.shields.io/static/v1?label=&message=JavaScript&color=F7DF1E&logo=javascript&logoColor=FFFFFF)

* * *

### [figlet](http://www.figlet.org/) - Output text as big ASCII art text

> `figlet` outputs text as ASCII art

![figlet-example-usage](https://i.ibb.co/fk4T7D0/figlet.png)

[![View figlet on GitHub](https://img.shields.io/github/stars/cmatsuoka/figlet?color=232323&label=figlet&logo=github&labelColor=232323)](https://github.com/cmatsuoka/figlet)[![Author cmatsuoka](https://img.shields.io/badge/cmatsuoka-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/cmatsuoka) ![Written in C](https://img.shields.io/static/v1?label=&message=C&color=A8B9CC&logo=c&logoColor=FFFFFF)

* * *

### [lolcat](https://github.com/busyloop/lolcat) - Make console output raibow colored

> `lolcat` makes any text passed to it rainbow coloured

![lolcat-example-usage](https://i.ibb.co/nfp9Ycx/lolcat.png)

[![View lolcat on GitHub](https://img.shields.io/github/stars/busyloop/lolcat?color=232323&label=lolcat&logo=github&labelColor=232323)](https://github.com/busyloop/lolcat)[![Author busyloop](https://img.shields.io/badge/busyloop-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/busyloop) ![Written in Ruby](https://img.shields.io/static/v1?label=&message=Ruby&color=CC342D&logo=ruby&logoColor=FFFFFF)

* * *

### [neofetch](https://github.com/dylanaraps/neofetch) - Show system data and ditstro info

> `neofetch` prints distro and system info (so you can flex that you use Arch btw on r/unixporn)

![neofetch-example-usage](https://i.ibb.co/x1PHpFC/Screenshot-from-2023-01-18-22-44-28.png)

[![View neofetch on GitHub](https://img.shields.io/github/stars/dylanaraps/neofetch?color=232323&label=neofetch&logo=github&labelColor=232323)](https://github.com/dylanaraps/neofetch)[![Author dylanaraps](https://img.shields.io/badge/dylanaraps-b820f9?labelColor=b820f9&logo=githubsponsors&logoColor=fff)](https://github.com/dylanaraps) ![Written in Bash](https://img.shields.io/static/v1?label=&message=Bash&color=green&logo=gnubash&logoColor=FFFFFF)

As an example, I'm using `cowsay`, `figlet`, `lolcat` and `neofetch` to create a custom time-based MOTD shown to the user when they first log in. It greets them by their name, shows server info and time, date, weather and IP. [Here's the source code](https://github.com/Lissy93/dotfiles/blob/master/utils/welcome-banner.sh).

![welcome](https://i.ibb.co/cTg0jyn/Screenshot-from-2023-01-18-22-59-28.png)

* * *

* * *

Installations and Management
----------------------------

Most of us have a core set of CLI apps and utils that we rely upon. Setting up a new machine, and individually installing each program would get tiresome very quickly. So the task of installing and updating your terminal apps is the perfect candidate for automation. [Here](https://github.com/Lissy93/dotfiles/tree/master/scripts/installs) are some example scripts I've written, which can be easily dropped into your dotfiles or just run independently to ensure you're never missing an app.

For MacOS users, the easiest method is using [Homebrew](https://brew.sh/). Just create a Brewfile (with `touch ~/.Brewfile`), then list each of your apps, and run `brew bundle`. You can keep your package list backed up, by putting it in a Git repo. Here's an example one, to get you started: [https://github.com/Lissy93/Brewfile](https://github.com/Lissy93/Brewfile)

On Linux, you usually want to use the native package manager (e.g. `pacman`, `apt`). As an example, [here's a script](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/arch-pacman.sh) to install the above apps on Arch Linux systems

Desktop apps on Linux can be managed in a similar way, via Flatpak. Again, [here's an example script](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/flatpak.sh) :)

* * *

Conclusion
----------

... So that's it - a list of handy CLI apps, and a method for installing and keeping them up-to-date across your systems.

Hopefully some of these will be useful to some of you :)

#### What wasn't included

*   This list doesn't include the basics, like Vim, Tmux, Ranger, ZSH, Git, etc - which you're likely already using
*   I've also not included anything too niche, or only specific to a small number of users
*   Nothing system-specific, or that isn't cross-platform (Linux/ Unix, MacOS) is included
*   And I've not included apps which relate to the terminal, but are not CLI apps (like terminal emulators)
*   For most of the projects listed, there's a plethora of alternatives that achieve similar things, for brevity those also weren't included

#### Credit

Huge kudos to the authors, and communities behind each of these apps. Without them and their hard work, our life in the command line would be much less awesome. Where possible, I've tried to credit the authors, but if I've missed any - let me know below, and I'll push an update

#### Find More

If you were enjoying this, I recommend also checking out:

*   **[terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy)** by Nikolaos Kamarinakis
*   **[awesome-shell](https://github.com/alebcay/awesome-shell)** by Caleb Xu
*   **[awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)** by Adam Garrett-Harris

If you're new to the command line, then **[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)** by Joshua Levy is an excellent resource, as is the **[Bash Guide](https://github.com/Idnan/bash-guide)** by Adnan Ahmed.

And if you are looking for inspiration, you'll love **[r/unixporn](https://www.reddit.com/r/unixporn/)** ⚡

If you like this kind of stuff,  
consider following for more :)

[![Follow Lissy93 on GitHub](https://img.shields.io/badge/-Lissy93-3a3a3a?style=flat&logo=GitHub&logoColor=white)](https://github.com/Lissy93)[![Follow Lissy_Sykes on Twitter](https://img.shields.io/badge/-@Lissy_Sykes-00acee?style=flat&logo=Twitter&logoColor=white)](https://twitter.com/Lissy_Sykes)

.post-body.p1 img, .post-body.p1 small, .post-body.p1 blockquote { max-width: 600px !important; margin: 0.25rem auto; border-radius: 5px; } .post-body.p1 blockquote { margin: 1rem auto; } .post-body.p1 img { box-shadow: 1px 2px 4px 2px #090909cf; } .post-body.p1 h2 { font-size: 1.8rem !important; max-width: 800px; margin: 1rem auto 0.25rem auto; text-align: center; } .post-body.p1 h3 { font-size: 1.5rem !important; border-top: 3px solid var(--post-code-border-color); padding: 1rem 0 0; max-width: 600px; margin: 1rem auto; }
