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

- Always want code to run faster
- First step is finding what takes time
- "What": instruction, LoC, function, executable
- How often, how many times vs. how much time
- (Something *has* to take time, so that's not necessarily a bad thing)
- "Can this be faster?"
- "Is this necessary?"
- Also useful is this doing the right thing (being called as expected)
- Heisenberg: runs slower


## Time



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

