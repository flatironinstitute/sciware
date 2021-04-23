# Sciware

## Testing and Packaging

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/14_TestingPackaging


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

- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

- Testing intro and background
- Python exercise



## What is a "test"?

* Something you can run (a program, script, function)
* distinct from your "real" code (unnecessary)
* that runs relatively quickly (while you wait, ideally)
* that executes some portion of your "real" code
* checks that it is doing what you expect
* and returns success if things are good, or some kind of error otherwise.


## We already do some scientific validation
- print statements
- plots or output files midway through

Implementing a "test" formalizes this process


## Motivation for testing

Why are tests important? 
* Lets you know your code is working properly
* Lets others know when they have broken your code
* Formal validation

Protect against:
* Bugs
* Crazy user edge cases
* Constantly changing code base


# Types of Tests 

## Unit Tests
Do all the little bits work?
* Tests of some small "unit" of code, usually a function
* Often augments documentation

### "Doc" test

* A unit test embedded in documentation


## Smoke tests

* A very simple test to make sure things are basically working
* Often run before other tests to determine whether to proceed

## Integration Tests
Does the code run as expected from beginning to end?
- Tests of the interaction between components or the entire system in some real-world-like scenario
- Output file should exist
- Is the output sensible/logical/physically realistic?


## Edge Tests
What unusual cases work?
- unexpected conditions, values (e.g., negative numbers)
- incorrect types, mismatching lengths
- null or missing data 

## Known Failures
What does the code NOT do?


### Regression tests

* *regression*: when something stops working due to a (theoretically unrelated) change
* Often added when fixing bugs, to avoid re-introducing them later

### Performance tests

* Automatically timing some code to make sure it still runs fast enough


### Test-driven development

* The practice of writing tests before code
* For example, a unit test for a function defines the API


### Continuous Integration (CI)

* Automatically running tests for each change/commit



## Strategies for writing tests

### Modularize your code (functions)

* Identify testable components to turn into functions
   * (See earlier sciware on functions)
* Call these functions from both tests and "real" code


### Think about automation

* Write many tests
* Write one script to call all the tests (more later...)

### Validate assumptions

* If some function works for a range of values, choose one at random each time
* Compose any pair of inverse operations (*g* ◦ *f*, `load` ◦ `save`)
* Validate properties that should hold
* Use a less efficient, equivalent calculation to check
* Identify and write down (test) your assumptions



## Workshop exercises

https://flatironinstitute.github.io/learn-sciware-dev/14_TestingPackaging/guide.html
