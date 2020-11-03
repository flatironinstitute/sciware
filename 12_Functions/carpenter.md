---
title: "**The why, when, and how of functions<br />&nbsp;**"
author: "**Bob Carpenter** <br />CCM<br />&nbsp;"
date: "<small>November 2020</small>"
output: revealjs::revealjs_presentation
---

# Programming is hard

## Programs quickly spin out of control
- users want more features
- research code grows organically idea to idea
- production code is constrained on all sides
- code gets duplicated
- debugging feels hopeless due to scale and combinatorics


## Code goes stale
- REPL code (Python, R, Julia) fails due to lack of context
- external dependencies change (especially in R)
- can't be understood by others or you in the future

## Only one solution to control fear &amp; dread
- first, admit we have a problem
- then, improve a couple simple coding practices
- today, we'll focus on writing **readable code**


# Naming is hard

## Heard on the street
- There are only two hard things in Computer Science: cache
invalidation and naming things. <br />--Phil Karlton <br /> &nbsp;
- There are 2 hard problems in computer science: cache invalidation,
naming things, and off-by-one errors. <br /> --Leon Bambrick <br /> &nbsp;
- Some people, when confronted with a problem, think "I know, I'll use
regular expressions." Now they have two problems. <br /> -- Jamie Zawinski

## Write readable code

## The bad and the good
- Bad:
<pre>
double yx_32;  // transfer constant in ml/s
</pre>
- Better:
<pre>
double transfer_constant;  // in ml/s
</pre>
- Best:
<pre>
double transfer_ml_per_s;
</pre>
- Look ma, no doc.


# Design top down, code bottom up

## Code should be designed for users
- Functional specification is the **what**
- Technical specification is the **how**
- Design functionally top down from user goals
- Flesh out user interfaces in the user's shoes
- Work down to the algorithms needed to code it

## Build code bottom up for developers
- Find small reusable functional units
- Build them, document their interfaces, and test.
- Only then proceed to the next level up.
- Work on manageable units with trustworthy foundations.

## Code changes over time
- But we can't anticipate where it's going well
- Do not overengineer in anticipation of the future
- Instead, write simple reusable chunks of code
- All this takes practice and judgement

# Design, Documentation, and Testing

## The Trinity of Code Development
- After 30+m of struggling with tikz/markdown in <code style="font-size: 85%; font-family:Menlo">reveal.js</code>, I gave up.
-
<pre>
        FEATURES
        /     \
       /       \
QUALITY ---- TIME
</pre>
&nbsp;

- But that's not what concerns us today.

## The Trinity of Function Development

- Code, doc, and testing are inextricably linked
-
<pre>
 DOCUMENTATION
     /    \
    /      \
CODE ------ TESTS
</pre>

- They are different aspects of the same thing
    - documentation provides the **functional specification**---what the code does
    - code **implements the specification**---how it does it
    - tests **verify the code does the right thing**

- Can reify this into "test-driven development"

# Exercises in Specification

## Let's work on some functions
- I'll give you a simple mathematical function
- You think about how it should behave (i.e., the doc)

## Sum

- <code style="font-size: 85%; font-family:Menlo">sum(x, y)</code>
    - <code style="font-size: 85%; font-family:Menlo">x, y</code> are scalars

- <code style="font-size: 85%; font-family:Menlo">sum(v)</code>
    - <code style="font-size: 85%; font-family:Menlo">v</code> is a sequence of scalars

## Did you define ...

- argument types?
- return type and value?
- behavior with NaN inputs?  infinite inputs?
- behavior with zero-length sequence inputs?
- behavior when there's overflow?
- behavior with integers or complex numbers?
- size of number types?


## Sum, revisted

-
<pre>
/**
 * Return the sum of the specified vector of double-precision
 * real-valued scalars.
 *
 * If the vector is empty, return 0.If any elements of the argument is
 * NaN, the result is NaN.  If one or more of the inputs is +infinity
 * and the rest are finite, the result is +infinity.  If one or more
 * of the inputs is -infinity and the rest are finite, the result is
 * -infinity.  If both +infinity and -infinty show up as elements of
 * the argument, the result is NaN.  If the sum exceeds the capacity
 * of a double precision float, the result is +infinity.
 *
 * @param v a vector of scalars
 * @return the sum of the elements of the vector
 */
</pre>

## Or maybe

- Just say it follows IEEE 754 arithmetic and let users look that up.

- What about varying floating point behavior?
    - what we wrote is guaranteed by the spec
    - but the actual value is only given up to some digits of precision

- Maybe there should be an integer/complex/real matrix/complex matrix signatures.


## Mean

- <code style="font-size: 85%; font-family:Menlo">mean(v)</code>
    - <code style="font-size: 85%; font-family:Menlo">v</code> is a sequence of scalars

## Did you...

- Appropriately define boundary condition with size zero input?
    - really helps to get boundaries right to make code flow nicely

## Variance

- <code style="font-size: 85%; font-family:Menlo">var(v)</code>
    - <code style="font-size: 85%; : font-family:Menlo">v</code> is a sequence of scalars

## Did you...

- Make sure to document whether the function implements the maximum likelihood
  (divide sume of squares by length) or unbiased (divide by length -
  1) estimator?
- Make sure to document size 0 and 1 inputs?

# Don't Get Carried Away

## Only abstract as much as you need
- Level of code can't exceed the capabilities of the developers
- It's easy to stray too far into the land of abstraction
- Only put in as much work as the current project demands
- Don't over-engineer for a future you're only imaginging

## Example: Accumulators
<pre style="font-size: 55%; font-family:Menlo">
std::unordered_map&lt;std::string, std::string&gt; id_to_seq_;


int64_t total_bases const {
  int64_t tot = 0;                               // initialize to 0
  for (const auto&amp; id_seq : id_to_seq_)          // visit each element
    tot += id_seq.second().size();               // update value
  return tot;                                    // return value
}


int64_t total_bases() const {
  return std::accumulate(                        // return value
      id_to_seq_.begin(),
      id_to_seq_.end(),                          // visit each element
      0,                                         // initialize to 0
      [](const auto&amp; tot, const auto&amp; id_seq) {
        return tot + id_seq.second.size();       // update value
      }
    );
</pre>

* Generates same optimized code (see: <code style="font-size: 85%; font-family:Menlo">godbolt.org</code>).
* If <code style="font-size: 85%; font-family:Menlo">accumulate()</code> looks fun, look
  up: "foldl" (not a typo), "monad", and "functional programming".
