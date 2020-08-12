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

- Future sessions planned:
  - github with Software Carpentry Sep 25-26 (2 day session!)
  - Designing APIs and software library interfaces
  - Data storage file formats (hdf5, numpy, parquet, sqlite, ...)
- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

- Environment variables
  - Introduction
  - Specific variables
  - Control
- Shells
  - Comparison
  - Features


## Defining terms

One often hears these terms used interchangably. Let's clairfy.

* Kernel * Shell * Terminal * Command Line * Console


### Kernel & Operating System

_Kernel_ is the bridge between application software and hardware.

_Operating System_ is comprised of a kernel + other applications.

<small>_Linux_ 🐧 can refer to a kernel or an OS built on that kernel.</small>


### Shell

A _Shell_ is a program that takes commands, gives them to the operating system to perform, and returns output. As opposed to a _graphical user interface_ (GUI), the shell is a _command line interface_ (CLI).

<small>Remember: The shell interface surrounds the kernel just as a nutshell surrounds a nut 🥜.</small>


### Common Shells

On most Linux systems `bash` (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, `sh`, written by Steve Bourne) acts as the shell program.

Besides bash, other shell programs include: `fish`, `ksh`, `tcsh`, and `zsh`.

<small>Note: As of macOS Catalina (Nov 19), `zsh` is now the default Mac shell.</small>


### Terminal

_Terminal_ is a program that runs and provides i/o to a shell (or other program).

Originally a physical device, now we run software terminal emulators.

Many different terminal emulators (Gnome-Terminal, iTerm, Terminator, xterm), but they all do the same thing - give you access to a shell session.

Opinions?


### Console

Console originally referred to the physical text entry and display device for system administration messages.
Now often used specifically in context of sys admin messages from BIOS, kernel, and the system logger, or the text mode of the OS (Alt-F1 in Linux).

```javascript
  console.log("👋 hello, you are in a web browser.");
```


### Bash Startup Process

The bash shell program uses a collection of startup files to help create an environment. Each file has a specific use and may affect login and interactive environments differently.

The files in the /etc directory generally provide global settings. If an equivalent file exists in your home directory it may override the global settings.


### Bash Startup



## Environment variables

<small>Jump to Nick's slides</small>



### Environment control (Robert)



## Shells

### Comparison (Dylan)


#### History

<img src="img/evolve.svg" width="1000" style="border:0;box-shadow:none">

- run commands, interactive, slowly developed more scripting features
- control structure syntax: ALGOL (`fi`, `esac`), C (`{}`), *other*...


#### Evolution

- ksh introduced functions
- tcsh invented history, alias, other interactive features
- bash developed (and spun off) readline, key bindings
- zsh added sophisticated tab-completion, prompts
- POSIX.2 standardized minimal shell features (see `dash`)

most modern shells copied, adopted similar, popular features


#### Startup files

<table>
<thead><tr><th>shell</th><th>login</th><th>interactive</th><th>neither</th></tr></thead>
<tbody>
<tr><td rowspan='2'>bash</td><td><code>.bash_profile</code> | <code>.bash_login</code> | <code>.profile</code></td><td><code>.bashrc</code></td><td>-</td></tr>
<tr>   <td><code>.bash_logout</code></td><td>-</td><td>-</td></tr>
<tr><td rowspan='2'>tcsh</td><td colspan='3' style="text-align: center;"><code>.tcshrc</code> | <code>.cshrc</code></td></tr>
<tr>   <td><code>.login</code>, <code>.logout</code></td><td>-</td><td>-</td></tr>
<tr><td rowspan='4'>zsh</td><td colspan='3' style="text-align: center;"><code>.zshenv</code></td></tr>
<tr>   <td><code>.zprofile</code></td><td>-</td><td>-</td></tr>
<tr>   <td colspan='2' style="text-align: center;"><code>.zshrc</code></td><td>-</td></tr>
<tr>   <td><code>.zlogin</code>, <code>.zlogout</code></td><td>-</td><td>-</td></tr>
</tbody>
</table>


#### Changing your shell

- Current shell: `$SHELL`, `ps`
- Most systems: `chsh`
- FI: email scicomp@flatironinstitute.org
- caveat: some things only work out of the box in bash (modules, source)
- alternative: exec different shell from `.bash_profile`

```sh
if [[ $- == *i* && -x /bin/zsh ]] ; then
	SHELL=/bin/zsh exec /bin/zsh -l
fi
```


#### Preferences

- bash
  - most common shell, especially for scripting
  - often assumed default
  - lags behind, catches up
- tcsh: fallen out of favor, non-POSIX, still maintained
- zsh
  - large, superset and **compatible with bash** and tcsh
  - many interactive features, tab completion
     - <small>`git diff <tab>`, `gcc -<tab>`, `rsync host:<tab>`</small>
  - more permissive license _(Apple)_
  - oh my zsh (plugins, themes)
- opinions?



### Configuring your prompt 🎨



### Shell features (Jonathan)



### Extras

* tab completion, expansion
* command history, `fc`
* shell scripting
* slurm
* jupyter kernels
