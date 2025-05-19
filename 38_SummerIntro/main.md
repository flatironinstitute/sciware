# Sciware

## Summer Sciware 1 - Setting up a laptop for scientific computing

https://sciware.flatironinstitute.org/38_SummerIntro

https://github.com/flatironinstitute/sciware/tree/main/38_SummerIntro


## Who We Are
- Sciware is a grassroots, scientific software learning community at Flatiron Institute
- We're here to help the computing parts of your summer project go more smoothly
- And we're here to help you build fundamental computing skills (terminal, VS Code, git/GitHub, Python project setup, etc)
  - These will be useful in any kind of computing career, academic or not!


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


## Summer Sciware Sessions
- Schedule
  - June 3: Summer Sciware 1 - Setting up a laptop for scientific computing
  - June 12: Summer Sciware 2 - VSCode and Github
  - June 24: Summer Sciware 3 - Intro to the cluster
  - July 2: Summer Sciware 4 - Cluster hands-on
  - All 10 AM - noon in the IDA Auditorium (162 Fifth Ave, 2nd Floor)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Where to Find Sciware
- The [#code-help](https://simonsfoundation.enterprise.slack.com/archives/C08SZK2C0TB) channel on Simons Foundation Slack
- The [#sciware](https://simonsfoundation.enterprise.slack.com/archives/CDU1EE9V5) channel on Simons Foundation Slack
- The anonymous [Summer 2025 Flatiron Computing Question Form](https://docs.google.com/forms/d/e/1FAIpQLSemCVw8_QHXFXN6nS27z-QMIpaWhvHNBVi7tRxAs85RaGbc4w/viewform?usp=dialog) Google Form
- Sciware website: https://sciware.flatironinstitute.org/


## Today's Agenda
- Install prerequisite software (xcode on Mac, WSL on Windows)
- Install uv Python
- Install VS Code
- Setup a Python project
- Setup a Jupyter Notebook in that project


## Prerequisite Software
- Mac users:
  - Open a terminal: press Command (⌘) + Space to open Spotlight Search, type "Terminal", and press Enter.
  - Run: `xcode-select --install`
- Windows users:
  - In the Start Menu, search for Window Command Prompt
  - Right click on Windows Command Prompt and select "Run as administrator"
  - Run: `wsl --install`
  - Restart your computer
  - If you can open WSL from the Start Menu, you're done! Otherwise, ask for help.
  - More detailed instructions here: https://learn.microsoft.com/en-us/windows/wsl/install


## Install VS Code
- Go to [code.visualstudio.com](code.visualstudio.com)
- Click Download in the top right
- Mac users: download and install the Mac version
- Windows users: download and install the Windows version
  - Most of the time with WSL, you will install the Linux version of packages. VS Code is the only exception to this rule that I'm aware of!


## Open a terminal in VS Code
- Mac users:
  - Open VS Code from the Applications folder
  - Press Command (⌘) + J to open the terminal
- Windows users:
  - Open VS Code from the Start Menu
  - Install the WSL extension
    - If you see a pop-up asking if you want to install the WSL extension, click "Install"
    - If you don't see a pop-up, click the Extensions icon in the left sidebar (or press Ctrl + Shift + X)
    - Search for "WSL" in the Extensions Marketplace
    - Click the green "Install" button next to "Remote - WSL"
  - Connect to WSL
    - Click the blue or green "Open a remote window" button in the bottom left corner of the window
    - Select "Connect to WSL"
  - Open a terminal
    - Press Ctrl + Shift + J to open the terminal


## Install uv Python
- Go to [docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- Click Installation on the left
- Copy the standalone installer command: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Open a terminal
  - Mac users: press Command (⌘) + Space to open Spotlight Search, type "Terminal", and press Enter.
  - Windows users: open the Start Menu, type "WSL", and click on WSL.
- Paste and run the standalone installer command
- Close the terminal (type `exit` and press Enter)
- Reopen the terminal and run `uv --version` to check that it installed correctly


## Start a Python Project

These instructions are adapted from uv's ["Working on projects"](https://docs.astral.sh/uv/guides/projects/) documentation.

- **WSL Users**: Open VS Code, then connect to WSL by clicking the "Open a remote window" button in the bottom left corner of the window and selecting "Connect to WSL".
- Open a terminal in VS Code (`Ctrl or Command + J`).

To create a new Python project and open it as a VS Code workspace, run:

```console
uv init summer-2025
code summer-2025
```

## Add a Dependency
To add a dependency (for example, NumPy), use:

```console
uv add numpy
```

- Check the `pyproject.toml` file—uv has added NumPy as a dependency!


## Run a Script
- Create a new file (e.g., `science.py`) and write code that uses your new dependency.
- To run your script, use:

```console
uv run science.py
```

- With uv, use `uv run script.py` instead of `python script.py` to ensure your virtual environment is always in sync with your dependencies.
- After adding a dependency or running a script, a virtual environment will appear in the `.venv` directory.
- Make sure VS Code uses this environment: press `F1`, type `Python: Select Interpreter`, and choose the `.venv` in your project directory.

For more advanced projects (like packages for GitHub or PyPI), see uv's [project concepts](https://docs.astral.sh/uv/concepts/projects/init/).


## Using Notebooks

These instructions are adapted from uv's ["Using Jupyter from VS Code"](https://docs.astral.sh/uv/guides/integration/jupyter/#using-jupyter-from-vs-code) documentation.

- Add `ipykernel` as a development dependency:

```console
uv add --dev ipykernel
```

- Make sure VS Code is using the virtual environment:
  - Press `F1`, type `Python: Select Interpreter`, and select the `.venv` in your project directory.

- Create a new notebook:
  - Press `F1`, type `Create: New Jupyter Notebook`.
  - Click `Select kernel` in the top right, choose `Python environments...`, and select the `.venv` in your project directory.

- To add new dependencies (like NumPy), run `uv add numpy` in the terminal—they'll be available in your notebook.


## Resources
- uv has excellent [documentation](https://docs.astral.sh/uv), including a [guide for Jupyter integration](https://docs.astral.sh/uv/guides/integration/jupyter/). If you get stuck, check the docs, or get in touch with us!


## Survey
Please give us some feedback!

[![survey](./qrcode.png)] 
