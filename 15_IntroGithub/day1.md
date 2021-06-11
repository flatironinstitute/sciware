# Sciware

## Intro to Github

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/15_IntroGithub


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
- We are recording. Link will be posted on #sciware Slack.


## Future Sessions

- July 8: Intro to IDEs and Debugging
- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

- What is Git and GitHub? 
- Setting up GitHub on your computer
- Getting code off of GitHub
- Putting code onto GitHub



# Intro to Git and GitHub

Dylan's slides here.



# Setting up GitHub on your Computer


## Make sure `git` is installed
```angular2html
> git version`
git version 2.30.1 (Apple Git-130)
```

If this returns an error, please raise your hand and someone can help you in a berakout room.

## Setting your name in Git 

### See what name is currently set
```
> git config --global user.name`
```

### Set your name
```
> git config --global user.name "Mona Lisa"
```


## Setting your email address

### See what email address is currently set
```
> git config --global user.email`
```

### Set an email address
```
> git config --global user.email "your_email@example.com"
```


## Setup SSH

### Generate an SSH key and copy it to the clipboard
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```
```
pbcopy < ~/.ssh/id_ed25519.pub
```

### Add the SSH key to GitHub
Profile Photo > Settings > SSH ad GPG keys > New SSH Key

Title should refer to the computer on which the key was generated.

Paste key into text box.


## Setup Git's default text editor
So that you don't get stuck in vi:
```
git config --global core.editor "nano -w"
```

**How to set up your favorite editor with Git:**
>https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config#ch_core_editor



# Getting code off of GitHub



# Putting code on GitHub