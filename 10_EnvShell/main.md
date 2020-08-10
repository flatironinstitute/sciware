# Sciware

## Shells and Environments

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/10_EnvShell

## Rules of Engagement

### Goal:

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, _technology choices_\*, and scientific disciplines.

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

- If comfortable, please keep video on so we can all see each other's faces.
- Ok to break in for quick, clarifying questions.
- Use Raise Hand feature for new topics or for more in-depth questions.
- Please stay muted if not speaking. (Host may mute you.)

## Feedback

- Future sessions planned?
- Suggest topics and vote on options in #sciware Slack

## Today's Agenda

- Environment variables
  - Introduction
  - Specific variables
  - Control
- Shells
  - Comparison
  - Features

## Environment variables

### Basic terms (Liz)

#### Defining our Terms

One often hears the following used interchangably. Let's clairfy.

    - Kernel
    - Shell
    - Command Line
    - Console

#### Kernel & Operating System

- Kernel: the bridge between application software and hardware.
- Operating System: comprised of a kernel + other applications.
- Linux can refer to a kernel or an OS built on that kernel.

#### Shell

- Name origin: Shell interface 🐚 surrounds the kernel just as a nutshell surrounds a nut 🥜.
- Shell is a program that takes commands, gives them to the operating system to perform, and returns output.
- In the old days, it was the _only_ user interface. Nowadays, we have graphical user interfaces (GUIs) in addition to command line interfaces (CLIs) such as the shell.

#### Shell Examples

- On most Linux systems `bash` (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, `sh`, written by Steve Bourne) acts as the shell program.
- Besides bash, other shell programs include: `fish`, `ksh`, `tcsh`, and `zsh`.
- Note: As of macOS Catalina (Nov 19), `zsh` is now the default Mac shell.

#### Terminal

- Terminal is a program that runs a shell.
- Originally a physical device, now we run software terminal emulators.
- Many different terminal emulators (Gnome-Terminal, iTerm, Terminator), but they all do the same thing - give you access to a shell session.
- Opinions?

#### Console

- Console originally referred to the physical text entry and display device for system adminstration messages.
- Now often used specifically in context of sys admin messages from BIOS, kernel, and the system logger.
- ```javascript
  console.log("👋from your web browser.");
  ```

#### Bash Startup Process

The bash shell program uses a collection of startup files to help create an environment. Each file has a specific use and may affect login and interactive environments differently. The files in the /etc directory generally provide global settings. If an equivalent file exists in your home directory it may override the global settings.

#### Bash Startup

<img src="img/bashstartup.svg" width="1000" style="border:0;box-shadow:none">

### Specific variables (Nick)

Slide 1

Slide 2

### Environment control (Robert)

Slide 1

Slide 2

## Shells

### Comparison (Dylan)

- Ways to interact with the system (surface, outer layer, vs kernel)
- Run commands, other programs

#### History

<img src="img/evolve.svg" width="1000" style="border:0;box-shadow:none">

- control structure syntax: ALGOL (`fi`) vs. C (`{}`)
- interactive vs. scripting
- POSIX.2 standard: widely adopted

#### Present

- most modern shells have similar features
- tcsh invented history, alias, others copied
- zsh developed sophisticated tab-completion, prompts, bash followed

- bash: most common shell, especially for scripting, often assumed default, lags behind but catches up
- zsh: many interactive features, large, more permissive license (cf Apple), oh my zsh (plugins, themes)
- opinions?

#### Startup files

<table>
<thead><tr><th>shell</th><th>login</th><th>interactive</th><th>neither</th></tr></thead>
<tbody>
<tr><td rowspan='2'>bash</td><td><code>.bash_profile</code> | <code>.bash_login</code> | <code>.profile</code></td><td><code>.bashrc</code></td><td>-</td></tr>
<tr>   <td><code>.bash_logout</code></td><td>-</td><td>-</td></tr>
<tr><td rowspan='4'>zsh</td><td colspan='3' style="text-align: center;"><code>.zshenv</code></td></tr>
<tr>   <td><code>.zprofile</code></td><td>-</td><td>-</td></tr>
<tr>   <td colspan='2' style="text-align: center;"><code>.zshrc</code></td><td>-</td></tr>
<tr>   <td><code>.zlogin</code>, <code>.zlogout</code></td><td>-</td><td>-</td></tr>
<tr><td rowspan='2'>tcsh</td><td colspan='3' style="text-align: center;"><code>.tcshrc</code> | <code>.cshrc</code></td></tr>
<tr>   <td><code>.login</code>, <code>.logout</code></td><td>-</td><td>-</td></tr>
</tbody>
</table>

#### Changing your shell

- Most systems: `chsh`
- FI: email scicomp@flatironinstitute.org
- caveat: many things only work out of the box in bash (modules, source)
- alternative: exec different shell from `.bash_profile`

```

if [[ $- == *i* && -x /bin/zsh ]] ; then
SHELL=/bin/zsh exec /bin/zsh -l
fi

```

#### EMACS shell modes?

### Colors! (Liz)

### Shell features (Jonathan)

Slide 1

Slide 2

### Extras

```

```
