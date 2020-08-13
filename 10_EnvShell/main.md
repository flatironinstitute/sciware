# Sciware

## Shells and Environments

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/10_EnvShell


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

- If comfortable, please keep video on so we can all see each other's faces.
- Ok to break in for quick, clarifying questions.
- Use Raise Hand feature for new topics or for more in-depth questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording, posted on #sciware Slack


## Feedback

- Future sessions planned:
  - github with Software Carpentry Sep 25-26 (2 day session!)
  - Designing APIs and software library interfaces
  - Data storage file formats (hdf5, numpy, parquet, sqlite, ...)
- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

- Environment variables
  - Introduction
  - Specific variables
  - Control
- Shells
  - Comparison
  - Features


## Defining terms

One often hears these terms used interchangably. Let's clairfy.

* Kernel * Shell * Terminal * Command Line * Console


### Kernel & Operating System

_Kernel_ is the bridge between application software and hardware.

_Operating System_ is comprised of a kernel + other applications.

<small>_Linux_ 🐧 can refer to a kernel or an OS built on that kernel.</small>


### Shell

A _Shell_ is a program that takes commands, gives them to the operating system to perform, and returns output. As opposed to a _graphical user interface_ (GUI), the shell is a _command line interface_ (CLI).

<small>Remember: The shell interface surrounds the kernel just as a nutshell surrounds a nut 🥜.</small>


### Common Shells

On most Linux systems `bash` (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, `sh`, written by Steve Bourne) acts as the shell program.

Besides bash, other shell programs include: `fish`, `ksh`, `tcsh`, and `zsh`.

<small>Note: As of macOS Catalina (Nov 19), `zsh` is now the default Mac shell.</small>


### Terminal

_Terminal_ is a program that runs and provides i/o to a shell (or other program).

Originally a physical device, now we run software terminal emulators.

Many different terminal emulators (Gnome-Terminal, iTerm, Terminator, xterm), but they all do the same thing - give you access to a shell session.

Opinions?


### Console

Console originally referred to the physical text entry and display device for system administration messages.

Now often used specifically in context of sys admin messages from BIOS, kernel, and the system logger, or the text mode of the OS (Alt-F1 in Linux).

```javascript
  console.log("👋 hello, you are in a web browser.");
```


### Bash Startup Process

The bash shell program uses a collection of startup files to help create an environment. Each file has a specific use and may affect login and interactive environments differently.

The files in the /etc directory generally provide global settings. If an equivalent file exists in your home directory it may override the global settings.


### Bash Startup

<img src="img/shell-chart.svg" width="1000" style="border:0;box-shadow:none">


## Environment variables

<small>Jump to Nick's slides</small>



### Environment control (Robert)


#### Shell variables

- Similar to local variables - set for current shell, don't persist in child processes
- Conventionally lower case ($history, $path, $aliases, etc.)
- Can list via a bare `set` command (depending on shell/mode, will print environment variables as well)
- Can delete with `unset var` command
```sh
$ fi="the best"
$ echo "flatiron is... $fi"
flatiron is... the best
$ sh
sh-4.2$ echo "flatiron is... $fi"
flatiron is...
```


#### Environment variables

- Persist through to child processes
- Conventionally upper case ($PATH, $HOME, etc.)
- Can list via a bare `export` or `/usr/bin/env` command
- Set with `export` command
- Can delete with `unset` command
- Set only for a child process by prepending
```sh
$ MY_ENV_VAR="Environment fun!" echo "Woo! $MY_ENV_VAR"
Woo! Environment fun!
$ echo "Woo! $MY_ENV_VAR"
Woo!
$ export FI="the GOAT"
$ echo "flatiron is... $FI"
flatiron is... the GOAT
$ sh
sh-4.2$ echo "flatiron is... $FI"
flatiron is... the GOAT
```


#### Variable expansion

- `foo=bar`, `file=mydata.csv`
- Concatenate: `${foo}stool` -> `barstool`
- Remove prefix: `${file##*.}` -> `csv`
- Remove suffix: `${file%%.*}` -> `mydata`
- Substitute prefix: `${file/#*./data.}` -> `data.csv`
- Substitute suffix: `${file/%.*/.bin}` -> `mydata.bin`
- Brace expansion: `{1..10..2}` -> `1 3 5 7 9`


#### Executing shell scripts: `source`, `.`, and `chmod +x`

- `source myscript.sh` and `. myscript.sh` will _generally_ execute the script in the current shell
   - all variables set in the file will persist in your shell after execution is complete
   - `source` and `.` are handled differently in different shells, depending on the mode, but are largely identical for most purposes
- Making a script executable via `chmod` and executing via `./myscript.sh` will execute the script in a child process, and the variables will **not** persist into your current shell


#### Startup files

- certain "dotfiles" or "rcfiles" are `source`d during shell startup (more later)
- can easily break your shell, prevent logins (ex: `exit`)
- Avoid generating output in non-login files, issues with `scp`:

```
if [[ -z $PS1 ]] ; then
	return
fi
```


### Environment Management


#### Modules

- Manages environment by setting and modifying environment variables for you
- `module avail` to available modules -- useful to `module avail -t | grep <pattern>` to search
- `module load <modulename>` to load module
- `module unload <modulename>` to unload module, and `module purge` to unload all modules
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
    conda deactivate
```

- Pros:
  - Can install non-python packages, even cross-platform
  - Useful for difficult to install packages (e.g. tensorflow)
  - Multiple environments in a central repository
- Cons:
  - Libraries can sometimes conflict: `shadowing`
  - Uses a __lot__ of files. Can hit filecount quota
  - [Un]installing packages (transactions) can be quite slow


#### venv (virtualenv)

```sh
    python3 -m venv myenvname # places in cwd
    source myenvname/bin/activate
    deactivate
```

- Pros:
  - Lightweight - fast [un]installs
  - Typically easier for SCC to support
  - More on-the-fly control on which library/python to use
- Cons:
  - Restricted to use existing python binaries
  - Some issues with compiled packages
  - (Almost) no non-python packages (vim, emacs, etc)


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



## Shells

### Comparison (Dylan)


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
     - <small>emacs mode, vi mode, custom bindings in `.inputrc`</small>
- zsh added sophisticated tab-completion, prompts
     - <small>`git diff <tab>`, `rsync host:<tab>`, `gcc -<tab>`</small>
     - more permissive license, adopted by Apple

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
  - oh my zsh (plugins, themes)
- opinions?


#### Dotfiles

<table>
<thead><tr><th>shell</th><th>login</th><th>interactive</th><th>neither</th></tr></thead>
<tbody>
<tr><td rowspan='2'>bash</td><td><code>.bash_profile</code> | <code>.bash_login</code> | <code>.profile</code></td><td><code>.bashrc</code></td><td>-</td></tr>
<tr>   <td><code>.bash_logout</code></td><td>-</td><td>-</td></tr>
<tr><td rowspan='2'>tcsh</td><td colspan='3' style="text-align: center;"><code>.tcshrc</code> | <code>.cshrc</code></td></tr>
<tr>   <td><code>.login</code>, <code>.logout</code></td><td>-</td><td>-</td></tr>
<tr><td rowspan='4'>zsh</td><td colspan='3' style="text-align: center;"><code>.zshenv</code></td></tr>
<tr>   <td><code>.zprofile</code></td><td>-</td><td>-</td></tr>
<tr>   <td colspan='2' style="text-align: center;"><code>.zshrc</code></td><td>-</td></tr>
<tr>   <td><code>.zlogin</code>, <code>.zlogout</code></td><td>-</td><td>-</td></tr>
</tbody>
</table>


#### Changing your shell

- Current shell: `$SHELL`, `ps`
- Most systems: `chsh`
- FI: email scicomp@flatironinstitute.org
- caveat: some things only work out of the box in bash (modules, source)
- alternative: exec different shell from `.bash_profile`

```sh
if [[ $- == *i* && -x /bin/zsh ]] ; then
	SHELL=/bin/zsh exec /bin/zsh -l
fi
```



### Configuring your prompt 🎨



### Shell Features (Jonathan)

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


- `sed`, `awk`
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



### Other things!

* tab completion, expansion
* command line editing
* shell scripting
* slurm
* jupyter kernels
* fzf
