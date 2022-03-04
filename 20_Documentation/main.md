# Sciware

# Documentation
### How to win users and influence science

https://github.com/flatironinstitute/sciware/tree/main/20_Documentation


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


# Tools to Generate Documentation


## Tools to Generate Documentation

- Let's break "documentation" into two categories
    - **Narrative** documentation: high-level, "instruction manual" prose
    - **API** documentation: granular technical specifications


## Tools for Narrative Documentation
- In order of increasing feature-richness and complexity
    - The `README`
    - Wiki
    - Jekyll + static web hosting (e.g. GitHub Pages)
    - Sphinx + ReadTheDocs


## Narrative Documentation: the `README`
- The simplest form of top-level documentation
- Highly portable, easily rendered into a webpage or read in a terminal
- Often where you will start documentation—don't underestimate the usefulness!
    - Great idea to jot down the steps to run your code in a `README` as soon as you start
    - We all promise ourselves we'll set up beautiful documentation later, but in case that doesn't happen, a `README` is a lifesaver
- GitHub and other code hosting sites will render your `README`


## Formatting the `README`
- Two popular languages to make your plain-text `README` look nice online:
    - Markdown (`README.md`)
    - reStructuredText (`README.rst`)
- Either one will help you render text

<img width="40%" src="assets/raw_readme_md.png" class="plain">
<img width="30%" src="assets/rendered_md.png" class="plain">



# Writing API Documentation

## The doc/test/code triangle

- When desiging a function, consider together
    1. **Documentation**: says what the code does
	2. **Testing**: tests it does what it says it does
	3. **Code**: the code itself
- Bad smells
    - if code is hard to doc, it's probably badly designed
    - if code is hard to test from the doc, either the code is badly
      designed or the doc is incomplete

## Exercise 1

1. In your favorite language, design a function to sum a sequence of
numbers.
2. Write documentation for it.
3. Can you write tests for it looking only at the doc?

```python
import numpy as np
def mySum(v: np.array) -> np.float64:
```

## Answer 1: Documentation

Things to document:

1. argument type and shape assumptions
2. return type
3. result when argument is empty
4. error conditions and behavior

# Answer 1: Tests

* What do we test?
    - throw the appropriate exception when argument is wrong shape
    - when arg is empty, return 0 (unit under addition is always the base value)
	- length 1 input, and at least one longer input
    - behavior when one or more arguments is not-a-number or infinite?
    - behavior when no argument is given?

# Answer 1: Code

- I've included typehints, but these could be documented some other way

```python
import numpy as np
def mySum(v: np.array) -> np.float64:
    """Return the sum of the elements of v or 0 if v is size 0.

    Arguments:
    v -- array to sum

    Exceptions:
	RuntimeError if v is not a one-dimensional array.

    Return:
    Sum of the elements of v, or 0 if v is empty.
	"""
    if len(v.shape) != 1:
        raise RuntimeError('Require 1D array argument') from None
    sum = 0
    for n in range(v.size()):
        sum += v[n]
	return sum
```


## Thought Exericse 2

- Consider how the above code might break with different type
arguments.
    - Does the type hint save you or should there be more code?

- Consider generalizing `mySum` to deal with different type and
different shape arguments.
    - How does the doc differ?
    - Will it be enough to base testing on?

## Thought Exercises 3, 4

- Consider writing a function `myAvg` to calculate the average of an array.
    - How much different is this than `mySum` in terms of code?
    - How does the documentation differ?
    - How will testing differ?

- Do the same for `mySD` that calculates the standard deviation of an array.

## Exericse 3, 4: Answers

- The main difference is that `myAvg` is not well defined for
zero-length inputs.
- Did you decide to
    - return not-a-number because that follows the divide-by-zero
      floating-point arithmetic?
    - throw an exception to help the user by failing early?

- `mySD` has two standard definitions
    - divide by `size` is the maximum likelihood estimate
    - dividing by `size - 1` gives an unbiased estimate
    - how do these affect the code and doc?
