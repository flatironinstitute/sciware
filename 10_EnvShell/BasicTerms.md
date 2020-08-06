# Defining our Terms

One often hears the terms terminal, command line, shell, and console used interchangably so before we discuss the configuration, let us define our terms.

### Kernel

Kernel is the bridge between application software and hardware. When a computer boots up, a kernel recognizes its own physical hardware and enables each component to talk with one another. It is the first program that is loaded into the main memory and remains in the main memory until the system is shut down.

The Operating System is comprised of a kernel and a bunch of other applications that control the very low-level aspects of the hardware and provides APIs to software to use them.

Note that Linux is not an OS, but rather a kernel.

Ex: Hardware drivers, orchestrated by the kernel, keep fans active to prevent overheating, disk space is monitored, RAM states managed, new devices are detected, and so on.

### Shell

Simply put, the shell is a program that takes commands, gives them to the operating system to perform, and returns output. In the old days, it was the only user interface available on a Unix-like system such as Linux. Nowadays, we have graphical user interfaces (GUIs) in addition to command line interfaces (CLIs) such as the shell.

There are different accounts on why the term "shell" was chosen, but a believable explanation is that the shell interface 🐚 surrounds the kernel just as a nutshell surrounds a nut 🥜.

On most Linux systems a program called bash (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, sh, written by Steve Bourne) acts as the shell program. Besides bash, there are other shell programs that can be installed in a Linux system. These include: ksh, tcsh and zsh.Note: As of macOS Catalina (Nov 19), `zsh` is now the default Mac shell.

- Example bash v. zsh
- IS SOMEONE EXPLICITLY DISCUSSING THESE ISSUES?

### Terminal

Terminal is a program that runs a shell. In the past it was a physical device (Before terminals were monitors with keyboards, they were teletypes) and then this concept was transferred into software.

While there are a number of different terminal emulators (Gnome-Terminal, iTerm), they all do the same thing - give you access to a shell session. You will probably develop a preference for one. The purpose of this talk is not to debate or endorse one shell or terminal over another.

### Process

A process is the instance of a computer program that is being executed by one or many threads.

While a computer program is a passive collection of instructions, a process is the actual execution of those instructions. Several processes may be associated with the same program; for example, opening up several instances of the same program often results in more than one process being executed.

## Startup Process

Basic startup process chart

## Resources

[Redhat](https://www.redhat.com/sysadmin/terminals-shells-consoles)
