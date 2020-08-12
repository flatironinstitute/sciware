# Sciware

## Shells and Environments

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/10_EnvShell


## Rules of Engagement

### Goal:

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, _technology choices_\*, and scientific disciplines.

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



## Basic terms

One often hears the following used interchangeably. Let's clarify.

    - Kernel
    - Shell
    - Command Line
    - Console


### Kernel & Operating System

- Kernel: the bridge between application software and hardware.
- Operating System: comprised of a kernel + other applications.
- Linux can refer to a kernel or an OS built on that kernel.


### Shell

- Name origin: Shell interface 🐚 surrounds the kernel just as a nutshell surrounds a nut 🥜.
- Shell is a program that takes commands, gives them to the operating system to perform, and returns output.
- In the old days, it was the _only_ user interface. Nowadays, we have graphical user interfaces (GUIs) in addition to command line interfaces (CLIs) such as the shell.


### Shell Examples

- On most Linux systems `bash` (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, `sh`, written by Steve Bourne) acts as the shell program.
- Besides bash, other shell programs include: `fish`, `ksh`, `tcsh`, and `zsh`.
- Note: As of macOS Catalina (Nov 19), `zsh` is now the default Mac shell.


### Terminal

- Terminal is a program that runs and provides I/O to a shell (or other program).
- Originally a physical device, now we run software terminal emulators.
- Many different terminal emulators (Gnome-Terminal, iTerm, Terminator, xterm), but they all do the same thing - give you access to a shell session.
- Opinions?


### Console

- Console originally referred to the physical text entry and display device for system administration messages.
- Now often used specifically in context of sys admin messages from BIOS, kernel, and the system logger, or the text mode of the OS (Alt-F1 in Linux).
- ```javascript
  console.log("👋from your web browser.");
  ```


### Bash Startup Process

The bash shell program uses a collection of startup files to help create an environment. Each file has a specific use and may affect login and interactive environments differently. The files in the /etc directory generally provide global settings. If an equivalent file exists in your home directory it may override the global settings.


### Bash Startup



## Environment variables

<small>Jump to Nick's slides</small>



### Environment control (Robert)



## Shells

### Comparison (Dylan)


#### History

<img src="img/evolve.svg" width="1000" style="border:0;box-shadow:none">

- run commands, interactive
- slowly developed more scripting features
- control structure syntax: ALGOL (`fi`, `esac`), C (`{}`), *other*...


#### Evolution

- ksh introduced functions
- tcsh invented history, alias, other interactive features
- bash developed (and spun off) readline, key bindings
- zsh added sophisticated tab-completion, prompts
- POSIX.2 standardized minimal shell features (see `dash`)

most modern shells copied, adopted similar, popular features


#### Startup files

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


#### Preferences

- bash
  - most common shell, especially for scripting
  - often assumed default
  - lags behind, catches up
- tcsh: fallen out of favor, non-POSIX, still maintained
- zsh
  - large, superset of **compatible with bash** and tcsh
  - many interactive features, tab completion
     - <small>`git diff <tab>`, `rsync host:<tab>`, `gcc -<tab>`</small>
  - more permissive license _(Apple)_
  - oh my zsh (plugins, themes)
- opinions?



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
- A: These commands are accessible no matter what and are not dependent on other processes or variables (e.g.: PATH)


More About Builtins

- There are over 70 builtin commands in bash (even more in zsh)
- Find them all by using the "help" command at your prompt (for zsh type "man zshbuiltins")
- Focus on a handful that are important to your interactive session


Today's Builtins

- alias and command
- bg, fg, jobs, kill and ^c
- suspend and ^z
- cd, pwd, pushd, popd, dirs
- export
- help
- history
- source and .


- alias: create or display a shortcut
  - with no arguments alias displays a list of all aliases
  - with a single word argument alias displays the definition of the alias to which the argument refers
  - with the argument NAME=VALUE, creates or updates the alias named NAME with the value of VALUE

- command: use the actual command or builtin, even if there is an alias making it something else
  - useful when you have an alias configued to runa command with a common set of flags


- jobs
  - displays the status of jobs and their ID
  - -p flag also gives the PID for the relevant process
  - common statuses are running, suspended, killed
- bg
  - puts the most recently suspended process in the background
- fg
  - brings the first process in the jobs list into the foreground


- ^c kills the current process that is running
- kill terminates the process specified by either a PID or a job number
  - -1 (SIGHUP): "Good afternoon process, please consider stopping or maybe re-reading your configuration file"
  - no flag specified (SIGTERM): "hey process, just die."
  - -9 (SIGKILL): "DIE DIE DIE STUPID PROCESS!!!"


- suspend
  - suspend the execution of your shell
- ^z
  - suspend the process currently running in the fireground of your shell


- cd
  - change into another directory
  - cd - puts you into the last directory you were in (super helpful when you change to the wrong place or when you have to go back and forth a bunch)
  - cd with no arguments puts you back to your home directory
- pwd
  - prints the name of the current working directory 


- pushd
  - change into a directory and place it onto the top of a stack
  - the -n option only adds the directory to the top of the stack but does not change directories
- popd
  - remnoves a directory from the top of the stack and changes into the new top of the stack
  - the -n option only removes the directory from the to pof the stack but does not change directories
- dirs
  - shows the contents of the stack generated by pushd
  - -c option clears the stack entirely



- export
  - makes a variable able to be inherited by subsequent commands

- help
  - with no arguments lists all shell builtins with very basic descriptions
  - with a single argument of a shall builtin, displays usage instructions on using the builtin


- history
  - display or manipulate the history of commands you have run
  - -c option clears it
  - usually you just run it without arguments to remember something you did before


- source and .
  - effectively the same thing
  - read and execute commands from a file
  - uses your PATH to find the file you specify
  - . is POSIX compliant, while source is the more readable version provided by BASH
  - source runs the file in the current shell where . runs it in a subshell


#### Quoting and Word Splitting

- spaces matter (set a variable with a space vs not)
- “ vs ‘
  - " does variable expansion
  - ' does not
- automatic string concatenation (nested quotes and such)
- \
  - escapes things like spaces


#### I/O Redirection

- > and >>
  - > writes output from a process to the file named after the greater than symbol. if the file already exists, ot is overwritten.
  - >> appends output from a process to the file name after the double greater than. if the file does not exist, it is created.
  - noclobber keeps you from overwriting files with > (set -o noclobber)
- stidin, stdout(1), stderr(2)
  - stdin is a stream of information you send to a process
  - stdout is usually the expected output of a process
  - stderr is either related to something going wrong or sort of control/status information depending on the process
  - walk through 2>&1
    - this redirects standard error to standard output 
- process redirection vs a pipe and why it’s awesome
- |
  - take the stdout from one process and send it to the stdin of another. very useful 

#### Command and Process Substitution

- ``
  - this is the equivalent to the output of the command in the backticks. often useful in loops.
- $()
  - the output of the command in the parentheses is sustituted. often useful in text strings.
	
#### Globs

- \* - 0 or more characters
- ? - precisely one character
- [somelistofcharspickone] - precisely one character from the list in the brackets (case matters)
- if a glob doesn’t match anything, then the glob is the name (this can be confusing)
- zsh globbing - if you press tab to complete, it will actually turn into the glob. (like pressing tab with a * on ls will actually expand the * to the files in your working directory)

#### Not Builtins But Still Great

- ls
  - lists the files in a directory. if no directory is specified, lists the currend directory
  - usually aliased with some options to make for easier color/formatting

- man
  - instructions on how to use a command
  - man -k / apropos is a keyword search of man pages (this is life changing)

- sed and awk
  - sed is used to selectively edit streams of text (usually replacement or transformation of one or more characters)
  - awk is used to carve up text based around some field separators
  - they are often used together
  - effective for formatting output from a command to be piped to another command

- nano
  - basic overview. open. (^r) save. (^o) quit. (^x) 

- rename
  - rename multiple files based on a supplied expression
  - usually 3 arguments starting format, ending format, and the things you want to change
    - rename foo foo00 foo?
    - the takes the files foo1 -> foo5 and makes them foo001 -> foo005

- sleep
  - wait for some number of seconds based on a single argument

- less
  - paginates output, so we can read it before it scrolls past  
	





### Extras

* tab completion, expansion
* command history, `fc`
* shell scripting
* slurm
* jupyter kernels
