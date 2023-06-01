# Sciware

## Tools to make programming easier
### Intro to code editors and debugging

https://sciware.flatironinstitute.org/27_SummerIntro


## Sciware goal

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, *technology choices*\*, and scientific disciplines.

<small>\*though sometimes we try to expand your options</small>


## Summer Intros

- May 31 2-4: command line & cluster
- Jun 7 2-4 in 162-2 IDA: git & Github, Part I
- Jun 14 2-4 in 162-2 IDA: git & Github, Part II
- today **1-3** in 162-2 IDA: VS Code


## Today's agenda

- Introduction
- Examples and demos of features
- Help with setting up your own environment



## How can you code faster?

What do you spend time doing (other than thinking about logic)?
Translating ideas into code:
- is this the right syntax?
- what was that function called? what are the arguments?
- what is in this variable?
- does it compile? does it run?
- trial-and-error, looking at documentation
- repetitive editing tasks
- saving and switching files


# What is an IDE?

### Integrated Development Environment
#### (or just "editor")

- an interactive environment (tool or program)
- for developing (writing, editing) code
- that integrates other features
- designed to make it easier to write code all in one place


## Text editor

- Most IDEs are, at the core, a text editor
- Fancy "spell checker" (variables, functions, syntax), autocomplete
- Aware of code structure, projects, programming language, libraries
- Integrated tools for running, compiling, testing, debugging, checking, documenting, sharing, ...
- No need to switch to terminal to run/build, web browser to look up documentation, ...


### Old school options (evolved text-editors)

- emacs: old UNIX editor, CTRL-heavy (`C-x C-c`), many optional extensions, fully functional programming environment (1976)
- vim: based on vi (*v*i *im*proved), old UNIX editor, heavy on single-key short cuts ("modal"), many optional extensions with IDE functionality (1991)
- Notepad++: in the tradition of Notepad, open-source Windows editor (2003)


## Learning curves

<img src="https://webdeveloperankitakulkarni.files.wordpress.com/2013/11/curves.jpg">


### Newer options

- Sublime Text: proprietary editor with fancy navigation, focused on MacOS (2008)
- PyCharm, Spyder: python-specific IDEs with focus on debugging (2010)
- Visual Studio Code ("vscode"): open-source cross-platform editor from Microsoft (2015)
   - not to be confused with MS Visual Studio, an older Windows IDE (1997)


### Notebooks

- JupyterLab
   - Notebooks..
   - Editor


## Today

- You'll see examples of a number of features
- Get a sense of what's possible
- No need to follow along on your own, live
- Slides can be used as reference to come back and try later
- Most features exist in many other editors (sometimes with plugins, extensions)



# Basic functionality

## Jeremy Magland & Jeff Soules (CCM)

https://github.com/jsoules/vs-code-introduction 



# Workspaces, integrated execution and debugging

## David Silva Sanchez (CCM)


# Workspaces

Workspaces are a quality of life feature of vscode that let you:

- Save which folders you are using.
- Configure settings that only apply to said folders.
- Set tasks (compiling/running) and debugging configurations.
- Store and restore UI state associated with that workspace (opened files, tab order, ...)
- Enable or disable extensions only for that workspace.


## Creating a workspace

### Open the folder(s) you will use
<img height=80% width=80% src="./assets/gifs/open_folder.gif">


## Save workspace
<img height=80% width=80% src="./assets/gifs/save_workspace.gif">


## Load workspace
<img height=80% width=80% src="./assets/gifs/open_workspace.gif">



# Integrated execution

Execute python codes without a terminal!


## Select your python interpreter

Press Ctrl+Shift+p and look for "python: Select interpreter"
<img height=80% width=80% src="./assets/gifs/select_interpreter.gif">


## Run your code!

Press Ctrl+F5 or press the green arrow
<img height=80% width=80% src="./assets/gifs/integrated_execution.gif">



# Compile and Debug c++ code


## Create a task file

### It tells VSCode how to compile your code
<img height=80% width=80% src="./assets/gifs/create_task.gif">


## Compiling the code

After you create the task file just press Ctrl+Shift+B!


## Examples

### Compiling with g++

```yml
{
 "version": "2.0.0",
 "tasks": [
  {
   "type": "cppbuild",
   "label": "Build .cpp file", //Remember this label!
   "command": "/usr/bin/g++", //Compiler
   "args": [
    "-g",
    "${workspaceFolder}/simple_addition.cpp",
    "-o",
    "${workspaceFolder}/simple_addition.out"
   ],
   "options": {
    "cwd": "${fileDirname}"
   },
   "problemMatcher": [
    "$gcc"
   ],
   "group": {
    "kind": "build",
    "isDefault": true
   },
   "detail": "compiler: /usr/bin/g++"
	 }
 ]
}
```


## Compiling with make

```yml
{
 "version": "2.0.0",
 "tasks": [
  {
   "type": "shell",
   "label": "Build .cpp file", //Remember this name!
   "command": "make",
   "group": {
    "kind": "build",
    "isDefault": true
   }
  }
 ]
}
```


## Create a launch file

### Defines how the debugging goes

<img height=80% width=80% src="./assets/gifs/create_launch.gif">


## Starting a debugging session

Press F5 for starting the session
<img height=80% width=80% src="./assets/vscode_debugging.png">


## Examples

### For c++

```yml
{
 "version": "0.2.0",
 "configurations": [        
   {
    "name": "(gdb) g++ buld and debug",
    "type": "cppdbg",
    "request": "launch",
    "program": "${workspaceFolder}/simple_addition.out",
    "args": [],
    "stopAtEntry": false,
    "cwd": "${workspaceFolder}",
    "environment": [],
    "externalConsole": false,
    "MIMode": "gdb",
    "setupCommands": [
     {
      "description": "Enable pretty-printing for gdb",
      "text": "-enable-pretty-printing",
      "ignoreFailures": true
     }
    ],
    "preLaunchTask": "Build .cpp file"
   }
 ]
}
```


## For python

```yml
{
 "version": "0.2.0",
 "configurations": [
  {
   "name": "Python: Specific file",
   "type": "python",
   "request": "launch",
   "program": "${workspaceFolder}/simple_addition.py",
   "console": "integratedTerminal"
  }
 ]
}
```


## Debugging options

### Breakpoints
<img height=80% width=80% src="./assets/gifs/create_breakpoint.gif">


## Types of breakpoints

- Normal breakpoints: "Breaks" the execution of the code when it is hit.
- Conditional breakpoints:
    - Expression condition: The breakpoint will "break" execution whenever the expression evaluates to True
    - Hit count: "Breaks" execution only if it has been hit a particular number of times
- Inline breakpoints: Only are hit when the execution reaches a specific line and column.


## Debugging Actions

- Continue/Pause (F5)
- Step Over (F10)
- Step Into (F11)
- Restart (Ctrl+Shift+F5)
- Stop (Shift+F5)


## Step Over
<img height=80% width=80% src="./assets/gifs/step_over.gif">


## Step Into
<img height=80% width=80% src="./assets/gifs/step_into.gif">


## Step Out
<img height=80% width=80% src="./assets/gifs/step_out.gif">


## Watch Variables
<img height=80% width=80% src="./assets/gifs/watch_variables.gif">



# Customization

### Adam Lamson (CCB)

<img height="60%" src="./assets/borrow_your_laptop.png">


## Links and resources

- Things to get you comfortable with editing `settings.json`: 
  - [VS Code settings you should customize](https://dev.to/thegeoffstevens/vs-code-settings-you-should-customize-5e75)
- Tips and tricks with some customization examples
  - [Short tips and tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
  - [Official MS VS code tips and tricks](https://github.com/Microsoft/vscode-tips-and-tricks)
- Collected extensions with examples
  - [Awesome VS code](https://github.com/viatsko/awesome-vscode)


## Finding, adding, and editing shortcuts

- Most shortcuts begin with `cmd`, `alt`, or `ctrl` depending on system.
- Shortcut for editing your shortcuts: 
  - (Mac) `cmd + K cmd + S`
  - (Windows/Linux) `ctrl + K ctrl + S`
- If you find yourself using one task a lot. Find or make a shortcut for it!
  - Tip: Don't be clever. Use the combination that first comes to mind.
- Cheatsheets: [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf), [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), [Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)


## JSON keybinding and settings file

### Why
- Often easier to edit file directly instead of using UI
- Easily copy settings other people recommend
- Transfer settings over to other machines

### How


## Some useful shortcuts to add to
- Move through open tabs quickly
```
    {
        "key": "ctrl+n",
        "command": "workbench.action.nextEditor",
    },
    {
        "key": "ctrl+p",
        "command": "workbench.action.previousEditor",
    },
```


- Quick file search
```
    {
        "key": "cmd+p",
        "command": "workbench.action.quickOpen"
    },
```


- Open and edit keybindings and settings 
```
   {
        "key": "cmd+;",
        "command": "workbench.action.openGlobalKeybindings"
    },
    {
        "key": "cmd+.",
        "command": "workbench.action.openSettingsJson"
    },
```


## Other things to play around with
### Color theme
- Access with `cmd + k cmd + t`
- Plenty of themes in extensions

### Other editor keymaps
- Vim, Emacs, Sublime, etc.



# Survey

https://bit.ly/TBD

# Questions & Help
