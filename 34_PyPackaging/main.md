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


What we'll show today helps get you ready for *distributing* your
work on a package archive like PyPI.

But we'll leave the fine details of
that for a future Sciware about distributing code.

For today, we just want you to be able to `import` your own code as easily
as you do someone else's.


## Defining Terms


### "Package" vs "Module" vs "Project"

The [documentation](https://docs.python.org/3/glossary.html#term-package) can
be quite confusing.

For today, we use these to mean:

- A `project` is some collection of files that you're working on.
- A `module` is any file that has Python code.
  - We won't use this term.
- A `package` is a bundle of Python code you can *import*.
  - Can be one or more files (the user doesn't need to care)
  - Can be downloaded from a repository or installed locally


In short:

We'll use "project" to refer to something you're editing, and "package"
to refer to something you want to import.

Our goal for today is to show how easy and beneficial it is to make your
*projects* into (locally) importable *packages*.


### Why Packages?

We've said packages are "stuff you can import."

So the point of packages is *code reuse*. They are
libraries of pre-written code.

A big part of Python's success is its robust package ecosystem!


<img src="https://imgs.xkcd.com/comics/python.png">


That comic is from *2007*. There have been a lot of changes and complications
to the Python import system in that time!

The system as a whole is still trying to solve 3 problems:

- How do I get useful code from other people
- How do I share my useful code with others
- How do I run the *right* code


## Five Pillars of Python Packages

- Python version management
- Environment management
- Package management
- Package building
- Package publishing


### Version control

- Python version management
  - i.e. interpreter. Python 2 is not 3.6 is not 3.12
- Package management
  - Regardless of environment, how do I install 3rd-party code?
  - `pip`, `conda`
- Environment management
  - Different tasks require different, maybe conflicting, packages
  - [(virtual) environments](https://docs.python.org/3/tutorial/venv.html) let them coexist
  - `venv`, `conda`


### Package distribution

- Package building
  - How do I get my code into a distributable form
  - `setuptools`, `hatch`, `pdm`, others
- Package publishing
  - How do I put my bundled code in a public place
  - `twine` (bundling), `PyPI` (a repository)


### Five Pillars Revisited

- Python version management <!-- .element style="color: #999999" -->
- Environment management <!-- .element style="color: #999999" -->
- **Package management**
- **Package building**
- Package publishing <!-- .element style="color: #999999" -->

For today, the tools we're focusing on are
`pip` and (a little bit of) `setuptools`.


### namespaces

A [namespace](https://docs.python.org/3/glossary.html#term-namespace) creates a hierarchy
of names.

Namespaces let packages define variables, functions, and classes without worrying about uniqueness.


Example:
- `numpy.linalg.norm()` is one function
- `torch.norm()` is a different function
- Both compute norms, but they have different parameters and work on different objects
- You can use both because the namespace (`numpy` vs `torch`) clarifies what you mean.


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

- Finds the code you're importing, and
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

- When you `import FOO`, Python looks for a module named `FOO`
- It looks in the list of locations defined in `sys.path`
- This list includes various standard locations
- It also includes your current working directory
  - But that changes with every `cd`!

Reliable imports require the package to be in one of the standard locations.


### Package installation

- When you `pip install` a package, `pip`:
  - downloads a bundle with the package code
  - Places it in a standard location (in `sys.path`)


### A bit more about environments

`sys.path` is actually how virtual
environments work.

Let's take a look at a `venv` virtual environment and
what happens when I install packages in it.

[LIVE]


`pip` can also install *your project* as a package, using *edit mode*:

`$ pip install -e /path/to/my/project`

- the base directory of your project gets added to `sys.path`
- Now regular import patterns work!
- First you just have to tell `pip` how to bundle your project

We do that through `pyproject.toml`.



## Properly Handling Python Projects

<img height="50%" src="assets/wikihow-Hold-a-Snake-Step-13-Version-2.jpg" class="plain">


### TODO: An example directory structure for a Python project
Which we'll show and refer to for the below


### pyproject.toml

- The modern way to configure a project
  - Not just for packaging--it's a single-source config file
- Written in [toml](https://toml.io/en/) format, so human-readable
- Goes in the root of your project's source code directory


Quick aside: there's a lot of old material recommending old package
configuration methods. Guides referring to `setup.cfg` are almost certainly
outdated.

`setup.py` is sometimes still required, but only very rarely--if you aren't
very positive why you need it, you might just have outdated instructions.


### Minimal requirements for package installation

`[project]` section:

```toml
[project]
name = "MY_PROJECT"
version = "0.0.1"
requires-python = ">=3.8"
dependencies = [
    "numpy>=1.24.0",
    "scipy>=1.10.0",
    "scikit-learn>=1.3.0"
]
```

`name` will be the name you use to import the package.

`dependencies` will be automatically installed when you `pip install` the package.


Additional fields for distributing your package:
```toml
[project]
...
description = "Describe your package here"
authors = [
    { name = "Your Name", email = "you@your.email" }
]
readme = "README.md"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]

[project.license]
file = "LICENSE"
```
- These help other users find your uploaded project
- `readme` can be text, a file, or even `dynamic` (see later)
- The `license` field grants others rights to use your code


### build system

Alongside the `[project]` section, you also need a `[build-system]`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend="setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}
packages = ["MY_PROJECT"]
```

This tells `pip` what tools to use to bundle up your code. `setuptools` is a
well-supported and painless option.

Then we have another config block for the `setuptools` tool.

(`pyproject.toml` combines tool-specific config into the same file)


```toml
[tool.setuptools]
package-dir = {"" = "src"}
packages = ["MY_PROJECT"]
```

This block is specific to `setuptools`. It just defines:
- the root directory of the code to distribute (the `src` directory adjacent to where this file is located)
- the packages that should be bundled (matches the `name` field of the `[project]` section)


That's it! With this minimal `pyproject.toml` config in place, you can install your project as a package.

- Assume our project is at `~/MY_PROJECT`
- We have `~/MY_PROJECT/pyproject.toml` defined as above
- And the code lives in `~/MY_PROJECT/src/`. Then:

```bash
$ cd ~/MY_PROJECT
$ pip install -e .
```


Now, in *any* Python file *anywhere*, you can just

```python
from MY_PROJECT import my_cool_stuff
from MY_PROJECT.util import my_cool_util
```

and those functions will be just as smooth and simple to use as the fancy store-bought ones you
got from a package off PyPI.


### But that's not all!

Now that you have `pyproject.toml` set up in your project, consider configuring other code quality
tools there! In particular, I like:

- `[tool.pytest]` to set default options for running tests
- `[tool.coverage.run]` to specify what files should be considered for test coverage reports
- `[tool.pylint]` to set what style rules to enforce and limit unnecessary messages
- `[tool.mypy]` to customize type-checking strictness

There's many more! It's worth looking into for any other tooling your project is using.
(And if you don't have any, now's a great time to consider it!)



# Live Demo

### Brian Ward, CCM


## Survey
Please give us some feedback!

NEED TO UPDATE SURVEY LINK
