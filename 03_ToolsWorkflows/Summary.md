*   **[Vim](https://en.wikipedia.org/wiki/Vim_(text_editor))** text editor (Joakim)	
    *   lots of keystroke shortcuts, syntax highlighting options. Very little mousing.
    *   Comparable functionality to **[emacs](https://www.gnu.org/software/emacs/)**
    *   Tabs, multiple files at the same time
    *   Ctags to index and find functions in your directory tree
    *   **[Fugitive](https://github.com/tpope/vim-fugitive)** to integrate with git
    *   Vim diff, Configure status line at the bottom, Autocomplete
*   **[Screen](https://en.wikipedia.org/wiki/GNU_Screen)** (Joakim)
    *   Multiple shell sessions at the same time (Ctrl-A C)
    *   Sessions will stay active even if computer disconnects (Ctrl-A D)
    *   Can split vertically (Ctrl-A |, not available on all versions)
    *   Comparable to **[tmux](https://en.wikipedia.org/wiki/Tmux)**.
    *   [Screen User's Manual](https://www.gnu.org/software/screen/manual/screen.html)
    *   [Quick reference](http://aperiodic.net/screen/quick_reference)
*   Custom something to be able to show images in terminal (Joakim)
*   **[Readline](https://en.wikipedia.org/wiki/GNU_Readline)** (Joakim)
    *   Shortcuts in terminal and across applications
    *   .inputrc
    *   Access history of commands issued
*   **[Zsh](https://en.wikipedia.org/wiki/Z_shell)** (Nils)
    * [Zsh Summary](https://github.com/flatironinstitute/learn-sciware-dev/blob/master/03_ToolsWorkflows/zsh_wentzell.md)
    *   Shell (alternative to bash)
    *   Globbing expressions - recursive pattern matching to find files, more powerful than **find**
    *   Can find files based on file name, type, permissions
    *   **Spaceship zsh** to customize prompts and make shortcuts, tab complete
    *   git integration, has nice icon which indicate status of repo, and branch indication
    *   **[Oh my zsh](https://ohmyz.sh/)**
    *   Nice alias “git l” for generating graphical (ascii art) version of git history. Better than **git log**
    *   Likely gonna be the default in the next Mac OS release (licensing reasons)
*   **Vi plugin managers** (Nils)
    *   Language server protocol 
*   **Tmux** (Dylan)
    *   Similar to **screens **for detached sessions and working remotely
    *   Split horizontally/vertically
    *   List of active sessions
    *   Can notify you when process completes
*   Window manager (Dylan)
    *   Google “tiling window manager”
    *   Tiling for application windows
    *   **Xmonad. **Need to setup config in Haskell. 
    *   **Divvy**. Option for Mac. $14 purchase.
    *   **Magnet**. $5 option for Mac.
*   **Vim** (Ruth)
    *   More ergonomic keyboard shortcuts compared to **emacs**.
    *   jonathansick[/sickvim](https://github.com/jonathansick/sickvim) - for the config files - or [dfm/dotfiles](https://github.com/dfm/dotfiles/tree/master/neovim)
    *   Some specific keyboard bindings for latex files
    *   **Overleaf** has vim keyboard bindings 
*   **Iterm2 **(Ruth)
    *   Window manager for terminal windows
*   API documentation (Ruth)
    *   Docstring format from a google template. 
    *   Google style guide for Python: [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)
    *   Astropy using the numpy doc template
    *   Any pros and cons of numpy vs astropy/numpy template?
        *   No real difference, just aesthetic.
*   **Readthedocs** (Ruth)
    *   Auto generate documentation based on docstrings
    *   Best practice for formatting docstrings
*   **Travis** (Ruth)
    *   For automatic running of tests via github
*   **Pycharm** (Nikolai)
    *   Editor for Python, but with many, many bells and whistles.
    *   Compared to **Spyder**.
    *   Documentation screen built in access to docstrings
    *   Autocomplete functions and arguments
    *   Very visual
    *   Can autopopulate docstrings based on defined parameters and defined template
    *   Lots of git integration and visual feedback, auto displays the diff
    *   Lots of feedback on PEP and best practices
    *   Change variables throughout 
    *   Profiling
    *   Professional version has more things. ask for license from SCC. or use .edu email address to qualify for edu version.
    *   Can execute parts of the code with # %%
    *   Interact with variables and output via SciView
    *   Easy to manage different conda/pip environments
*   More** PyCharm** (Tiberiu)
    *   Integrates with **unittest**
    *   Click to run all the tests
    *   Also works with **pytest**.
    *   Debugger, add breakpoints, run line by line
    *   Run with Coverage to give graphical feedback on what is tested and not tested
    *   Can also create and edit Jupyter notebooks. Split screen interaction.
    *   Can also interact with markup languages (md, html) with a split screen interaction with code on one side and rendered version on the other.
*   Jupyter Addons (Tiberiu)
*   **Black** (Tiberiu)
    *   Code formatter - linter
    *   Reformats code 
    *   Made a custom shortcut to run black on code to reformat code
    *   Can integrate with git so it does it everytime you commit
*   **JupyterLab** (Tiberiu)
    *   Nicer interface than Jupyter
    *   Jupyterlab_code_formatter repo <add link>
*   **R in Jupyter notebook** (Danxun)
    *   **DESeq2** R package
    *   lots of work on the cluster and send up an environment with all necessary packages
    *   R kernel does support tab completion and access to data frame properties
*   **VSCode** (Jeremy)
    *   [MD file in the repo with lots of notes](https://github.com/flatironinstitute/learn-sciware-dev/blob/master/03_ToolsWorkflows/vscode/vscode_magland.md)
    *   **Sublime Text 3** is an alternative, and **Pycharm**
    *   VSCode is very different than VSStudio
    *   Lightweight text editor with extensions
    *   Developed by Microsoft but open source
    *   File explorer, split screen options
    *   Extension marketplace. Choose based on number of downloads and stars
    *   Github integration and history browsing with _GitLens_ extension
    *   Recommend Pyright extension for Python static typing
    *   Similar to **Atom**, but takes up lots of memory. Anecdotal is that VSCode is less resource intensive
    *   All of these have Vim emulator
*   **TensorBoard** (Charlie)
    *   IDE for Tensorflow (machine learning package) 
    *   Histograms of gradients to help identify trends of the model over time
*   **Cortex:** Manuscripts from github repo (Rodrigo)
    *   Reproducible papers
    *   Links to scripts/commits which generate the figure
    *   Figures live as scripts
    *   Every commit triggers a build and force pushes pdf to a new branch
