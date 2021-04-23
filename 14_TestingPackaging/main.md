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


## Feedback



# Previous testing session slides

## We already do some scientific validation
- print statements
- plots or output files midway through

Implementing "test" formalizes this process


## Example: Crossmatch two lists of fast moving astro objects with sky locations from different decades
- Read in coordinates columns from List #1
- Forecast coordinates of List #1 to date of List #2
- Choose objects from from List #2 with closest to coords to forecasted List #1
- Output matched List with all columns from both lists


# Types of Tests 
- **Integration** - Does the code run as expected from beginning to end?
- **Acceptance/Scientific** - Is the output logical and/or physically realistic?
- **Unit** - Do all the little bits work?
- **Edge** - What unusual cases work?
- **Known Failures** - What does the code NOT do?


## Software Integration Tests
Does the code run as expected from beginning to end?
- Output file should exist
- Output file should be a CSV


## Acceptance/Scientific Integration Tests
Is the output logical and/or physically realistic?
- Number of lines in output matched list should be the same as in List #1
- Characteristics from List #1 and #2 should be similar for matched objects (e.g., faint matched with faint)
- Sample characteristics of List #1 and output matched list should be similar


## Unit Tests
Do all the little bits work?
- Test coordinate forecast method
- Test finding closest coords method


## Edge Tests
What unusual cases work?
- Make a test List #1 with "edge" cases.
## Edges
- objects which didn't match the first time
- objects where closest match isn't correct one
- objects with null or missing data 


## Known Failures
What does the code NOT do?
- objects with insufficient data to test if closest match is the best one
- objects with large uncertainties on location


## Activity: Think of one of each type of test relevant to your current work
- **Software Integration** - Does the code run as expected?
- **Acceptance/Scientific Integration** - Is the output logical and/or physically realistic?
- **Unit** - Do all the little bits work?
- **Edge** - What unusual cases work?
- **Known Failures** - What does the code NOT do?



## What is a "test"?

* Something you can run (a program, script, function)
* distinct from your "real" code (unnecessary)
* that runs relatively quickly (while you wait)
* that executes some portion of your "real" code
* and checks that it is doing what you expect
* and returns success if things are good, or some kind of error otherwise.


## Debugging assertions

Many languages provide some kind of `assert`:

```python
def assert(expr):
    if __debug__:
        if not expr: raise AssertionError
```

```c
#ifndef NDEBUG
#define assert(expr) if (!expr) abort()
#endif
```


```python
x = load_file("input")

y = process(x)

write_file("output", y)
```

A very simple kind of "test" inserts checks into an existing code flow


```python
x = load_file("input")
assert(len(x) == 345)
y = process(x)
assert(len(y) < len(x) and y[0] > 0)
write_file("output", y)
```

This validates some assumptions, but isn't very flexible (hard-coded input)


Instead, write a separate test with hard-coded data:

```python
x = [...]
y = process(x)
assert(len(y) < len(x) and y[0] > 0)
```


## Motivation for testing
##### (from Rosetta tutorials)

Why are tests important? 
* Lets you know your code is working properly
* Lets others know when they have broken your code
* Formal validation

Protect against:
* Bugs
* Crazy user edge cases
* Constantly changing code base



## Strategies for writing tests

Real-world code is more complicated

```
G0 = 100
G1 = 200
global_data = load_file("globals")
z = 0

for i in 1:120
    x = load_file(str(i)+"/input")
    z += f(x)/G0
    y = g(G1, x, z)
    write_file(str(i)+"/output", y)
end
```


### Modularize your code (functions)

* Identify testable components to turn into functions
   * Chunk of calculations 
   * Body of for loop
   * Pass all inputs as arguments, return outputs
   * Look for similar (repetitive) parts of code (mode argument)
* Anything you're not sure about, tricky
   * That you might try separately, interactively, in a debugger or REPL
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



## Boring Terminology


### Unit tests

* Tests of some small "unit" of code, usually a function
* Often augments documentation

#### "Doc" test

* A unit test embedded in documentation


### Smoke tests

* A very simple test to make sure things are basically working
* Often run before other tests to determine whether to proceed


### Integration, System, Acceptance tests

* Tests of the interaction between components or the entire system in some real-world-like scenario


### Regression tests

* *regression*: when something stops working due to a (theoretically unrelated) change
* Often added when fixing bugs, to avoid re-introducing them later

### Performance tests

* Automatically timing some code to make sure it still runs fast enough


### Test-driven development

* The practice of writing tests before code
* For example, a unit test for a function defines the API
* May be written as a "TODO" for things to be implemented

* Coding with the end in mind
* Determine requirements for "working" code
* Write tests that assert these requirements based on an interface
   * Requirement: `f(2)` always returns 4
   ```
   assert f(2) == 4
   ```
* Implement functions
* Check function passes the test


### Continuous Integration (CI)

* Automatically running tests for each change/commit


## CI: Test Automation

Integration with github and other repositories to automatically run tests

### [Travis-CI](https://travis-ci.org/)

`.travis.yml`:
```yaml
language: python
```

### [Jenkins](https://jenkins.flatironinstitute.org/)


