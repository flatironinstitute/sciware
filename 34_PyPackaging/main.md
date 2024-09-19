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


## Zoom Specific

- Dedicated Zoom moderator to field questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Future Sessions

- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda

- What do we mean by packaging, and why do you want to do it?
- Review of the Python import system 
- Configuring your project with `pyrpoject.toml`
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


Bet you never have these issues with packages you install by `pip`.

You just `import ThePackage` and it Just Works.

Running your own code should be that simple too.


What we'll show you today helps get you ready for *distributing* your
work on a package archive like PyPI. But we'll leave the fine details of
that for a future Sciware about distributing code (already in planning).

For today, we just want you to be able to `import` your code as easily
as you do someone else's.


## Defining Terms


### "Package" vs "Module" vs "Project"

The [documentation](https://docs.python.org/3/glossary.html#term-package) can
be a little confusing or circular.

For today, we use these to mean:

- A `project` is some collection of files that you're working on.
- A `module` is any file that has Python code.
  - We won't use this term.
- A `package` is a bundle of Python code you can *import*.
  - Can be one or more files (the user doesn't need to care)
  - Can be downloaded from a repository or installed locally

We'll use "project" to refer to something you're editing, and "package"
to refer to something you want to import.

Our goal for today is to show how easy and beneficial it is to make your
*projects* into (locally) importable *packages*.


### pip, pypi, conda, condaforge...

- `pip` is a tool for installing packages.
- `pypi` is one *package repository* where you can download packages.
- `conda` is one tool for managing [virtual environments](https://docs.python.org/3/tutorial/venv.html).
  - A `virtual environment` lets you control which packages (& versions) are visible. This helps
  avoid conflicts between different projects or tools running on the same machine.
- `conda-forge` is another package repository, specific to conda. It also provides non-Python packages.

Today we will assume you are working in a virtual environment (you always should!) but we'll only talk
about installation with pip.


### namespaces

A [namespace](https://docs.python.org/3/glossary.html#term-namespace) is a way to create a hierarchy
of names.

They let different packages define variables, functions, and classes without worrying about uniqueness.

Example:
- `numpy.linalg.norm()` is one function
- `torch.norm()` is a different function
- Both compute norms, but they have different parameters and work on different objects
- You can use both because the namespace (`numpy` vs `torch`) clarifies what you mean.


### global vs local namespaces

The *global namespace* is the top level for everything in the file. Example:
```python
x = 10
print(f"{x}")
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

print(f'{sqrt(16)}')
print(f'{math.pi}') # fails--we didn't import math!
my_array_1 = np.array([1, 2, 3])
my_array_2 = numpy.array([1, 2, 3]) # fails!
```
- `sqrt` is attached to the *global namespace*
- its parent, `math`, is not!
- The `numpy` package has been imported with an alias
  - That *alias* is in the global namespace, but the original name isn't


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

Python tries to satisfy `import FOO` by looking for a module named `FOO`.

The places it looks are defined in `sys.path`, a list of filesystem locations.

This list will include various standard locations, as well as your current
working directory--but that working directory will change with every `cd`!

Reliable imports require the package to be in one of the standard locations.


### Package installation

When you install a package (like with `pip`), you're downloading a bundle with
its code, and placing that in a standard location that's part of `sys.path`.

(This is actually how virtual environments work--they set `sys.path` to something
unique, and install packages there, so that's where Python finds them.)


But `pip` can also install *your project* as a package, using *edit mode*:

`$ pip install -e /path/to/my/project`

When you do this, the base directory of your project gets added to `sys.path`.
So regular import patterns work. All you need to do is to tell `pip` (or
any other package installer) *how* your project should be bundled.

We do that through `pyproject.toml`.


## Properly Handling your Python Project

<img height="50%" src="assets/wikihow-Hold-a-Snake-Step-13-Version-2.jpg" class="plain">


### pyproject.toml

- The modern way to configure a project
  - Not just for packaging! It's a unified configuration file!
- Written in [toml](https://toml.io/en/) format--human-readable
- Goes in the root of your project's source code directory


### Minimal requirements for installability

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


Additional fields can be useful:
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
- Most of these fields help other users find your project once it's uploaded to a repository
- `readme` can be set to text, or a file, or even marked `dynamic` (see later)
- The `license` field lets you reference how others are allowed to use your code


### build system

In addition to the `[project]` section, you also need a `[build-system]`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend="setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}
packages = ["MY_PROJECT"]
```

This tells `pip` what tools to use to bundle up your code. We've specified `setuptools` here.

Then we have a separate config block for `setuptools` specifically (`pyproject.toml` combines
tool-specific config into the same file).


```toml
[tool.setuptools]
package-dir = {"" = "src"}
packages = ["MY_PROJECT"]
```

This is specific to `setuptools`. We're just telling it:
- The root directory of the code to distribute (the `src` directory adjacent to where this file is located)
- The packages that should be installed (just matches the `name` field of the `[project]` section)


That's it! You can install your project as a package.

- Assume our project is at `~/MY_PROJECT`
- We have `~/MY_PROJECT/pyproject.toml` defined as above
- And the code lives in `~/MY_PROJECT/src/`

```bash
$ cd ~/MY_PROJECT
$ pip install -e .
```


Now, in *any* Python file *anywhere*, you can just

```python
from MY_PROJECT import my_cool_stuff
from MY_PROJECT.util import my_cool_util
```

and it'll be just as smooth as the fancy store-bought packages you got from PyPI.


### But that's not all!

Now that you have `pyproject.toml` set up in your project, it's a great time
and place to configure other code quality tools! In particular, I like to use:

- `[tool.pytest]` to set default options for running tests
- `[tool.coverage.run]` config to specify what files should be considered for test coverage reports
- `[tool.pylint]` to set what style rules to enforce and limit unnecessary messages
- `[tool.mypy]` to customize type-checking behavior and strictness

There's many more! It's worth looking into for any other tooling your project is using.
(And if you don't have any, now's a great time to consider it!)



# Live Demo



## Survey
Please give us some feedback!

https://bit.ly/sciware-file-formats-2022

![bit ly_sciware-file-formats-2022](https://user-images.githubusercontent.com/1444249/207740745-d14dabf1-9227-4cd8-bd4a-72843da1003d.png)
