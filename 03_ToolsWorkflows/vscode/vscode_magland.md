# Review of Visual Studio Code (VS Code)

## Sciware: Tools and Workflow Show and Tell

Date: July 18, 2019

Presenter: Jeremy Magland

## What I used prior to switching to VS Code

I have always preferred simple text editors rather than IDEs that take control of projects, add a lot of configuration or project files, or restrict how files may be organized. I settled on Sublime Text 3 for a while. James Jun mentioned VS Code and encouraged me to try it. I didn't try it for quite a while because I associated it with *Microsoft Visual Studio*, which I used back in the day for C++ (VS Code is actually a completely different product). Then toward the beginning the year I gave it a go and haven't turned back

## Key advantages for me

* Lightweight -- Primarily a source code editor, not a complete IDE
* Choose from many powerful, yet lightweight extensions
* Designed for software developers (maximizes efficiency)
* Does not litter file system with a lot of extra files (can easily use in conjunction with other tools)
* Supports Python, JavaScript, and many other languages

## How popular is VS Code among developers?

According to Wikipedia

**Stack Overflow 2016 survey**: 7.2% of respondents using it (ranked #13 among popular development tools)

**Stack Overflow 2019 survey**: 50.7% of respondents using it (ranked #1 among popular development tools)

**PYPL index**: VS Code is [ranked #6](https://pypl.github.io/IDE.html) among IDEs, but it is trending up, whereas 4 of the top 5 are trending down (Android Studio is trending up, but that's because people are moving toward mobile devices).

Only introduced in 2015 by Microsoft, it has grown substantially in popularity in a short time frame.

## Installation

There are various methods (see https://code.visualstudio.com/)

## How I open a project

Note: I use Linux, but VS Code is also available on Mac and Windows (startup may be slightly different)

A project is simply a directory on the file system (no extra files needed).

Open a terminal (I use yakuake which drops down from above when pressing F9), change to the project directory and open VS Code:

```
cd /path/to/my/project
code .
```

Open the integrated terminal within VS Code:

```
Ctrl+Shift+`
```

Now I have two terminals: one inside the IDE and one outside the IDE (in my yakuake terminal). This gives multiple views of the same project. The yakuake terminal gives me more space and flexibility whereas the integrated terminal is convenient in other ways (it's integrated!).

The file explorer is on the left, the main editor workspace is on the right, and the terminal is at the bottom.

Just start editing files and using the terminal!

## Extensions

VS Code has many wonderful extensions. You can search the extensions marketplace by clicking the appropriate icon on the left. Each extension has a description and popularity metrics, including number of users and number of stars. This is extremely helpful.

Extensions are very lightweight (programmed in typescript) so they download quickly and typically do not slow down the IDE.

## Some of the extensions I use

| Name          | Num. downloads | Num. stars   |
| ------------- | -------------- | ----------   |
| Python        | 55 million     | 4.5          |
| GitLens       | 23 million     | 5            |
| LatexWorkshop |  3 million     | 5            |
| Markdown Preview Github Styling |  276 thousand | 4.5 |
| autoDocstring | 131 thousand   | 5            |
| Pyright       | 68 thousand    | 5            |

## Python

I use the terminal to run all Python programs. Thus I use VS Code just as an editor, and do everything else in the terminal.

The basics are provided by the official Python extension:

* Syntax highlighting and checking
* Auto-completion
* Code navigation
* Linting (configurable)
* Debugging (I don't use this)
* Manage virtual environments, conda environments
* Auto formating (Ctrl+Shift+I) -- configurable

In the past I used integrated notebooks capabilities, but now I use JupyterLab separately

## GitLens

This extension provides a very tight integration of many aspects of the IDE with git.

* Click a line of code and see when, why, and by whom it was changed.
* Use the git view on the left to see which files have been modified, staged, deleted, etc, and visually perform basic git operations (add, commit, push, pull)
* See side-by-side, editable comparisons of what has been modified since the last commit.
* Other powerful capabilities -- file history view, line history view, comparison between branches/commits, search commits

Try `Ctrl+Shift+P` and type `GitLens` to see the many available commands and views.

## Markdown previews

Split-screen editing of markdown files with preview (github style).

## Project search -- lightweight and pleasant

Search for text in files of given type and get list of results. 

Very efficient interactive find/replace interface.

## Pyright and static typing

Static type checker for Python -- officially supported by Microsoft.

As of Python 3.6, there is a nice syntax for static typing.

Pyright will show you type errors before you run the code.

Highly recommended: add static typing to your Python code and use this extension!

Note: you don't need to update your entire code base -- static typing pieces at a time is fine.

## I use VS Code to edit all kinds of text files

Lightweight and unobtrusive!

.tex, .md, .rst, .html, .css, .js, .py, .sh, .m, .txt, .json, Dockerfile, .yml, etc.

## Some useful key shortcuts

* Open a new terminal (`Ctrl+Shift+[backtic]`)
* Search for a command (includes extensions) (`Ctrl+Shift+P`) -- super useful
* Toggle side panel (`Ctrl+B`)
* Search in project files (`Ctrl+Shift+F`)
* Search and replace in project files (`Ctrl+Shift+H`)
* Zen mode, which I only started using today (`Ctrl+K Z`, `Esc Esc` to exit)
* Many more