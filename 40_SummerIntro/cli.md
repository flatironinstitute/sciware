# Sciware

## Intro to the Command Line

https://sciware.flatironinstitute.org/40_SummerIntro/cli.md


## Agenda

- What is a Command Line Interface?
- Navigating the File System: CLI vs GUI
- Why Use a CLI?



# What is a Command Line Interface?

- "CLI" = _command line interface_
    - "keyboard" interface
    - "terminal", "shell", (rarely) "console"
- "GUI" = _graphical user interface_
    - "mouse" or "touch" interface
    - "desktop", "window system"


<img src="assets/cli/desktop-terminal-shell.png" width="100%" style="border:0;box-shadow:none">


### Example Shell Command

<img src="assets/cli/command-line-example.png" width="60%" style="border:0;box-shadow:none" />

- The *prompt* is from the shell (user types the rest)
- The *command* is the program to run
- *options* or *flags* control how command behaves
- *arguments* tell command what to operate on



# CLI and GUI


## Navigating the File System

- *Operating system*: the code that makes the computer hardware work
- *File system*: the part of the OS that:
  - stores data permanently on disk (*files*)
  - and organizes it (into *directories* or *folders*)


- On *Unix*-like systems:
  - File system begins at `/` ("root")
  - Directories separated with `/` character
  - String location is a *path* (`/home/users/NAME`)
- *absolute paths* start with `/`
- *relative paths* don't
  - They're relative to some "current location"


### Where am I?

`pwd` **p**rints **w**orking **d**irectory:

```bash
$ pwd
TKTKTK
```

`ls` **l**i**s**ts what's in this directory:

```bash
$ ls
TKTKTKTK
```


### To follow along...

Clone a git repository:

```bash
$ git clone REPO-TK
$ ls
```


### Going somewhere

`cd` **c**hanges the **d**irectory you're in

```bash
$ cd REPO-TK
$ pwd
$ ls
```


### My neighborhood

- `~` = alias for home directory
- `.` = "the current directory"
- `..` = "the directory above this one" (*parent*)

```bash
$ pwd
TKTK
$ cd .
$ pwd
TKTK
$ cd ..
$ pwd
TKTK
```


### Getting information

`ls` can give more details if you ask:

```bash
$ ls Mainfile.idx
MainFile.idx
$ ls -l Mainfile.idx
-rw-rw-r-- 1 jsoules jsoules 43 Jun  3 14:51 MainFile.idx
```

Those columns are:
- Access permissions
- Link count
- Owner and group of the file
- size of the file
- modification date
- name


- `-a` shows *all* results, including "hidden" files/directories
  - (the ones that start with a `.` character)
```bash
$ ls -a
.     dir2          MainFile.idx   myfile_03.txt  myfile_06.txt  myfile_09.txt  myfile_12.txt  myfile_15.txt  myfile_18.txt
..    .git          myfile_01.txt  myfile_04.txt  myfile_07.txt  myfile_10.txt  myfile_13.txt  myfile_16.txt  myfile_19.txt
dir1  .hidden.file  myfile_02.txt  myfile_05.txt  myfile_08.txt  myfile_11.txt  myfile_14.txt  myfile_17.txt  myfile_20.txt
```


- `-h`: show human-readable sizes
```bash
$ ls -l /usr/bin/chromium-browser
-rwxr-xr-x 1 root root 2408 Sep 18  2020 /usr/bin/chromium-browser
$ ls -lh /usr/bin/chromium-browser
-rwxr-xr-x 1 root root 2.4K Sep 18  2020 /usr/bin/chromium-browser
```


- `-d`: display directories themselves (not their contents)
```bash
$ ls dir1
datafile_1.txt  subdir1
$ ls -d dir1
dir1/
```


- Single-letter flags can be combined:
```bash
$ ls -laht # same as ls -l -a -h -t
$ ls -ahlt # also the same; order usually doesn't matter
$ ls --help # works for many commands
$ man ls # read the manual
```


### Aside: keystrokes

- `tab` auto-completes up to uniqueness
- double-`tab` will show you the possible completions for non-unique values
- Unix is case-sensitive!

```bash
$ ls M # hitting tab will auto-complete MainFile.idx
$ ls m # tab once will give myfile_
$ ls m # tab twice will show the possible completions of myfile_
```


- Up arrow lets you scroll through previous commands
  - `control` and `r` together (`ctrl-r` or `C-r`) lets you search previous commands
- You can then edit those commands by deleting, or moving the cursor with arrow keys

<!-- 
- You can also review your earlier commands with `history`
```bash
$ history | tail -n 10
```
- and rerun a previous command with `!<NUMBER>`
```bash
$ !20032
ls .

``` -->


### Moving and Renaming

- `mkdir` *m*a*k*es a *dir*ectory
- `cp` *c*o*p*ies files 
- `mv` *m*o*v*es files/directories (including to a new name)

```bash
$ mkdir newdir
$ ls
dir1  MainFile.idx   myfile_02.txt  myfile_04.txt  myfile_06.txt  myfile_08.txt  myfile_10.txt  myfile_12.txt  myfile_14.txt  myfile_16.txt  myfile_18.txt  myfile_20.txt
dir2  myfile_01.txt  myfile_03.txt  myfile_05.txt  myfile_07.txt  myfile_09.txt  myfile_11.txt  myfile_13.txt  myfile_15.txt  myfile_17.txt  myfile_19.txt  newdir
$ cp MainFile.idx newdir
$ cp .hidden.file newdir
$ mv newdir newdir2
$ ls -a newdir2
.  ..  .hidden.file  MainFile.idx
```


### Removing

- `rm` *r*e*m*oves files
  - There is NO "TRASH". This deletes the file right away!
- `rmdir` *r*e*m*oves *dir*ectories (only if empty)

```bash
$ rm newdir2
rm: cannot remove 'newdir2/': Is a directory
$ rmdir newdir2
rmdir: failed to remove 'newdir2/': Directory not empty
$ rm newdir2/MainFile.idx
$ rm newdir2/.hidden.file
$ rmdir newdir2
$ ls
dir1  MainFile.idx   myfile_02.txt  myfile_04.txt  myfile_06.txt  myfile_08.txt  myfile_10.txt  myfile_12.txt  myfile_14.txt  myfile_16.txt  myfile_18.txt  myfile_20.txt
dir2  myfile_01.txt  myfile_03.txt  myfile_05.txt  myfile_07.txt  myfile_09.txt  myfile_11.txt  myfile_13.txt  myfile_15.txt  myfile_17.txt  myfile_19.txt
```


- `rm -r` (for "recursive") removes a directory's contents, then the directory itself
- Remember there's NO BACKSIES--only do this if you're sure!


### Spaces Separate Arguments

```bash
$ ls -l myfile_01.txt myfile_02.txt
-rw-rw-r-- 1 jsoules jsoules 0 Jun  3 14:50 myfile_01.txt
-rw-rw-r-- 1 jsoules jsoules 0 Jun  3 14:50 myfile_02.txt
```

- What about files with spaces in them?
- Use quotes or `\` escape character
```bash
$ ls -l dir1/file with spaces.doc
ls: cannot access 'dir1/file': No such file or directory
ls: cannot access 'with': No such file or directory
ls: cannot access 'spaces.doc': No such file or directory
$ ls -l dir1/"file with spaces.doc"
-rw-rw-r-- 1 jsoules jsoules 0 Jun  5 11:45 'dir1/file with spaces.doc'
$ ls -l dir1/file\ with\ spaces.doc # same thing
```



# Words Are Worth a Thousand Pictures


## Globbing

- The `*` character is a *glob*
- It means "expand all the possible completions"

```bash
$ ls *
MainFile.idx   myfile_02.txt  myfile_04.txt  myfile_06.txt  myfile_08.txt  myfile_10.txt  myfile_12.txt  myfile_14.txt  myfile_16.txt  myfile_18.txt  myfile_20.txt
myfile_01.txt  myfile_03.txt  myfile_05.txt  myfile_07.txt  myfile_09.txt  myfile_11.txt  myfile_13.txt  myfile_15.txt  myfile_17.txt  myfile_19.txt

dir1:
 datafile_1.txt  'file with spaces.doc'   subdir1

dir2:
done

$ ls myfile_0*
myfile_01.txt  myfile_02.txt  myfile_03.txt  myfile_04.txt  myfile_05.txt  myfile_06.txt  myfile_07.txt  myfile_08.txt  myfile_09.txt

$ ls m*6*
myfile_06.txt  myfile_16.txt
```


### Printing values

- `echo` prints out its arguments after shell has processed them
- `cat` (for con**cat**enate) prints the contents of the file arguments
- `nano` is a simple text editor
```bash
$ echo myfile_0*
myfile_01.txt myfile_02.txt myfile_03.txt myfile_04.txt myfile_05.txt myfile_06.txt myfile_07.txt myfile_08.txt myfile_09.txt
$ cat MainFile.idx
This is the main file
It contains some txt
$ nano myfile_02.txt
```


### More glob characters

- `*` matches 0 or more characters
- `?` matches exactly one character
- `[1,3,5]` matches *any* of the characters 1, 3, or 5

```bash
$ ls myfile_?6.txt
myfile_06.txt  myfile_16.txt
$ ls myfile_?[1,3,5].txt
myfile_01.txt  myfile_03.txt  myfile_05.txt  myfile_11.txt  myfile_13.txt  myfile_15.txt
```


### Spooky action at a distance

```bash
$ ls dir1/subdir1
processed_22.data  processed_24.data  processed_26.data  processed_28.data  processed_30.data  processed_32.data  processed_34.data
processed_23.data  processed_25.data  processed_27.data  processed_29.data  processed_31.data  processed_33.data
```


### Putting them together

```bash
$ mv dir1/subdir1/processed_* dir2/done/
$ mv myfile_0[1,3,5,7,9]* dir1/subdir1/
$ ls . dir1/subdir1/ dir2/done/
.:
dir1  MainFile.idx   myfile_04.txt  myfile_08.txt  myfile_11.txt  myfile_13.txt  myfile_15.txt  myfile_17.txt  myfile_19.txt
dir2  myfile_02.txt  myfile_06.txt  myfile_10.txt  myfile_12.txt  myfile_14.txt  myfile_16.txt  myfile_18.txt  myfile_20.txt

dir1/subdir1/:
myfile_01.txt  myfile_03.txt  myfile_05.txt  myfile_07.txt  myfile_09.txt

dir2/done/:
processed_22.data  processed_24.data  processed_26.data  processed_28.data  processed_30.data  processed_32.data  processed_34.data
processed_23.data  processed_25.data  processed_27.data  processed_29.data  processed_31.data  processed_33.data
```


This only scratches the surface!

- Tools like `find` and `xargs` can let you:
  - Mass rename thousands of files in a directory structure
  - Selectively move and archive files older than a given time
  - Combine multiple files from different locations into one

and much more



# CLI -- Under the Shell


## Most shell commands are just programs

- `which` tells you the absolute path for a command

```bash
$ which chromium
/snap/bin/chromium
$ /snap/bin/chromium # launches a web browser
```

And that's exactly what happens if you double-click the file in a gui window.


```bash
$ which python3  # this lets me know if I'm in the virtual environment I expect
/usr/bin/python3
```


- Shell interprets commands by checking `PATH` environment variable
  - This is a list of what paths to check
  - See it with `echo`

```bash
$ echo $PATH # $ means "retrieve the value of the variable"
```


## Who Does What

- globs `*` and variable expansion `$VAR` happen in the *shell*
  - The results are *treated as live commands*
  - Expansion happens *before* the values are passed to any command

```bash
$ LSVAR="ls -l"
$ echo $LSVAR  # just prints out the variable's contents
ls -l
$ $LSVAR    # will expand "ls -l" and then try to execute that
total 16
drwxrwxr-x 3 jsoules jsoules 4096 Jun  5 11:46 dir1
drwxrwxr-x 3 jsoules jsoules 4096 Jun  5 14:15 dir2
-rw-rw-r-- 1 jsoules jsoules   43 Jun  3 14:51 MainFile.idx
-rw-rw-r-- 1 jsoules jsoules    0 Jun  5 12:52 myfile_01.txt
-rw-rw-r-- 1 jsoules jsoules   22 Jun  5 14:17 myfile_02.txt
[...]
```


```bash
$ *  # this will expand to everything in the directory then treat those as commands
Command 'dir1' not found, did you mean:
  command 'dirb' from deb dirb (2.22+dfsg-5)
  command 'dir' from deb coreutils (8.32-4.1ubuntu1.2)
  command 'dirt' from deb dput-ng (1.34)
Try: sudo apt install <deb name>

$ myfile*  # matches all the myfile... files, but those files are not executable
bash: ./myfile_01.txt: Permission denied
```

Here the "permission denied" means that the file `myfile_01.txt` does not have
*execution permissions* set on it. If it *did*, the shell would try to execute it.


### This has security implications!

- Dangerous to run something if you don't know what it expands to
- Expanding lists of filenames can cause problems
  - especially if they contain spaces
  - or other special characters that need to be escaped `\`


## Process management

- Running commands are just programs
- The computer can run many programs at once
  - Only one can have the terminal's attention
  - This is the "foregrounded" program
  - (Others may be running in the background)
- Interactive programs include Python, editors...
- Program must end before you launch a new one


### Aside: Essential Control Characters

Keys pressed with the `control` modifier usually have special meanings:

- `ctrl-a` (`C-a`) brings the cursor to the start of the line
- `ctrl-e` (`C-e`) brings the cursor to the end of the line


- `C-k` **k**ills the line through to the end and saves it in a clipboard
- `C-y` **y**anks the cut text back and pastes it

```bash
$ ls -la dir1/subdir1/ [C-a C-k]
$
$ [C-y]
$ ls -la dir1/subdir1/
```


- `ctrl-c` (`C-c`) interrupts an operation in progress
```bash
$ curl parrot.live
[time passes...]
[C-c]
$
```


- `C-d` sends an `end of file` character (ends interactive programs)
```bash
$ python3
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>  [c-d]
$ 
```


- `C-z` backgrounds the current program and returns you to prompt
  - `fg` (**f**ore**g**round) command brings that program back up
```bash
$ python3
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>  [c-z]
[1]+  Stopped                 python3
$ ls
[...]
$ fg
python3
```


- `C-a` move to head of line
- `C-e` move to end of line
- `C-k` cut text
- `C-y` paste text
- `C-c` cancel process
- `C-d` send end-of-file
- `C-z` background process


