# Sciware

## Command line and Shell interaction

https://sciware.flatironinstitute.org/27_SummerIntro

https://github.com/flatironinstitute/learn-sciware-dev/tree/main/27_SummerIntro


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


## Today's Agenda

- Pre-session: setup a terminal (15 min)
- Command-line intro (45 min, with terminal)
- Cluster intro (30 min)
- VS code intro, terminal (10 min)

- Homework for next time: create a github account



## Preparation Instructions
*Instructions to get your laptop set up before the session*

- Windows
   - See next slide
- Mac
  - Install xcode: open a terminal and run
     - `xcode-select --install`
  - Install VS Code: https://code.visualstudio.com/docs/setup/mac
- Linux
   - Install VS Code: https://code.visualstudio.com/docs/setup/linux


## Windows Instructions
- Follow the three steps at this link to install WSL, VS Code, and the WSL extension for VS Code: https://code.visualstudio.com/docs/remote/wsl#_installation
- Check if your installation worked: follow these instructions to open VS Code and connect to WSL: https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace
- If you see "WSL" in the bottom left of your VS Code window, your installation is working



## Definitions

* Terminal
* Shell
* Command Line
* Programs

Let's start a terminal!
- Start "Terminal" on Mac or Linux, or "wsl" on Windows


<img src="assets/desktop-terminal-shell.png" width="100%" style="border:0;box-shadow:none">


### Command Line

- "CLI" = _command line interface_
   - Compare to GUI = _graphical user interface_
- In a terminal, you run a shell
- With the shell, you run programs
- Shell may be on another (remote) computer (e.g., ssh)


### Shell Command Example

<img src="assets/command-line-example.png" width="60%" style="border:0;box-shadow:none" />

Here's a typical shell command, with three parts:

- A **prompt** provided by the shell
- A **command**, the other program I want to run
- The **options** or **flags** that control behavior, usually starting with `-`
- The **arguments**, additional words that will be passed in to the command


## Working directory

A shell or program always has a "current working directory": the directory (or folder) that's used by default
- `pwd` shows you the current directory ("print working directory")
- `cd` changes the current directory, by default to your "home" directory (`~`)

```bash
> pwd
/home/you/somewhere
> cd
> pwd
/home/you
> cd ~
> cd /home/you # same thing, for your home directory path
```


## Clone a repo

- `ls` lists the files and directories (...in a specific directory, or your current by default)

```bash
> ls
Desktop
> git clone https://github.com/flatironinstitute/sciware-command-intro
Cloning into 'sciware-command-intro'...
> ls
Desktop  sciware-command-intro
> cd sciware-command-intro
> pwd
/home/you/sciware-command-intro
```


### Looking at files

To see *inside* a file, the contents, you need something else
- `cat` just prints an entire file to the terminal
- `less` lets you scroll around (`q` to quit)
- You can also use an editor

```bash
> cat README
> less README
```


### Listing files

`ls` lists files in a directory, and has many options to show more/different information

```bash
> ls -l # long
> ls -ltr # long, sort by modification time, reversed
> ls --help # may not work on Mac
> man ls
```

### Tab completion

No one wants to type all these file names: use tab!

```bash
> cat RE<tab>
> cd ~/sciware-<tab>
```

If there are multiple things, press tab twice:

```bash
> cd di<tab><tab>
```


### Creating directories

Create a new directory with `mkdir`, remove with `rmdir`

```bash
> mkdir mydir
> cd mydir
> ls
> cd ..
> rmdir mydir
```

- `..` always refers to the "parent" directory, one above


### Quoting, spaces, arguments

What if we want to make a directory `work stuff`?

```bash
> mkdir work stuff
> ls
> rmdir work stuff
> mkdir "work stuff"
> cd work<tab>
```

- The shell always splits arguments into words before the command gets it.
- To avoid this, use quotes, or `\ `, which "escapes" any character


### More file manipulation

- `mv` renames or moves files or directories
- `rm` removes files, or `rm -r` removes directories and contents (careful!)

```bash
> cd ~/sciware-command-intro
> mv filea fileb
> mv fileb dir1
> ls dir1
> rm dir1/fileb
> rm -r dir1
```


### Hidden "dot" files

Files and directories that start with `.` don't show up by default, but you can access them as usual.

```bash
> cd dir2
> ls
> ls -a
> ls -la
> mv .hiddenfile nothidden
> ls
> cd ..
```


### Copying files

`cp` makes an identical copy of a file.

```bash
> cp README readnot
> cat readnot
> diff README readnot
```

To copy entire directories, use `cp -a`.


### Interactive programs

- Some programs are interactive, don't immediately return you to the shell.
- You can often use Control keys to stop them, written `<ctrl-c>` or often `^C`
   - `^D` tells a program you're done
   - `^C` tells a program to exit ("cancel")

```bash
> python
Python 3
>>> 1+1
2
>>> ^D
```


### History, navigation

```bash
> <up>/<down>
> history
> <left><right><home><end>
```


### Shell interaction

- `^A` = Home (beginning of line), `^E` = End (end of line)
- `^L` = clear

```bash
> exit
```


### Shells and configuration

- bash: .bashrc
- zsh: .zshrc



## VS code

Interactive demo
* look at a couple files
* correspond to command line
* terminal


## Homework

* create github account
