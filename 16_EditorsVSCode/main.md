# Sciware

## Tools to make programming easier
### Intro to code editors and debugging

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/16_EditorsVSCode


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

Integrated Development Environment:
- an interactive environment (tool or program)
- for developing (writing, editing) code
- that integrates other features
   - for running, compiling, testing, debugging, checking, documenting, sharing, ...
- designed to make it easier to write code all in one place
   - no need to switch to terminal to run/build, web browser to look up documentation, ...


## Text editor

- Most IDEs are, at the core, a text editor
- Aware of code structure, project, programming language
- Fancy "spell checker" (variables, functions, syntax)


## Options

- vim: based on vi (Vi IMproved), old UNIX editor, heavy on single-key short cuts ("modal": edit by default), many optional extensions with IDE functionality
- emacs: old UNIX editor, CTRL-heavy, similarly many extensions
- Notepad++: in the tradition of Windows Notepad
- vscode: Visual Studio Code (not to be confused with Visual Studio, also an IDE)
- atom: from github
- sublime: proprietary editor
- PyCharm, Spyder: python-specific editors


## Learning curves

<img src="https://webdeveloperankitakulkarni.files.wordpress.com/2013/11/curves.jpg">


## Today

- You'll see examples of a number of features
- You don't need to follow along on your own live
- Slides can be used as reference to come back and try later
- Using VS Code to demo features
- Most features exist in many other editors (sometimes with plugins, extensions)



# Quick reference guides



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
