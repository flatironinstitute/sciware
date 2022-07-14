# Sciware

## Command line and Shell interaction

https://sciware.flatironinstitute.org/23_CommandLine

https://github.com/flatironinstitute/learn-sciware-dev/tree/main/23_CommandLine


## Rules of Engagement

### Goal:

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, *technology choices*\*, and scientific disciplines.

<small>\*though sometimes we try to expand your options</small>


## Rules of Engagement

- Avoid discussions between a few people on a narrow topic
- Provide time for people who haven't spoken to speak/ask questions
- Provide time for experts to share wisdom and discuss
- Work together to make discussions accessible to novices

<small>
(These will always be a work in progress and will be updated, clarified, or expanded as needed.)
</small>


## Zoom Specific

- Dedicated Zoom moderator to field questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/).


## Future Sessions

- Planning for this fall
   - How types can help you think about programs
   - File formats, data management, hdf5
   - Modern C++
- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

- 



## Overview

One often hears these terms used interchangeably. Let's clarify.

* Operating System
* Shell
* Terminal
* Command Line
* Console


### Operating System

- The base programs and libraries that define and control what a computer runs
- Made up of many parts:
   - a kernel: controls hardware and manages processes
   - "user space" processes: daemons (servers), applications, desktop

<small>_Linux_ 🐧 can refer to both a kernel and the various OSs built on that kernel.</small>


### Terminal

- _Terminal_ is a program that provides I/O (input/output) between a shell (or other program) and a display
- Originally a physical device to interact with remote computers, now we run software terminal _emulators_
- Many different terminal emulators (Gnome Terminal, iTerm, Terminator, xterm)


### Command Line

- Any programs that run inside the terminal, that only interact with text and typing
  - _Command line interface_ (CLI), as opposed to a _graphical user interface_ (GUI)
- _Console_ can be used to mean text terminal or command-line
  - "Print to the console": display output on the command-line, which you see in the terminal ("standard out")
  - Originally referred to the physical text entry and display device on a computer
- While a terminal usually runs locally (on the computer in front of you), the programs in it may be running remotely (like over ssh)


### Shell

- A _Shell_ is a program that lets you enter commands, passes them to the operating system to run
- Usually the first program that runs in a terminal

<small>The shell interface surrounds the kernel just as a nutshell surrounds a nut 🥜.</small>


<img src="assets/desktop-terminal-shell.png" width="100%" style="border:0;box-shadow:none">


### Common Shells

- `bash`: Bourne Again SHell, an enhanced version of the shell written by Steve Bourne
   - default interactive on most Linux systems
   - most common shell for shell scripts
- `zsh`: a modern interactive shell
   - compatible with bash (mostly superset of features)
   - default on MacOS (replacing bash in 2019, for licensing reasons)
- Other shells: `fish`, `ksh`, `tcsh`, ...


### Shell startup process

- Shells run certain scripts when they start, commonly called "dotfiles", containing configuration and setup
- Can easily break your shell, prevent logins (ex: `exit`)

<!-- TODO: vertical borders -->
<table class="vert">
<thead><tr><th>shell</th><th style="text-align: center;">login (ssh)</th><th style="text-align: center;">interactive</th><th>neither</th></tr></thead>
<tbody>
<tr><td rowspan='2'>bash</td><td style="text-align: center;"><code>.bash_profile</code> | <code>.bash_login</code> | <code>.profile</code></td><td style="text-align: center;"><code>.bashrc</code></td><td style="text-align: center;">-</td></tr>
<tr>   <td style="text-align: center;"><code>.bash_logout</code></td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr>
<tr><td rowspan='4'>zsh</td><td colspan='3' style="text-align: center;"><code>.zshenv</code></td></tr>
<tr>   <td style="text-align: center;"><code>.zprofile</code></td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr>
<tr>   <td colspan='2' style="text-align: center;"><code>.zshrc</code></td><td style="text-align: center;">-</td></tr>
<tr>   <td style="text-align: center;"><code>.zlogin</code>, <code>.zlogout</code></td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr>
</tbody>
</table>


#### Changing your shell

- Most systems: `chsh`
- FI: https://fido.flatironinstitute.org/
- caveat: some things only work out of the box in bash (modules, source)



## Interacting

### Nomenclature/shorthand/tips
- Default shell interaction is based on `Emacs` keybindings, though there are vim bindings as well
- We use `^A` as shorthand for the 'chord' `Control + a` together
- `Alt-X` keybindings might not work without proper terminal configuration (e.g. `Alt` sends `Meta` in `Iterm.app`)
- `Alt-X` keybindings can be simulated by hitting `Esc` and then the character after releasing


### Tab completion

- once, twice
- zsh more


### Navigating

- `Left` (`^B`), `Right` (`^F`) [Move back and forward a character]
- `^Left` (`Alt-B`), `^Right` (`Alt-F`) [Move back and forward a word]
- `Home` (`^A`) [Jump to beginning of line]
- `End` (`^E`) [Jump to end of line]


### Editing
Shells have a builtin clipboard 'kill ring' where 'cuts' add new entries to the ring.

- `^K` [Cut "kill" to end of line from cursor]
- `^U` [Cut line from beginning to end]
- `^W` (`Alt-BS`) [Cut previous word - repeating adds to the last cut]
- `^Y` [Paste whatever was last cut, `Alt-Y` after to cycle through the kill ring]


### History

- `Up` (`^N`), `Down` (`^P`) [Go to previous/next command in history of commands]
- `history 10` [Print last 10 commands you entered]
- `^R` [Search history. After matching, pressing `^R` repeatedly will go to previous matches]


### Processes

- ^C [Send 'interrupt' signal to current process, usually stopping it]
- ^D EOF [Kills most interactive sessions, if line is empty (your current shell, python repl, etc)]
- ^Z ... [Pause current running process and background it]

- jobs [List currently backgrounded jobs]
- bg [Unpause last backgrounded job, keeping in background]
- fg [Unpause last backgrounded job, bringing back to foreground]
- %1
- (interactive)
- `&`
- `wait`

- tmux/screen?


### Evaluation

what happens when you type something

- which
- `$PATH`

- `alias`


### Directories

- `pwd`
- `cd DIR`, `cd`, `cd -`



## TODO

- prompt customization
- scripting


### Environment control


#### Environment variables

- Conventionally upper case (`$PATH`, `$HOME`, etc.)
- Can list with `export` or `env` command
- Set with `export` command
- Delete with `unset` command
- Set only for a child process by prepending
```sh
$ export FI="the GOAT"
$ echo "flatiron is... $FI"
flatiron is... the GOAT
$ MY_ENV_VAR="Environment fun!" echo "Woo! $MY_ENV_VAR"
Woo! Environment fun!
$ echo "Woo! $MY_ENV_VAR"
Woo!
```


#### Variable expansion

- `foo=bar`, `file=mydata.csv`
- Concatenate: `${foo}stool` -> `barstool`


#### Executing shell scripts: `source`

- `source myscript.sh` will execute the script in the current shell (as if you typed them)
   - all variables set in the file will persist in your shell after execution is complete
- Vs. running a script in a child process:
   - `bash myscript.sh`
   - the variables will **not** persist into your current shell


### Environment Management

- there are a number of tools that change your environment, add things to PATH
- can be used inside scripts (not in your .bashrc)
- `module`
- `conda`, `venv`, etc.
- `source`



## Configuring your prompt 🎨

- prompt can show information about your environment

### ⚠️ Warning ⚠️

- Customizing your prompt can have hidden costs.  Avoid anything that hides expensive operations behind a "simple" interface (e.g., 🌈 ls aliases).


### Prompt design

 - Only include what you will actually use.
 - That said, don't be afraid to add a little ✨.
 - ♥ ☆ Try a new starting character(s) ʕ•ᴥ•ʔ.
 - Need inspo? ASCII Art Archive https://www.asciiart.eu/
 - ANSI escape sequences for colors: https://gist.github.com/vratiu/9780109
 - Powerline: https://github.com/powerline/powerline


### Off the shelf options

- Oh-my-zsh:
  - _ 🙃 A delightful community-driven framework for managing your zsh configuration. Includes 200+ optional plugins, over 140 themes to spice up your morning, and an auto-update tool._
  - Can cause ⚠️ performance issues, so I recommend using the themes on github for inspiration.

<img src="img/oh-my-zsh-themes.gif" width="600" style="border:0;box-shadow:none">


### Off the shelf options

- Powerline:
  - _ A statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile._

<img src="img/powerline.png" width="1000" style="border:0;box-shadow:none">


### Prompt variables (bash)

- `PS1`: default interactive prompt.
- `PROMPT_COMMAND`: executed just before PS1, often used for timestamps.
- Other prompt variables (PS2, 3, 4...) exist to manage specific conditions like select loops, continuation, and tracing.
- Check out ss64 for reference info on `bash` prompt special characters, colors, and prompt variables:  https://ss64.com/bash/syntax-prompt.html


### Accessing git branch (bash)

- Homebrew bash autocompletion / git comes with `__git_ps1` predefined to display the branch.
- Otherwise you can use the following function to find the active git branch.

```sh
  function parse_git_branch {
    git symbolic-ref --short HEAD 2> /dev/null
  }
```


### Example prompt (bash)

- Show some 💛 for FI with this prompt:

```sh
  # Define the prompt character
  char="♥"

  # Define some local colors
  red="\[\e[0;31m\]"
  blue="\[\e[0;34m\]"
  green="\[\e[0;32m\]"
  gray_text_blue_background="\[\e[37;44;1m\]"

  # Define a variable to reset the text color
  reset="\[\e[0m\]"

  # Export PS1:  default interactive prompt
  PS1="\[\e]2;\u@\h\a[$gray_text_blue_background\t$reset]$red\$(parse_git_branch) $green\W\n$blue//$red $char $reset"
```


### Prompt variables (zsh)

- `PROMPT`: default is `%m%#`
  - %m: short form of the current hostname
  - %#:  stands for a % or a #, depending on whether the shell is running as root or not.
- `RPROMPT`: right side prompt variable. `RPROMPT='%t'`

<img src="img/zsh-theme-3.png" width="1000" style="border:0;box-shadow:none">


###  Accessing git branch (zsh)

```zsh
  autoload -Uz vcs_info
  precmd() {vcs_info}
  zstyle ':vcs_info:git:*' formats '%F{yellow}%B% (%b)'
```

- Enable `vcs_info` function and call it in a pre-command.
- `zstyle`: builtin command is used to define and lookup styles stored as pairs of names and values.


### Example prompt (bash)

- `PROMPT_SUBST`: expands the parameters usable in the prompt.
- `%F{green}%B%`: Named colors must be surrounded by the escape characters.
- The final `%F{black}%B%` sets the color for the
- Showing the same FI love.

```zsh
  setopt PROMPT_SUBST
  PROMPT='%F{green}%B% %c ${vcs_info_msg_0_} %F{blue}%B% // %F{red}%B% ♥ %F{black}%B%'
```

<img src="img/fi-prompt.png" width="1000" style="border:0;box-shadow:none">



## Shell commands and scripting

- `ls`
- `rm`, `rm -r`
- `mkdir`
- `mv`

- `cat`
- `echo`
- `>`, `>>`
- `|`
- a bit about stderr

- quoting
- globs

- `if`, `for`



## Please give us feedback

### TBD: survey link



## Other resources


* shell scripting
* slurm
* fzf


## Environment variables

[EnvironmentVariables.md](https://sciware.flatironinstitute.org/10_EnvShell/EnvironmentVariables.html)


### Shell Comparison

#### History

<img src="img/evolve.svg" width="1000" style="border:0;box-shadow:none">

- run commands, interactive
- slowly developed more scripting features
- control structure syntax: ALGOL (`fi`, `esac`), C (`{}`)


#### Evolution

- ksh introduced functions
- tcsh invented history, alias, other interactive features
- POSIX.2 standardized minimal /bin/sh features (see `dash`)
- bash developed (and spun off) readline, key bindings
     - emacs mode, vi mode, custom bindings in `.inputrc`
- zsh added sophisticated tab-completion, prompts
     - <small>`git diff <tab>`, `rsync host:<tab>`, `gcc -<tab>`</small>
     - more permissive license, adopted by Apple as default (as of Catalina, Nov 2019)

most modern shells copied, adopted similar, popular features


#### Preferences

- bash
  - most common shell, especially for scripting
  - often assumed default
  - lags behind, catches up
- tcsh: fallen out of favor, non-POSIX, still maintained
- zsh
  - large, superset of **compatible with bash** and tcsh
  - many interactive and scripting features
  - [oh my zsh](https://ohmyz.sh/) ([plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins), [themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes))
- opinions?


- change shell alternative: exec different shell from `.bash_profile` (careful!)

```sh
if [[ $- == *i* && -x /bin/zsh ]] ; then
	SHELL=/bin/zsh exec /bin/zsh -l
fi
```


- Remove prefix: `${file##*.}` -> `csv`
- Remove suffix: `${file%%.*}` -> `mydata`
- Substitute prefix: `${file/#*./data.}` -> `data.csv`
- Substitute suffix: `${file/%.*/.bin}` -> `mydata.bin`
- Brace expansion: `{1..10..2}` -> `1 3 5 7 9`


#### Shell variables

- Similar to local variables - set for current shell, don't propagate to child processes
- Conventionally lower case (`$file`, `$dir`, `$x`, etc.)
- List with `set` command (depending on shell/mode, will print environment variables as well)
- Delete with `unset` command
```sh
$ fi="the best"
$ echo "flatiron is... $fi"
flatiron is... the best
$ sh
sh-4.2$ echo "flatiron is... $fi"
flatiron is...
```


   - make it executable (by adding `#!/bin/bash` and doing `chmod +x myscript.sh`) and run `./myscript.sh`


#### Modules

- Manages environment by setting and modifying environment variables for you
- `module avail` to see all available modules
  - search: `module avail -t | grep <pattern>`
- `module load <modulename>` to load module
- `module unload <modulename>` to unload module
- `module purge` to unload all modules
- `module show <modulename>` to show what loading the module does


#### Python (conda and venv/virtualenv)

- Two main ways to manage multiple python environments
- conda is a powerful, but heavier, one-stop-shop solution
  - Must be user installed, though install is straight forward (__please__ use our docs for installing conda)
- venv is lighter weight and is handled natively by python modules, but is more difficult for some packages


#### Conda

```sh
    conda create -n myenvname # places inside conda
    conda activate myenvname
    conda install numpy
    conda deactivate
```

- Pros:
  - Cross-platform installs of non-python packages
  - Handles complex packages well (e.g. tensorflow)
  - Multiple environments in a central repository
- Cons:
  - Libraries can sometimes conflict: `shadowing`
  - Uses a __lot__ of files. Can hit filecount quota
  - [Un]installing packages (transactions) slow


#### venv (virtualenv)

```sh
    python3 -m venv myenvname # places in cwd
    source myenvname/bin/activate
    pip install numpy
    deactivate
```

- Pros:
  - Lightweight - fast [un]installs
  - Can build on SCC-supported and maintained python installations, better support
  - More on-the-fly selecting of library/python
- Cons:
  - Restricted to use existing python binaries
  - Some issues with compiled packages
  - (Almost) no non-python packages (vim, emacs, etc.)


#### Manual sourcing

- Often useful to lump environment control commands into a single file
- I often create an environment file in a project root

```sh
$ cat setenv.sh
module purge
module load gcc python3 intel/compiler/2020 --force
module load pvfmm/1e4bef5 home/stkfmm/59951f4 openmpi2/2.1.6-intel-hfi intel/mkl/2020
source $HOME/projects/codes/fiber-private/env/bin/activate
$ source setenv.sh
```


### Shell features

- Builtins
- Quoting and Word Splitting
- I/O Redirection
- Command and Process Substitution
- Globs
- Common programs that aren't builtins


#### Builtins

- Q: What is a builtin?
- A: A builtin is a command you run that is part of the shell itself and not a separate executable
- Q: Why does this matter?
- A: These commands are accessible no matter what and are not dependent on other processes or variables (e.g., `PATH`)


##### More About Builtins

- There are over 70 builtin commands in bash (even more in zsh)
- Find them all by using the `help` command at your prompt (for zsh `man zshbuiltins`)
- Now, we will focus on a handful that are important to your interactive session


##### Today's Builtins

- `export`, `source` and `.` (see above)
- `alias` and `command`
- `bg`, `fg`, `jobs`, `kill`, and *^C*
- `suspend` and *^Z*
- `cd`, `pwd`, `pushd`, `popd`, and `dirs`
- `help`
- `history` and `fc`
- `echo`


- `alias`: create or display a shortcut
   - with no arguments `alias` displays a list of all aliases
   - with a single word argument alias displays the definition of the alias to which the argument refers
   - with the argument `NAME=VALUE`, creates or updates the alias named *NAME* with the value of *VALUE*
- `command`: use the actual command or builtin, even if there is an alias making it something else
   - useful when you have an alias configued to run a command with a common set of flags
   - prefixing with `\` has a similar effect


- `bg`
   - puts the most recently suspended process in the background
- `fg`
   - brings the first process in the jobs list into the foreground
- `jobs`
   - displays the status of jobs and their ID
   - `-p` flag also gives the PID for the relevant process
   - common statuses are running, suspended, killed


- `kill`: terminates the process specified by either a PID or a job number
   - `-HUP`: "Good afternoon process, please consider stopping or maybe re-reading your configuration file"
   - `-TERM` (default): "hey process, just die."
   - `-KILL`: "DIE DIE DIE STUPID PROCESS!!!"
   - *^C* is equivalent to `-INT`: "please stop"


- *^Z*
   - suspend the process currently running in the foreground of your shell (`kill -TSTP`)
- `suspend`
   - suspend the execution of your shell (because *^Z* doesn't work for shells)


- `cd`
   - change into another directory
   - `cd -` puts you into the last directory you were in
   - `cd` with no arguments puts you back to your home directory
   - `cd A B` substitutes *A* for *B* in your path (zsh only)
- `pwd`
   - prints the name of the current working directory (also `$PWD`)


- `pushd`
   - change into a directory and place it onto the top of a stack
- `popd`
   - removes a directory from the top of the stack and changes into the new top of the stack
- `dirs`
   - shows the contents of the stack generated by `pushd`


- `echo`
   - just print its arguments
   - also a non-builtin, in some shells

- `help`
   - with no arguments lists all shell builtins with very basic descriptions
   - with a single argument of a shell builtin, displays usage instructions on using the builtin


- `history`
   - display or manipulate the history of commands you have run
   - usually you just run it without arguments to remember something you did before
- `fc`
   - opens the last command in the editor, re-runs edited result
   - can also search history and do many other things (zsh)


#### Quoting and Word Splitting

- spaces matter: for most things they define the boundaries of strings
- `"` vs `'`
  - `"` does variable expansion
  - `'` does not
- automatic string concatenation (nested quotes and such)
  - if you have consecutive quoted things
- `\`
  - escapes things like spaces or special characters


#### I/O Redirection

- `>` and `>>`
   - `>` writes output from a process to the file named after the greater than symbol. if the file already exists, it is overwritten.
   - `>>` appends output from a process to the file name after the double greater than. if the file does not exist, it is created.
   - `set -o noclobber` keeps you from overwriting files with `>`


##### stdin, stdout, stderr

- stdin (`0`) is a stream of information you send to a process
- stdout (`1`) is usually the expected output of a process
- stderr (`2`) is either related to something going wrong or sort of control/status information depending on the process
- what does this mean?  `2>&1`
   - this redirects standard error to standard output


- `|`
   - take the stdout from one process and send it to the stdin of another. very useful
- `<( CMD )` (and `>( CMD )`)
   - output from *CMD* is passed as if in a real file
   - multiple processes can write to the hidden file
   - the program that wants to read the data only needs to be able to open a file


#### Command and Process Substitution

- <code>\`CMD\`</code> or `$( CMD )`
   - this is replaced with the output of the command


#### Globs

Globs match things (but are less awesome than regular expressions)
- `*`: 0 or more any characters
- `?`: precisely any one character
- `[somelistofcharspickone]` precisely one character from the list in the brackets (case matters)
- if a glob doesn't match anything, then the glob stays as is (this can be confusing)
- (zsh) if you press tab to complete, it will expand the glob in-place


#### Not Builtins But Still Great

- `ls`
   - lists the files in a directory. if no directory is specified, lists the current directory
   - usually aliased with some options to make for easier color/formatting (and slower!)


- `man`
   - instructions on how to use a command
   - `man -k` / `apropos` is a keyword search of man pages (this is life changing)
   - if you try to use `man` on a builtin, you might get a generic or bash man page.


- `sed`, `awk`, `cut`
   - `sed` is used to selectively edit streams of text (usually replacement or transformation of one or more characters)
   - `awk` is used to carve up text based around some field separators
   - `cut` selects single columns
   - effective for formatting output from a command to be piped to another command


- `nano`
   - basic editor. open. (^R) save. (^O) quit. (^X)


- `rename`
   - rename multiple files based on a supplied expression
   - usually 3 arguments: starting format, ending format, and the things you want to change
      - `rename foo foo00 foo?`
      - the takes the files foo1 -> foo5 and makes them foo001 -> foo005


- `sleep`
   - wait for some number of seconds (or other unit) based on a single argument


- `less` (is `more`)
   - paginates output, so we can read it before it scrolls past
- `cat`
   - does not
