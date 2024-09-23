# Sciware

## Python Packaging

https://sciware.flatironinstitute.org/34_PyPackaging

https://github.com/flatironinstitute/sciware/tree/main/34_PyPackaging


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


## Future Sessions

- Oct 2 10-noon: Intro to HPC: Extended introduction to the FI cluster
- Suggest topics or contribute to content in #sciware Slack
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Today's Agenda

- What do we mean by packaging, and why do you want to do it?
- Review of the Python import system 
- Configuring your project with `pyproject.toml`
- Hands-on example of turning a Jupyter notebook into importable code



# Whats and Whys of Python Packaging

### Jeff Soules (CCM)

<img height="50%" src="assets/python-packaging.gif" class="plain">


## Outline

- Motivation
- Vocabulary
- The Import System
- `pyproject.toml` and You


## Does this sound like you?

- My script only runs from a certain directory!
- My tests can't find my code!
- I've defined the same function in three notebooks!
- To run that function in `ipython` I paste in...
- So first we edit `sys.path`...


Do you have these issues with packages you install by `pip`?

No. You `import ThePackage` and it Just Works.

Running your own code should be that simple too.


- What we'll show today helps get you ready for *distributing* your
work on a package archive like PyPI.

- But we'll leave the fine details of
that for a future Sciware about distributing code.

- For today, we just want you to be able to `import` your own code as easily
as you do someone else's.


## Defining Terms


### "Package" vs "Module" vs "Project"

The [documentation](https://docs.python.org/3/glossary.html#term-package) can
be quite confusing.

For today, we mean:

- `Project`: some collection of files that you're working on.
- `Module`: any file that has Python code.
- `Package`: a bundle of Python code you can *import*.
  - One or more files (the user doesn't need to care)
  - Downloaded from a repository or installed locally


In short:

- We'll use "**project**" to mean something you're editing, and "**package**"
to mean something you want to import.

- Our goal for today is to show how easy and beneficial it is to make your
  *projects* into (locally) importable *packages*.


### Why Have Packages?

- We've said packages are "stuff you can import."

- So the point of packages is *code reuse*.
  - They are libraries of pre-written code.

- A big part of Python's success is its robust package ecosystem!


<img src="https://imgs.xkcd.com/comics/python.png">


That comic is from *2007*. (A few things have changed!)

The ecosystem addresses 3 problems:


- How do I get useful code from other people
- How do I share my useful code with others
- How do I run the *right* code


## Five Pillars of Python Packages

- Python version management
- Environment management
- Package management
- Package building
- Package publishing


### (Installed) Version Control

- Python version management
  - = interpreter version. Python 2 is not 3.6 is not 3.12
- Package management
  - How do I install 3rd-party code?
  - `pip`, `conda`
- Environment management
  - Different tasks require different (conflicting?) packages
  - [(virtual) environments](https://docs.python.org/3/tutorial/venv.html) let them coexist
  - `venv`, `conda`


### Package distribution

- Package building
  - How do I put my code in a distributable form?
  - `setuptools`, `hatch`, `pdm`, others
- Package publishing
  - How do I share my bundled code in publicly?
  - `twine` (bundling), `PyPI` (a repository)


### Five Pillars Revisited

- Python version management <!-- .element style="color: #999999" -->
- Environment management <!-- .element style="color: #999999" -->
- **Package management**
- **Package building**
- Package publishing <!-- .element style="color: #999999" -->

Each of these offers many tools, but for today
we're really only talking about `pip`
(and maybe a little bit of [setuptools](https://setuptools.pypa.io/en/latest/)).


### namespaces

- A [namespace](https://docs.python.org/3/glossary.html#term-namespace) creates a nested 
  hierarchy of names.

- Namespaces let packages define variables, functions, and classes without worrying about uniqueness.


Example:
- `numpy.linalg.norm()` is one function
- `torch.norm()` is a different function
- Both compute norms, but they have different parameters and work on different objects
- You can use both in the same script because the
namespace (`numpy` vs `torch`) clarifies what you mean.


### global vs local namespaces

The *global namespace* is the top level for everything in the file.
```python
x = 10
print(f"{x}") # prints 10
```

*Local namespaces* nest one name inside another:
```python
class MyClass:
    y = 10  # note this is a class variable

print(f'{y}') # fails: y not defined
print(f'{MyClass.y}') # prints 10
```



## Python imports

<img height="50%" src="assets/declare-live-animals.jpg" class="plain">


### What importing does

An [import](https://docs.python.org/3/reference/import.html) does
two things:

- Finds the code you want to use, and
- Attaches that code to a name in the namespace

Let's talk about the second point first.


Example:
```python
from math import sqrt
import numpy as np

print(f'{sqrt(16)}') # prints 4
print(f'{math.pi}') # fails--we didn't import math!
my_array_1 = np.array([1, 2, 3]) # works
my_array_2 = numpy.array([1, 2, 3]) # fails!
```
- `sqrt` is attached to the *global namespace*
- its parent, `math`, is not! We didn't import that.
- The `numpy` package has been imported with an alias
  - That *alias* is visible, but the original name isn't


### Relative imports

What about this?
```python
from .mycode import function_a
from . import othercode
from .. import thirdfile as t

print(f'{function_a(1, 2)}')
print(f'{othercode.function_b(3, 4)}')
print(f'{t.fun_c()}')
```

It *might* work...
- if we are in the right directory
- if we invoked Python the right way
- if the files don't move

Why is this so brittle?


### Finding the code to import

- `import FOO` makes Python look for a *module* named `FOO`
- It looks in the list of locations defined in `sys.path`
  - This list includes various standard locations
  - It also includes your current working directory, but...
    - ...that changes with every `cd`!

Reliable imports require the code to be in one of the standard locations.
Managing that is what `pip` does.


### Package installation

- When you `pip install` a package, `pip`:
  - downloads a bundle with the package code
  - Places it in a standard location (in `sys.path`)


`pip` can also install *your project* as a package, using *edit mode:*

`$ pip install -e /path/to/my/project`

- the base directory of your project gets added to `sys.path`
- Now regular import patterns work!
- You just have to describe your project to `pip`
- which you do through `pyproject.toml`

But first...


### A bit more about environments

`sys.path` is actually how
environments work.

Let's take a look at a `venv` virtual environment and
what happens when I install packages in it.


```bash
$ which python  # none found--it's called python3
$ which python3 # /usr/bin/python3
$ python3 --version # Python 3.10.12
$ python3 -m venv ~/tmp/my-venv
$ source ~/tmp/my-venv/bin/activate
$ which python  # now returns ~/tmp/my-venv/bin/python
```


<img src="./assets/venv-demo-2.png" class="plain">

Note the paths:
- `''` gives the directory where you launched `python`
- The `/usr/lib/` directories are for preinstalled packages
- `~/tmp/my-venv/lib/python3.10/site-packages` is
  where downloaded packages will be installed


Before we install anything:

<img src="./assets/venv-demo-3.png" class="plain">

that directory has a few package-distribution tools installed,
and that's it.


Now let's install numpy!

```bash
$ pip install numpy
```

And see that `numpy` gets copied into the package directory.

<img src="./assets/venv-demo-4.png" class="plain">


What about a local package installed in editable mode?

<img src="./assets/venv-demo-5.png" class="plain">


Note we get a project descriptor, but no actual code directory.

Instead:
<img src="./assets/venv-demo-6.png" class="plain">

The project src directory gets added to `sys.path`.

This means my changes are visible live--no reinstall needed.



## Properly Handling Python Projects

<img height="50%" src="assets/wikihow-Hold-a-Snake-Step-13-Version-2.jpg" class="plain">


### Pythons Organized Neatly

To make following discussion concrete, we'll work with an example project using a standard layout.
We're calling our package `SciwarePackage`.

The code for this example is under `example_project_root` in
[this presentation repository](https://github.com/flatironinstitute/sciware/tree/main/34_PyPackaging).


<img src="./assets/sample-layout.png" class="plain">
<img src="./assets/sample-layout-shorter.png" class="plain">


The highlights:
- The root of the project is `example_project_root` (this name doesn't matter)
- Package code is in the `src` directory.
  - Specifically, in a `SciwarePackage` sub-directory
    - That name matches the package name
  - `separate_file.py` is not part of the package
- Test code is in a `test` directory
  - Also *not* part of the package
- `pyproject.toml` goes at the top level--the project root


### pyproject.toml

- The modern way to configure a project
  - Not just for packaging--it's a single-source config file
- Written in [toml](https://toml.io/en/) format, so human-readable
- Goes in the root of your project directory


Quick aside: there's a lot of old material online recommending deprecated package
configuration methods. Guides referring to `setup.cfg` are almost certainly
outdated.

`setup.py` is sometimes still required, but only very rarely--if you aren't
positive why you need it, you're probably just using outdated instructions.


### Minimal pyproject.toml for an installable package

`[project]` section:

```toml
[project]
name = "SciwarePackage"
version = "0.0.1"
requires-python = ">=3.8"
dependencies = [
    "numpy>=1.24.0",
]
```

`name` will be the name you use to import the package.

`dependencies` will be automatically installed when you `pip install` the package.


### [project] section, continued
```toml
description = "Example package for Sciware 34"
authors = [
    { name = "Jeff Soules", email = "jsoules@flatironinstitute.org" }
]
readme = "README.md"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]

[project.license]
file = "LICENSE"
```
- Not required right now but help others find your uploaded package
- `readme` can be text, a file, or even `dynamic` (see later)
- `license` describes how others can legally use your code


### Build system

You also need a `[build-system]` section:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend="setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}
packages = ["SciwarePackage"]
```

Specifies the tool that bundles your code (i.e. `setuptools`)

We have another config block for the `setuptools` tool.

(`pyproject.toml` collects most tools' config into the same file)


```toml
[tool.setuptools]
package-dir = {"" = "src"}
packages = ["SciwarePackage"]
```

This block is specific to `setuptools`. It defines:
- the root directory of the code to distribute, relative to where `pyproject.toml` is located
  - Here that's the `src` directory
- the packages that should be bundled (matches the `name` field of the `[project]` section)


That's it! With this minimal `pyproject.toml` config in place, you can install your project as a package.
If:

- the project is at `~/example_project_root`
- `~/example_project_root/pyproject.toml` is as above
- package code lives in `~/example_project_root/src/`

```bash
$ pip install -e ~/example_project_root/
```


Now, in *any* Python file *anywhere*, you can import the `SciwarePackage` package
and the code it defines.

```python
from SciwarePackage import describe_operation
from SciwarePackage.util.formatting import canonicalize_string
```

Importing your package will work just as smoothly as importing a fancy published package
you got off PyPI!


### But that's not all!

Now that you have a `pyproject.toml`, consider configuring other tools too!
Here are some that support `pyproject.toml` configuration:

- [pytest](https://docs.pytest.org/en/6.2.x/customize.html#pyproject-toml) for automated testing
- [pytest-cov](https://coverage.readthedocs.io/en/latest/config.html) for test coverage reports
- [pylint](https://pylint.pycqa.org/en/latest/user_guide/configuration/all-options.html) the classic linter
- [mypy](https://mypy.readthedocs.io/en/stable/config_file.html) for type-checking
- [ruff](https://docs.astral.sh/ruff/configuration/), monolithic linter and formatter

It's worth looking into for any tool you use.
(And if you don't use any code quality tools, now's a great time to start!)



# Live Demo

### Brian Ward, CCM


## Survey
Please give us some feedback!

<img width="50%" src="./assets/bit.ly_sciware-sep2024.png">

[https://bit.ly/sciware-sep2024](https://bit.ly/sciware-sep2024)
