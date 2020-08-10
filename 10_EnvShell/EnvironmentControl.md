<!-- Working file for setting up slides dealing with environment control that works with my
     existing reveal.js setup -->
### Environment control

<!-- - Shell variables, export, env -->
<!-- - Basic $VAR expansion -->
<!-- - Source, dot (vs. +x) -->
<!-- - Startup files -->
<!-- -- Default cluster bashrc -->
<!-- - Environment management -->
<!-- - Modules -->
<!-- - Conda/venv activate -->
<!-- - Manual sourcing -->

---

#### Shell variables
- Similar to local variables - set for current shell, don't persist in child processes
- Conventionally lower case ($history, $path, $aliases, etc.)
- Can list via a bare `set` command (depending on shell/mode, will print environment variables as well)
- Can delete with `unset var` command
```
$ fi="the best"
$ echo "flatiron is... $fi"
flatiron is... the best
$ sh
sh-4.2$ echo "flatiron is... $fi"
flatiron is...
```

---

#### Environment variables
- Persist through to child processes
- Conventionally upper case ($PATH, $HOME, etc.)
- Can list via a bare `export` or `/usr/bin/env` command
- Set with `export` command
- Can delete with `unset` command
- Set only for a child process by prepending
```
$ MY_ENV_VAR="Environment fun!" echo "Woo! $MY_ENV_VAR"
Woo! Environment fun!
$ echo "Woo! $MY_ENV_VAR"
Woo!
$ export FI="the GOAT"
$ echo "flatiron is... $FI"
flatiron is... the GOAT
$ sh
sh-4.2$ echo "flatiron is... $FI"
flatiron is... the GOAT
```

---

#### Variable expansion
- `foo=bar`, `file=mydata.csv`
- Concatenate: `${foo}stool` -> `barstool`
- Remove prefix: `${file##*.}` -> `csv`
- Remove suffix: `${file%%.*}` -> `mydata`
- Substitute prefix: `${file/#*./data.}` -> `data.csv`
- Substitute suffix: `${file/%.*/.bin}` -> `mydata.bin`
- Brace expansion: `{1..10..2}` -> `1 3 5 7 9`

---

#### Executing shell scripts: `source`, `.`, and `chmod +x`
- `source myscript.sh` and `. myscript.sh` will _generally_ execute the script in the current shell
-- all variables set in the file will persist in your shell after execution is complete
-- `source` and `.` are handled differently in different shells, depending on the mode, but are largely identical for most purposes
- Making a script executable via `chmod` and executing via `./myscript.sh` will execute the script in a child process, and the variables will **not** persist into your current shell

---

#### Startup files
- `zsh`: `/etc/zprofile`, `.zprofile`, `.zshrc`
- `bash`: `/etc/profile`, `.profile`, `.bash_profile`, `.bashrc`, 
- 'profile' files executed only on __login__ shells (e.g. `ssh`, `bash --login`), and should typically contain only environment variable definitions. It's common to source the relevant 'rc' file here.
- 'rc' files executed only on __interactive__ shells. Used for everything else (aliases, functions, bash/zsh variables, etc). 
- Avoid issues with `scp`: in 'rc' file `[ -z "$PS1" ] && return`

---

### Environment Management

---

#### Modules

---

#### Conda/venv

---

#### Manual sourcing
