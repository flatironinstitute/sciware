# VSCode - Remote-Containers extension

*Note* - don't let the "Remote" in the name of the extension confuse you. This extension is primarily used on your local machine.

This vscode extension allows you to:

* Create an isolated development environment
* Specify the operating system and exact dependencies needed to develop your project using a Dockerfile recipe
* Open your project in a vscode session that is running inside a docker container on your local machine
* Share your exact development environment with colaborators (even if they are on a different OS)

## Preliminary notes

Using devcontainer requires a **learning curve**. However, if you are up for it, it will be rewarding in the following ways:

* You will learn about Docker (can be used to create singularity containers to run on our cluster)
* Different projects can use different environments (greater level of isolation than conda or virtualenv)
* You can share your exact development environment with collaborators - without requiring complex installation steps
* If your code works today, it should also work next year
* Unit testing will be more reliable
* You can bundle the vscode extensions and other dev tools (linters, debuggers, etc) into your dev environment

**It's about bundling a development environment with your project and making it accessible to others and to your future self.**

## Getting started

### Step 1: Install the extension

[![Install Remote-Containers extension](https://img.youtube.com/vi/-oXFn7tvG5Y/0.jpg)](https://www.youtube.com/embed/-oXFn7tvG5Y)

### Step 2: Open your project in vscode

Your project should have a `.devcontainer` directory at the root (see below for more info).

On linux you can just do this:

```
cd /path/to/project
code .
```

### Step 3: Reopen the project in the dev container

* Use the green button in the lower-left part of the window
* Click "Remote-Containers: Reopen in container"
* Your docker image will automatically build (if needed)
* Your project will reopen inside the dev container.

### Example

Here's an example repo you can try: `https://github.com/ahbarnett/floatingspeed`

It benchmarks numerical performance, comparing languages, compilers and flags.


If you look at the `.devcontainer/Dockerfile` you will see that the particular versions of the following are installed in the container:

* Fortran (gfortran-7 and gfortran-9)
* Julia
* C++
* Octave
* Python

Normally, it would be challenging to get these all installed appropriately on one system.

[![Example: floatingspeed](https://img.youtube.com/vi/YK8kU3o15uM/0.jpg)](https://www.youtube.com/embed/YK8kU3o15uM)

### Tasks

VSCode tasks work really well with dev containers.

* Configure custom tasks in the `.vscode/tasks.json` file in your project
* These are services or operations that can be run within the development container.
* For example:
    - Start a Jupyter notebook server
    - Run unit tests
    - Run benchmarking
    - Run a database server (for testing)

### Other examples

I put some other examples in this repo:

* [example_latex](./example_latex) - Everything you need to compile and view LaTeX
* [example_jupyterlab](./example_jupyterlab) - Host a JupyterLab server in the dev container

### Mounting directories

* Use an environment variable to specify a data directory (outside the container)
* Make that data directory available at a fixed location inside the dev container
* This can be `.devcontainer/devcontainer.json`

### Exposing ports

This can be done inside `.devcontainer/devcontainer.json`

### Installing vscode extensions

This can be done inside `.devcontainer/devcontainer.json`

## Author of this guide

Jeremy Magland