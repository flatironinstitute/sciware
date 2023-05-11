# Sciware

## Command line and Shell interaction

https://sciware.flatironinstitute.org/27_SummerIntro

https://github.com/flatironinstitute/learn-sciware-dev/tree/main/27_SummerIntro



## Preparation Instructions
*Instructions to get your laptop set up before the session*

- Windows
   - See next slide
- Mac
  - Install xcode: open a terminal and run `xcode-select --install` (10 min)
  - Install VS Code: https://code.visualstudio.com/docs/setup/mac
- Linux
   - Install VS Code: https://code.visualstudio.com/docs/setup/linux


## Windows Instructions
- Follow the three steps at this link to install WSL, VS Code, and the WSL extension for VS Code: https://code.visualstudio.com/docs/remote/wsl#_installation
- Check if your installation worked: follow these instructions to open VS Code and connect to WSL: https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace
- If you see "WSL" in the bottom left of your VS Code window, your installation is working
- If not, SciWare will be available to help you before/at the beginning of the session (TODO: is this true?)



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
- git clone https://github.com/flatironinstitute/sciware-command [create]
- Command-line intro (45 min, with terminal)
- Cluster intro (30 min)
- VS code intro, terminal (5 min)

- Homework for next time: create a github account



# Background

## Definitions

You may hear people use these terms to mean the same thing:

* Operating System
* Shell
* Terminal (console)
* Command Line


<img src="assets/desktop-terminal-shell.png" width="100%" style="border:0;box-shadow:none">


### Command Line

- "CLI" = _command line interface_
- Term for any program you control with typed commands
- Compare to GUI = _graphical user interface_
- Non-shell programs can have a CLI (e.g. `ipython`)
  - But usually "command line" means a shell


### Shell Command Example

<img src="assets/command-line-example-major.png" width="60%" style="border:0;box-shadow:none" />

Here's a typical shell command, with three parts:

- A **prompt** provided by the shell
- A **command**, the other program I want to run
- The **arguments** -- additional text that will be passed in to the command


### Interactive navigation

```
cd
pwd
ls
git clone https://github.com/flatironinstitute/sciware-command
ls
cd sciware-command
pwd
ls
cat README
less README
mv
cp
rm
mkdir
rmdir
ls -la
git --help
```

history, scroll, up, down
tab completion

```
exit
touch
python
1+1
^D
```


### Shell Command Example

<img src="assets/command-line-example-minor.png" width="60%" style="border:0;box-shadow:none" />

- **Options** customize the command's behavior
  - Also known as *flags* or *switches*
  - Often have long (`--`) and short (`-`) forms
  - Order usually doesn't matter
  - Short flags can usually be combined (`-l -a` = `-la`)


### Shell Command Example

<img src="assets/command-line-example-minor.png" width="60%" style="border:0;box-shadow:none" />

- **Positional Arguments** ("args")
  - Order *does* matter for many commands
  - Often identify files or directories to run on
  - "arguments" by itself usually means positional arguments


### Shells and configuration

- bash: .bashrc
- zsh: .zshrc



## VS code

Interactive demo
* look at a couple files
* correspond to command line
* terminal
