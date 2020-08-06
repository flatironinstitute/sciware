# Sciware

## Shells and Environments

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/10_EnvShell


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

Slide 1


Slide 2



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


#### Evolution

- control structure syntax: ALGOL (`fi`), C (`{}`), other...
- ksh introduced functions
- tcsh invented history, alias, other interactive features
- bash developed (and spun off) readline, key bindings
- zsh added sophisticated tab-completion, prompts
- POSIX.2 standardized minimal shell features (cf., dash)

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
   - most common shell
   - especially for scripting
   - often assumed default
   - lags behind but catches up
- zsh
   - many interactive features
   - large, superset and compatible with both tcsh and bash
   - more permissive license (*Apple*)
   - oh my zsh (plugins, themes)
- opinions?


#### EMACS shell modes?



### Colors! (Liz)



### Shell features (Jonathan)

Slide 1


Slide 2



### Extras
