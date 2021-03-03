# Sciware

## Functions

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/13_Debugging


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

- Sciware Office Hours follow-up discussion in 2 weeks
- Advanced testing (test frameworks, strategies, TTD, ...)
- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

* Introduction to debugging: goals and strategies (Jeff Soules, CCM)
* TotalView (Marsha Berger, CCM)
* gdb gui + lldb (Nils Wentzell, CCQ)
* Valgrind & Sanitizers (Nils & Lehman)
* Python debuggers (Lehman Garrison, CCA)


## Terminology

* backtrace, stacktrace: a state of a running/crashed program, the sequence of (nested) function calls leading to the current line of code
* coredump, core file: a file (`/tmp/core.UID-PROG.PID`), produced when a program crashes in certain ways (segfault, `abort()`), if enabled (`ulimit -c unlimited`)
* Heisenbug: a bug that goes away when you try to debug it
* Debugger, interactive debugging: a tool to let you watch your program as it runs, one line at a time
* wolf fence debugging, bisection: finding a bug by recursively dividing your code and seeing which part fails (commenting out lines or reverting some changes)
