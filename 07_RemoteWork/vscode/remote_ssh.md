# VSCode - Remote-SSH extension

This vscode extension allows you to:

* Open a folder on a remote machine in vscode
* Edit files as though they are local

It's like opening an ssh terminal except you get the full 
functionality of vscode and its extensions!

The use cases go beyond code development.

### Step 1: Install the Remote-SSH vscode extension

[![Install Remote-SSH extension](https://img.youtube.com/vi/8jcrKcAGpD0/0.jpg)](https://www.youtube.com/embed/8jcrKcAGpD0)

### Step 2: Set up passwordless ssh log in to the remote machine

Although this is not strictly necessary, it simplifies the process.

See [this guide](../content.md) for more information.

### Step 3: Connect to the remote folder

* Use the green button in the lower-left part of the vscode editor
* Click "Remote SSH: Connect to Host..."
* Enter the ssh login information (e.g., user@host.com)
* Open a folder on the remote machine

[![Open a remote folder](https://img.youtube.com/vi/pByJPvqqXuU/0.jpg)](https://www.youtube.com/embed/pByJPvqqXuU)

### Use cases

* Use it as a terminal (vscode integrated terminal)
* Use it as a file explorer (vscode integrated file explorer)
* Use it as a code editor
    - Powerful integration between local and remote extensions
    - Full speed of local file editing (syntax highlighting, completion, etc.)
    - Code parsing, navigation, uses remotely installed extensions
* Drag/drop to copy files to/from the remote computer
* Git integration (Gitlense!)
* Other amazing vscode extensions

### Notes

When developing software, it's generally better to have files stored locally. So don't develop using "Remote-SSH" just because you can. There should be a good reason to use this method.

Better to use a version control system like git to sync source code between local and remote computers.

I generally use this vscode extension for maintaining files on the server (more like a terminal) rather than for actually developing code.

Some extensions are installed locally and some are installed remotely... it can sometimes be confusing. Things may not always work as expected. For example, the Docker extension always lists local containers (not remote).

### My recommendation

Use vscode with the "Remote-SSH" extension any time you need to view or edit files on a remote server via ssh.

When developing software, use a git repository and clone the files locally (do not use this extension). But DO use the [Remote-Containers](./remote_containers.md) extension!

Unfortunately, it is not currently possible to use the Remote-Containers extensions in conjunction with the Remote-SSH.

### Author of this guide

Jeremy Magland