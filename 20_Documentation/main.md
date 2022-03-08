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

Documentation

- why: overview, examples, and scope for today

- how:
  - tools for nice docs (web-facing, manuals, etc)
  - writing API docs (ie docs for a function)



# Documentation: Principles and Definitions


## What is documentation?

Helps someone use and understand a code or software tool

(cut this)

- The code itself?
  - name of a function and names of its args are a form of doc:
  https://github.com/ahbarnett/sciware/tree/main/12_Functions
- Papers?
- A manual?

Explain _to whom_? Understand _by whom_?


## What documentation are we talking about today?

- User-facing: users (not developers) of your code
  - this includes _your future self_: <6 months you forget how to use own code!
- Text that can be seen without opening a code editor (or reading a journal)
  - eg typing in {\tt ipython}
    ```python
    ?range
    ```

    (give output). Called inline doc

  - eg typing in {\tt MATLAB/octave}
    ```matlab
>> help linspace
 LINSPACE Linearly spaced vector.
    LINSPACE(X1, X2) generates a row vector of 100 linearly
    equally spaced points between X1 and X2.
 
    LINSPACE(X1, X2, N) generates N points between X1 and X2.
    For N = 1, LINSPACE returns X2.
 
    Class support for inputs X1,X2:
       float: double, single
 
    See also LOGSPACE, COLON.
    ```


## Won't talk about today, but important:

- writing tests for your code/function
- choosing a good interface (API) for your code/func
- your algorithms :)  (the body of your code)
- good commenting of code
- discussion/documentation of bugs (eg git Issues)
- academic papers showcasing your package


## Types of documentation for today

- API documentation = how to use a given function
  - Ex: docstrings, doxygen, ...
- Basic installation/Getting Started
  - "How to make sure the code"
  - Frequently in a Readme.md on github: the first thing a potential user sees
- More extensive narrative documentation
  - Wikis, compiled manuals, ...
  - More detailed use cases, system design & choices, etc.
- Tutorials/Case Studies
  - Notebooks; also wiki etc.
- Developer documentation (not our audience)


## Audience: Who are you talking to

Documentation isn't there "just because," it should be saying something useful to someone.-

- Messages only have meaning in relation to an audience
- What does your audience want to accomplish?
- What does your audience already know?
- What does your audience need to know?
- What do you need to add to bridge that gap?

Tell your audience things they don't know but can understand


## API Documentation

- "How do I call Function X"
- Audience: People who want to call your software's functionality from their software
  - Assumes an audience that is already invested in using your work
  - (Does little to sell your work to new users)
  - (Not the best way to express the full scope of utility of your code)
- Should describe the functionality you expose
  - What are the inputs and outputs?
  - What are the edge cases? What behavior should happen in those cases?


## API Documentation (cnt'd)

- Advantages:
  - Integrated with code (how so?)
  - (Explain why that's good)
- Limitations:
  - Not a good format for describing things other than local functionality
  - Function-by-function may not be the only or best way to organize/analyze what your code can do
  - You must never confuse lengthiness with completeness! --> This point might belong elsewhere

Insert good and bad function API doc examples.
- make up one. Then give improved one.

<!--
(Ex: psycopg2 (Postgres database adapter in Python) only allows Python tuples for a `WHERE foo IN (%s)` clause,
and only allows Python lists for a `WHERE foo = ANY (%s)`. The two expressions do almost the exact same thing,
but the valid data inputs are in complementary distribution. This is documented as a throwaway in one
sentence of a several-thousand-line API documentation doc.)
-->

- Use any time you're releasing an API for public use


Bad API docs:
https://portal.hdfgroup.org/display/HDF5/HDF5


## The Triangle: API, Test, Documentation

Q: What order should you write these in?
A: Write them all at once!
Good practices are mutually interdependent (I try to make this point every SciWare)

Personally: write doc first, then test, then function body.

## Readmes

- "How do I get and run this package" - link to good example
- Audience:
  - New users of the software
  - People who may be calling your code as a step in a pipeline (rather than interacting with your functions as an API)
- Tells users how to install the package & make sure it works
- Describes some of the functionality but probably only scratches the surface of what your code can do
- Include a minimal usage example, eg:
     https://emcee.readthedocs.io/en/stable/
- Needed for any package, but it's probably only the start

## Narrative Documentation

- "What-all can this package do" to "Tell me technical details about this package", user manual. FINUFFT manual.
   https://emcee.readthedocs.io/en/stable/tutorials/quickstart/

- Audience:
  - More sophisticated users who want to know how to handle the non-modal use case
  - People who want to know more about how your system works
  - People you're trying to convince why they should use your tools at all
- Can include rationale, design decisions, or more sophisticated configurations
- Can include more detailed discussion of how and why to use different features
- Needs additional work to make sure it stays up to date as design decisions change
- Should probably be included for any reasonably mature package


## Tutorials

- "How can I solve ABC using XYZ"
- Audience:
  - All users, from basic to sophisticated uses
  - People who want to know *how to solve a particular problem* rather than *how to use a particular function*
  - Can be a "cookbook", a gallery, or if extensive enough, a way to show exhaustively what your tool can do
  - how to string together may funcs in a package.  Use FINUFFT tutorial.
- Fully worked (and working!) examples
  - Ideally cover the full gamut of what people would want to do with your tool
  - Distinction: Unlike API documentation, this does *not* need to be organized the same way as your implementation/code!
  - Better to focus on typical/paradigmatic *problems* in the field
  - Or use examples from several different fields/subfields, if your tool is more broadly applicable
- It's important not to leave out the middle: it's easy to jump from basic examples to "pet" sophisticated ones but miss a lot of other useful functionality and/or start assuming your audience knows more than they do
- Needs additional work to make sure it stays up to date as your methods/design decisions change
- Include any time you want to maximize the utility of your package
  - Or when your users are from many fields, may not immediately be familiar with your method, or have lots of packages to choose from

Remember: your work only makes a difference if people use it. Science isn't sales, but people spend entire careers re-inventing poorly-publicized wheels. If you want your work to matter, you need to it easy to find, easy to use, and easy to understand, for people across the broadest possible spectrum of disciplines.



# Tools to Generate Documentation

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



# Writing API Documentation (Bob)

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
    - Does the type hint save you or should there be more code?

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
    - return not-a-number because that follows the divide-by-zero
      floating-point arithmetic?
    - throw an exception to help the user by failing early?