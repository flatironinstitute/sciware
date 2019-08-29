# Debugging Strategies and Tools

## Sciware Session #4

[https://github.com/flatironinstitute/learn-sciware-dev](https://github.com/flatironinstitute/learn-sciware-dev/tree/master/04_Debugging)


# Flatiron Reveal js theme

## Available for everyone to use!
<div class="spacer"></div>
<div class="spacer"></div>
Instructions here:  
https://flatironinstitute.github.io/learn-sciware-dev/Theme_Demo/
<div class="spacer"></div>
<div class="spacer"></div>
**Thanks Liz Lovero!**


# Next Time

- Sept 26 **or** Oct 3<div class="spacer"></div>
- Thurs, 3--5 pm<div class="spacer"></div>
- Advanced Testing **or** HPC Cluster Intro<div class="spacer"></div>
- Location TBD
<div class="spacer"></div>
<div class="spacer"></div>
**Let's discuss on #sciware Slack channel**



# Goals for Today 

**Foster an environment which encourages participation across experience levels, coding language fluency, technology choices, and scientific disciplines.**
<div class="spacer"></div>

- Avoid discussions between a few people on a narrow topic<div class="spacer"></div>
- Provide time for people who haven't spoken to speak/ask questions<div class="spacer"></div>
- Work together to make discussions accessible to novices


# Schedule

About 15 mins each<div class="spacer"></div>

- **Overview of Debugging Strategies** - Kelle Cruz, CCA <div class="spacer"></div>
- **System Tools** - Dylan Simon, SCC <div class="spacer"></div>
- **Pycharm Debugging Tools** - Tibi Tesileanu, CCB <div class="spacer"></div>
- **Emacs and gdb (C++)** - Nick Carriero, SCC <div class="spacer"></div>
- **gdb web frontend (C++)** - Nils Wentzell, CCQ <div class="spacer"></div>
- **C++/LLVM Sanitiziers** - Olivier Parcollet, CCQ 



# Debugging Strategies

## [The Art of Software Testing,    3rd Edition](https://www.amazon.com/Art-Software-Testing-Glenford-Myers-dp-1118031962/dp/1118031962)  
by Glenford J. Myers, Corey Sandler, Tom Badgett  
<div class="spacer"></div>
<div class="spacer"></div>
**Chapter 8 Debugging**



# Debugging Can Be Unpleasant

- Bugs represent mistakes and an ego hit<div class="spacer"></div>
- Debugging is mentally taxing and tiring<div class="spacer"></div>
- Debugging can take you down rabbit holes<div class="spacer"></div>
- You probably weren't taught helpful strategies to help



# Error-Locating Principles <!-- .slide: class="center" -->


## THINK. 
### Without looking at the code.  <div class="spacer"></div>
 - Review in your mind how the program is designed and how it *should* be performing  <div class="spacer"></div>
 - Concentrate on the process for correct performance, and then imagine ways in which the code may be incorrectly designed


## Sleep on It  <div class="spacer"></div>

- The human subconscious is a potent problem solver.  <div class="spacer"></div>
- If error is not located in approximately 30 mins, set it aside and do something else  <div class="spacer"></div>
- If solution arises while sleeping, capture it with a recording before going back to sleep


## Describe Problem to Someone Else <div class="spacer"></div>

- Talking to someone else may lead to the solution without any verbal assistance from the listener.


## Use Debugging Tools Cautiously 

- Debugging tools need to be used in conjunction with problem solving strategies
<div class="spacer"></div>
<div class="spacer"></div>
<div class="spacer"></div>
<div class="spacer"></div>

## Experimentation is a Last Resort

- A haphazard approach is inefficient and could result in compounding the problem by introducing new errors



# Error Repairing Techniques <!-- .slide: class="center" -->


## Errors Tend to Cluster

- When repairing an error, examine its immediate vicinity for anything else which looks suspicious.
<div class="spacer"></div>
<div class="spacer"></div>
<div class="spacer"></div>
<div class="spacer"></div>

## Fix the Error, Not the Symptom

- Be careful to find all instances of an error, not just the one causing the failing right now


## Bug Fixes Are Often Wrong

- Corrections are more error prone than original code and should be tested more rigorously 
- **Regression testing** is important to help catch new errors potentially introduced by bug fixes

<img src='https://imgs.xkcd.com/comics/fixing_problems.png' height='400'>  
([xkcd #1739](https://xkcd.com/1739/))



# Debugging Methods

- Use induction or deduction to form hypotheses  <div class="spacer"></div> 
- Eliminate and/or refine possible hypotheses   <div class="spacer"></div>  
- **Prove** the hypothesis  <div class="spacer"></div>  
- Fix the error  <div class="spacer"></div>  
- **Run regression tests**


## Debugging by Testing

Two types of test cases:
- *for testing*: to expose previously undetected error  
  Can cover many conditions with a small number of test cases <div class="spacer"></div>  
- *for debugging*: to provide information useful in locating suspected error  
  cover only a single condition in each test<div class="spacer"></div>
<div class="spacer"></div>

**As you track down bugs, write more tests!**



# Learn from Mistakes

- When and where was the error made? <div class="spacer">
- Who made the error? <div class="spacer">
- What was done incorrectly? <div class="spacer">
- How could the error have been prevented? <div class="spacer">
- Why wasn't it detected earlier? <div class="spacer">
- How could it have been detected earlier? <div class="spacer">
