# Sciware

## Functions

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/12_Functions


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

- Future sessions planned:
  - Data storage file formats (hdf5, numpy, parquet, sqlite, ...)
- Suggest topics and vote on options in #sciware Slack


## Today's Agenda

- Intro: what is a function? (Alex)
- Designing good functions (Bob)
- Hands-on exercise : extracting a function (Alex)
- Case studies (Joakim)
- Discussion








<!-- AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA -->

<!-- I want default left-justify everywhere:  -->
<style type="text/css">
  .reveal p {
    text-align: left;
  }
 </style>
<!-- see: https://stackoverflow.com/questions/41024596/r-markdown-slides-with-reveal-js-how-to-left-align-list-items-bullets-and-numb/41047550#41047550    -->


## Intro: what is a function? (Alex)

----

Say you have python script/notebook including snippet...

```python
S = 0; T = 0
for i in range(10) :
  S += a[i]*a[i]
for i in range(20) :
  T += b[i]*b[i]
result = S-T
```
<small>Seems to sum the squares of array a, then similar for b, then subtract them.</small>

Good to package the self-contained repeated task as a *function*:
```python
def sumsquares(a):
    """Sum the squares of the elements of a NumPy array."""
    return sum(a*a)
```
Then entire snippet becomes much simpler, *and* easier to read:
```python
result = sumsquares(a)-sumsquares(b)
```
plus other users, and future you, get a useful tool: a function :)


### Functions are sad without tests

```
def sumsquares(a):
    """Sum the squares of the elements of a NumPy array."""
    return sum(a*a)
```
A ("pure") function has inputs (here ``a``), outputs (returned value)
- refers to no global variables
- has no "state" (internal memory). This makes it *testable*.
Never trust a function you wrote but didn't test! Here's a simple tester:
```
import numpy as np
if sumsquares(np.array((3.0,4.0))) == 25.0:
    print('pass')
else:
    print('fail')
```
Every such tester (aka driver, example) *shows a human how to use your function*

<!-- are more elaborate tests, like what if you send it empy, or non-numpy array... -->


### Standing on the shoulders of giants

We rely on other people's functions all the time, eg ``y=sin(x)`` (low-level math lib), ``coeffs=numpy.polyfit(y,x,degree)``.
Good *design* work went into these functions, as docs for latter show:
<img src="pics/polyfit_doc.png">

Note _interface_: three arguments required, plus various optional ones

But you can be a giant too, by writing (& distributing) your own functions!

### Session goals & topics

__I. Get us to package most of our code as functions:__
- breaks tasks in to *separately* testable components
- clean, modular code, leaving scripts/notebooks short and readable

__II. Write functions with good interfaces, and critique them:__
- naming, inputs, outputs, their types, optional args
- testers, documentation
- these are *just as important* as the algorithm ("meat") inside the function
Otherwise no-one will use your functions... and that includes future you!  :(

Call it "good interface design", in sense of API (application programmer interface). Can include *wrapping existing code so it can be called from another language* (eg Python ``y=sin(x)`` actually wraps ``libm`` library)

[Not to be confused with: "interfacing" in sense of UX/UI (user experience), human-computer interfaces, package management (``apt`` etc)...]

Any questions about what we're talking about or goals ?


## Bob



## Jabberwocky demo (Alex)



## Exercise (breakouts)

Choose an examples in [repo](https://github.com/flatironinstitute/learn-sciware-dev/tree/master/12_Functions/exercise)



## Discussion, guides (Joakim)


### Naming


...
