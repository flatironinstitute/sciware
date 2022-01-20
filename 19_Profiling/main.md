# Sciware

## Finding Where Your Code Spends Time
### Performance Troubleshooting and Profiling

https://github.com/flatironinstitute/sciware/tree/main/19_Profiling


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
- OK to break in for quick, clarifying questions.
- Use Raise Hand feature for new topics or for more in-depth questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted on #sciware Slack.
- Please keep questions for the speaker in the Zoom chat.


## Future Sessions

- Suggest topics and vote on options in #sciware Slack


## Today's agenda

- Intro
- Time
- Python
- Julia
- C



# Profiling Intro

### Dylan Simon


- We always want everything to take less time
- Need a way to quantify "less". And measure "time".
- It's easy to figure out how much time something takes... right?

<img width="80%" src="assets/clock-time.jpg">


## "Wall time"

- Useful baseline measure
- Can compare changes (algorithms, dependencies, architectures, anything...)
- Which parts take time?
- What if it takes weeks?
- Wall time is a noisy measure


## Profilers

- Tools to break down which parts of your code take time
   - Program: entire run of executable
   - Function: time how long each function takes, how many times
   - Line of code
   - Machine instruction
- Each of these can run multiple times
   - total time, number of executions, average time/execution


## Strategies

- Is this what I expected?
   - Is this part running too many times?
   - Do the counts make sense (think about loops, sanity check)?
   - Are unexpected parts slow?
- Can this be faster?
- Is this necessary?
- Calculation *has* to take time...


## Bite-sized pieces

- Break calculations into smaller pieces
   - Smaller data sets, fewer loops
- Profiling doesn't require getting results, just running code
- Can use smaller profiling results to infer longer run times (multiply!)
- Heisenberg: code when observed, runs slower


## Time units

- "Wall time" = time
- "CPU time" = cpu cores * time
   - Multiple threads
   - 1 core for 1 second + 8 cores for 5 seconds + 1 core for 2 seconds = 43 cpu seconds, 8 wall seconds
   - "CPU hours": cluster usage (allocated, may be idle), 130k cores = 1.1B cpu hours/year



# Simple timing

### Lehman Garrison



# Python profiling

### Robert Blackwell



# Julia profiling

<h3 style="color:#7e588aff">James Smith (CCQ)</h3>



# C profiling

## with gprof

### Dylan Simon


## Building

- Compile and link all files with `-g -pg`
- Better to disable optimization (no `-O`)
- Works with `gcc`, `g++`, `gfortran`, `clang`, `clang++`


## Running

- Run your program normally to produce `gmon.out` (must not be killed/crash)
- `GMON_OUT_PREFIX=foo ./myprog` produces `foo.PID`
- Analyze with: `gprof myprog gmon.out`

[*Example*](gprof_example)



## Alternatives

- oprofile (full system)
- vtune (processor stats)
- ...
- what do you use?


# Questions


# Survey

