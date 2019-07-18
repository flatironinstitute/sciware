# Some Useful Information and Resources on Zsh + Git, Vim

## Sciware: Tools and Workflow Show and Tell

Date: July 18, 2019

Presenter: Nils Wentzell

My config files can be found [here](https://github.com/wentzell/dotfiles)

# Zsh

## Why should you use it?

* Powerful globbing expressions
* Intelligent autocompletion and autocorrection
* Plugin-based through [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
* Powerful and customizeable command line prompts
* Git command line integration

## Installation

* Install through system package manager (recommended) or compile from [source](https://github.com/zsh-users/zsh)
* Initial configuration setup through [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
* Use `chsh -s $(which zsh)` to change your default shell or ask SCC to change it for you on the ldap based linux workstations

## Some remarks

* Enable extended globbing by adding `setopt extendedglob` to your ~/.zshrc
* Enable completion by adding `autoload -Uz compinit` to you ~/.zshrc

## Some globbing examples

* `ls **/a.out` -- Find a.out recursing into all subdirectories
* `ls *.(c|h)`  -- Files ending in .h or .c (Groupings)
* `ls <10-13>.txt` -- List files with matching the integer range
* `ls *.^c` -- Negation, files not ending in c
* `ls **/<10-13>*.(c|h)` -- Combine them

## Pattern Globbing examples

* `ls *(.)` -- regular files
* `ls *(x)` -- executable files
* `ls *(.x)` -- regular executable files
* `ls *(@)` -- links
* `ls *(W)` -- world-writeable files
* `ls *(R)` -- world-readable files

## Don't forget your command history reverse search (Ctrl + R)

# git

## Useful alias for command line branch history viewing

* Set the alias for `git l` using `git config --global alias.l "log --graph --abbrev-commit --decorate --format=format:'%C(blue)%h%C(reset) - %C(cyan)%aD%C(reset) %C(green)(%ar)%C(reset)%C(yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all"`

# Vim

## Plugin Managers

* Vundle --  [https://github.com/VundleVim/Vundle.vim](https://github.com/VundleVim/Vundle.vim)
* vim-plug -- [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)

## A small selection of plugins I use

* [vim-scripts/GrepCommands](github.com/vim-scripts/GrepCommands) - Useful commands to grep through multiple files at once
* [scrooloose/nerdcommenter](github.com/scrooloose/nerdcommenter) - Easy commenting / uncommenting of blocks for various programming languages
* [prabirshrestha/vim-lsp](github.com/prabirshrestha/vim-lsp) - Add support for the Language Server Protocol to use tools such as e.g. [clangd](https://clang.llvm.org/extra/clangd/) and [pyls](https://github.com/palantir/python-language-server)
* [vim-airline/vim-airline](github.com/vim-airline/vim-airline) - Nice status bar

# Language Server Protocol

* Separate programming language support from the editor / IDE
* Provides functionality such as auto completion, jump to definition, variable replacements, compiler errors and warnings, ...
* Initially developed for VSCode, now an open standard
* Integrates with many editors
