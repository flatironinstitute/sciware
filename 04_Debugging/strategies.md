# Debugging Strategies and Tools

## Sciware Session #4

[https://github.com/flatironinstitute/learn-sciware-dev](https://github.com/flatironinstitute/learn-sciware-dev/tree/master/04_Debugging)


# Goals for Today 



# Debugging Strategies

## [The Art of Software Testing, 3rd Edition](https://www.amazon.com/Art-Software-Testing-Glenford-Myers-dp-1118031962/dp/1118031962)  
by Glenford J. Myers, Corey Sandler, Tom Badgett  
Chapter 8 Debugging



# Debugging Can Be Unplesant

- Bugs represent mistakes and an ego hit
- Debugging is mentally taxing and tiring
- Debugging can take you down rabbit holes
- You probably weren't taught helpful strategies to help



# Error-Locating Principles


### Think. Without looking at the code. 
  - Review in your mind how the program is designed and how it *should* be performing 
  - Concentrate on the process for correct performance, and then magine ways in which the code may be incorrectly designed


### Sleep on It

- The human subconscious is a potent problem solver.
- If error is not located in approximately 30 mins, set it aside and do something else
- If solution arises while sleeping, capture it with a recording before going back to sleep


### Describe Problem to Someone Else

- Talking to someone else may lead to the solution without any verbal assistance from the listener.


### Use Debugging Tools Cautiously

- Debugging tools need to be used in conjunction with problem solving strategies


### Experimentation is a Last Resort

- A haphazard approach is inefficient and could result in compounding the problem by introducing new errors



# Error Repairing Techniques


### Errors Tend to Cluster

- When repairing an error, examine its immediate vicinity for anything else which looks suspicious.


### Fix the Error, Not the Symptom

- Be careful to find all instances of an error, not just the one causing failing right now


### Bug Fixes Are Often Wrong

- Corrections are more error prone than original code and should be tested more rigorously 
- Regression testing is important to help catch new errors potentially introduced by bug fixes

<img src='https://imgs.xkcd.com/comics/fixing_problems.png' height='400'>  
([xkcd #1739](https://xkcd.com/1739/))



# Debugging Methods

- Use induction or deduction to form hypotheses
- Eliminate and/or refine possible hypotheses
- **Prove** the hypothesis
- Fix the error
- **Run regression tests**


## Debugging by Testing

Two types of test cases:
- *for testing*: to expose previously undetected error  
   Can cover many conditions with a small number of test cases
- *for debugging*: to provide information useful in locating suspected error  
   cover only a single conditon in each test

As you track down bugs, write more tests!

# Learn from Mistakes
<section class="align-top" style="top: 387.5px; display: block;">   
</section>

- When and where was the error made?
- Who made the error?
- What was done incorrectly?
- How could the error have been prevented?
- Why wasn't it detected earlier
- How could it have been detected earlier?
