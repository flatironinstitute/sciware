# Sciware

## Summer Sciware 1
## Setting up a laptop for scientific computing

https://sciware.flatironinstitute.org/38_SummerIntro

https://github.com/flatironinstitute/sciware/tree/main/38_SummerIntro


## Who We Are
- Sciware is a grassroots, scientific software learning community at Flatiron Institute
- We're here to help! Our goals are:
  - to help you setup and learn the computing tools you need to do your summer work, and
  - to help you build fundamental computing skills (terminal, VS Code, git/GitHub, Python project setup, etc).
- These will be useful in any kind of computing career, academic or not!

<!-- ## Rules of Engagement
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
</small> -->


## Summer Sciware Sessions
- Schedule
  - **June 3**: Summer Sciware 1 - Setting up a laptop for scientific computing
  - **June 12**: Summer Sciware 2 - VSCode and Github
  - **June 24**: Summer Sciware 3 - Intro to the cluster
  - **July 2**: Summer Sciware 4 - Cluster hands-on
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
  1. Open a terminal: press Command (⌘) + Space to open Spotlight Search, type "Terminal", and press Enter.
  1. Run: `xcode-select --install`
- Windows users:
  1. In the Start Menu, search for Window Command Prompt
  1. Right click on Windows Command Prompt and select "Run as administrator"
  1. Run: `wsl --install`
  1. Restart your computer
  1. If you can open WSL from the Start Menu, you're done! Otherwise, ask for help.
  
More detailed instructions here: https://learn.microsoft.com/en-us/windows/wsl/install


## Install VS Code
- Go to [code.visualstudio.com](https://code.visualstudio.com)
- Click Download in the top right
- Mac users: download and install the Mac version
- Windows users: download and install the Windows version
  - Most of the time with WSL, you will install the Linux version of packages. VS Code is the only exception to this rule!


## Windows Only: VS Code Setup
- Mac users:
  - Skip this slide.
- Install the WSL extension
  - Open VS Code from the Start Menu
  - Install the WSL extension
    - If you see a pop-up asking if you want to install the WSL extension, click "Install"
    - If you don't see a pop-up, click the Extensions icon in the left sidebar (or press Ctrl + Shift + X)
    - Search for "WSL" in the Extensions Marketplace
    - Click the "Install" button next to the "WSL" extension
- Connect to WSL
  - Click the blue "Open a Remote Window" button in the bottom left corner of the window
  - Select "Connect to WSL"
  - VS Code should reload, and you should see "WSL" in the bottom left corner of the window


## Open a Terminal in VS Code
- Mac users:
  - Open VS Code from the Applications folder
  - Press Command (⌘) + J to open the terminal
- Windows users:
  - Open VS Code from the Start Menu
  - Press Ctrl + J to open the terminal


## Install uv Python
- Go to [docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- Click Installation on the left
- Copy the standalone installer command: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Paste the command in the terminal and press Enter
- Close the terminal (type `exit` and press Enter)
- Reopen the terminal (Ctrl/⌘ + J) and run `uv --version` to check that it installed correctly


## Start a Python Project
These instructions are adapted from uv's ["Working on projects"](https://docs.astral.sh/uv/guides/projects/) documentation.

- **WSL Users**: check the Remote Window icon in the bottom left of the screen: it should say WSL. If it does not, click the icon and select "Connect to WSL".
- Open a terminal in VS Code (`Ctrl/⌘ + J`).
- To create a new Python project and open it as a VS Code workspace, run:
  ```console
  uv init sciware-2025
  code sciware-2025
  ```


## Add a Dependency
- To add a dependency (for example, NumPy), use:
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


## uv Cheatsheet
| Traditional Command         | uv Equivalent         | Description                                 |
|----------------------------|-----------------------|---------------------------------------------|
| `pip install package`      | `uv add package`      | Add a package as a dependency               |
| `pip uninstall package`    | `uv remove package`   | Remove a package from dependencies           |
| `python script.py`         | `uv run script.py`    | Run a Python script using project env       |


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


## Exercise: Create a New Project
1. Create a new project called `sciware-exercise` in your home directory.
2. Open the project in VS Code.
3. Add `numpy` and `matplotlib` as dependencies.
4. Add `ipykernel` as a development dependency.
5. Create a new notebook in the project.
7. Make a colorful scatter plot from a 2D Gaussian distribution!
  1. Use NumPy to generate 100 random points from a 2D Gaussian distribution with mean `[0, 0]` and covariance `[[1, 0.5], [0.5, 1]]`.
  2. Use Matplotlib to create a scatter plot of the points, with each point colored by a random value between 0 and 1.

  ```python
  import numpy as np
  import matplotlib.pyplot as plt

  N = 100
  rng = np.random.default_rng()
  mean = [0, 0]
  cov = [[1, 0.5], [0.5, 1]]  # Covariance matrix for some correlation
  x, y = rng.multivariate_normal(mean, cov, N).T
  colors = rng.random(N)  # Random color for each point

  plt.scatter(x, y, c=colors, cmap='viridis', s=60)
  plt.title('Random Colorful Gaussian Scatter Plot')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.colorbar(label='Color value')
  plt.show()
  ```

## Resources
- uv has excellent [documentation](https://docs.astral.sh/uv), including a [guide for Jupyter integration](https://docs.astral.sh/uv/guides/integration/jupyter/). If you get stuck, check the docs, or get in touch with us!
- Microsoft's VS Code introduction: https://code.visualstudio.com/docs/getstarted/getting-started
- VS Code documentation for the cluster: https://wiki.flatironinstitute.org/SCC/Software/VSCode


## Survey
Please give us some feedback!

[![survey](./qrcode.png)] 
