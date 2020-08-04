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


#### History

<img src="img/evolve.svg" width="1000" style="border:0;box-shadow:none">

- POSIX standard
- C vs ALGOL


#### Startup files

<table>
<thead><tr><th>shell</th><th>login</th><th>interactive</th><th>neither</th></tr></thead>
<tbody>
<tr><td rowspan='2'>bash</td><td>`.bash_profile`|`.bash_login`|`.profile`</td><td>`.bashrc`</td></tr>
<tr>   <td>`.bash_logout`</td></tr>
<tr><td rowspan='4'>zsh</td><td colspan='3'>`.zshenv`</td><tr>
<tr>   <td>`.zprofile`</td></tr>
<tr>   <td colspan='2'>`.zshrc`</td></tr>
<tr>   <td>`.zlogin`, `.zlogout`</td></tr>
<tr><td rowspan='2'>tcsh</td><td colspan='3'>`.tcshrc`|`.cshrc`</td><tr>
<tr>   <td>`.login`</td></tr>
</tbody>
</table>


#### Changing your shell

- Most systems: `chsh`
- FI: email us
- caveats


#### EMACS shell modes?



### Colors! (Liz)



### Shell features (Jonathan)

Slide 1


Slide 2



### Extras
