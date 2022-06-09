# Intro to Github
- Jun 21-22 2022
- 10:00am-12:00pm
- Flatiron 2nd floor IDA

- [day 1: github](https://sciware.flatironinstitute.org/21_IntroGithub/slides1.html) ([source](day1.md))
- [day 2: collaboration](https://sciware.flatironinstitute.org/21_IntroGithub/slides2.html) ([source](day2.md))

## Pre-workshop prep

- Create a [Github account](https://github.com/join) if you don't already have one.
- If you are running Windows, [install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)
- Make sure you have a working terminal on your laptop
  launch a terminal (such as `Terminal.app` on OS X or `WSL`/`Ubuntu` on Windows)
  and ensure that you see something similar when running `echo $SHELL` in the terminal.
  ```
  > echo $SHELL
  /usr/bin/bash
  ```
   you also might see `/usr/bin/zsh` or `/bin/bash` or `/bin/zsh`, depending on your environment. If you instead see
   `$SHELL`, you are probably running a Windows `command` prompt and not in WSL.
- Make sure you have git installed. In your terminal:
  ```
  > git --version
  git version 1.8.3
  ```
  if you have a higher version, that is perfectly fine.
- Make sure you have ssh-keygen:
  ```
  > which ssh-keygen
  /usr/bin/ssh-keygen
  ```
  or something similar should be returned.
- If you have trouble with any of the above steps, please don't hesitate to contact us in either the #sciware
  slack channel or via email at sciware@flatironinstitute.org
