# Sciware

## Tools to make programming easier
### Intro to code editors and debugging

https://github.com/flatironinstitute/learn-sciware-dev/tree/main/16_EditorsVSCode


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
- We are recording. Link will be posted on #sciware Slack.


## Future Sessions

- Suggest topics and vote on options in #sciware Slack


## Today's agenda

- Introduction
- Examples and demos of features
- Help with setting up your own environment



# What is an IDE?

### Integrated Development Environment

- an interactive environment (tool or program)
- for developing (writing, editing) code
- that integrates other features
   - for running, compiling, testing, debugging, checking, documenting, sharing, ...
- designed to make it easier to write code all in one place
   - no need to switch to terminal to run/build, web browser to look up documentation, ...


## Text editor

- Most IDEs are, at the core, a text editor
- Fancy "spell checker" (variables, functions, syntax), autocomplete
- Aware of code structure, projects, programming language, libraries


## Options

### Old school (evolved text-editors)

- emacs: old UNIX editor, CTRL-heavy (`C-x C-c`), many optional extensions, fully functional programming environment (1976)
- vim: based on vi (*v*i *im*proved), old UNIX editor, heavy on single-key short cuts ("modal"), many optional extensions with IDE functionality (1991)
- Notepad++: in the tradition of Notepad, open-source Windows editor (2003)


## Learning curves

<img src="https://webdeveloperankitakulkarni.files.wordpress.com/2013/11/curves.jpg">


### Modern

- Sublime Text: proprietary editor with fancy navigation, focused on MacOS (2008)
- PyCharm, Spyder: python-specific IDEs with focus on debugging (2010)
- Atom: open-source cross-platform editor from Github, "web" (js) based, can be a bit slow (2014)
- Visual Studio Code ("vscode"): open-source cross-platform editor from Microsoft (2015)
   - not to be confused with MS Visual Studio, an older Windows IDE (1997)



## Today

- You'll see examples of a number of features
- No need to follow along on your own live
- Slides can be used as reference to come back and try later
- Most features exist in many other editors (sometimes with plugins, extensions)



# Basic functionality

## Jeremy Magland & Jeff Soules (CCM)



# Workspaces and C++

## David Silva Sanchez (CCM)



# Remote environments

## Wen Yan (CCB)


# Working on Remote Clusters

All of the cool features you've seen so far, can be used when editing _remote_ files, i.e. on a cluster!!


## How It Works

<img height=80% src="./assets/vscode_remote_setup.png">


## What You Can Do

- View, move, and reorganize directories
- Edit files
- Debug
- Static linting
- Formatting
- View figures


## Bonus: Setup

1. Get OpenSSH compatible SSH client
2. Download the [Remote SSH extension](https://code.visualstudio.com/docs/remote/ssh) for VSCode
3. Enable key-based authentication, see the [VSCode docs](https://code.visualstudio.com/docs/remote/troubleshooting#_configuring-key-based-authentication) for details
4. From the VSCode command palette search for `Remote-SSH: Connect to Host`
5. Enter your username and host info, e.g. `jasm3285@login.colorado.edu`

See the official instructions [here](https://code.visualstudio.com/docs/remote/ssh-tutorial)



# Customization

## Adam Lamson (CCB)



# Questions & Help
