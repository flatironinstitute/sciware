# Sciware

## Data Types and Typing for Writing Better Code

https://sciware.flatironinstitute.org/24_Types

https://github.com/flatironinstitute/learn-sciware-dev/tree/main/24_Types


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

- Dedicated Zoom moderator to field questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Future Sessions

- Planning for the next few months:
   - Modern C++ (Oct 13?)
   - File formats, data management, hdf5 (Nov)
- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda

- Numeric types, performance
- Thinking about types: concepts, syntax
- Types in python: mypy



# Bits & Representation
## or When Bits can Byte You

When do you need to worry about types of numeric data in your code?

Lehman Garrison (SCC, formerly CCA)


## Numeric Data Types

* In scientific computing, we often deal with numeric data: floats and ints
* Don't always need to think about how these are represented by the computer
  * Often, the computer just does the Right Thing
* But sometimes it doesn't...


## When Do You Need To Worry?

* Broadly two categories of when you might worry about types of numeric data
  * Performance
  * Correctness


## Types and Performance

* Consider an array of 32-bit floats vs 64-bit floats:

```python
a32 = np.ones(10**9, dtype=np.float32)
a64 = np.ones(10**9, dtype=np.float64)
```

* Each 32-bit float takes up 4 bytes, and 64-bit 8 bytes
* 32-bit has ${\sim}10^{-7}$ fractional precision; 64-bit has ${\sim}10^{-16}$
* Total sizes are 4 GB and 8 GB:

```python
>>> print(a32.nbytes/1e9)
4.0
>>> print(a64.nbytes/1e9)
8.0
```


## Types and Performance

* How long to multiply each array by a scalar?

```python
>>> %timeit 2*a32
1.1 s ± 2.09 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
>>> %timeit 2*a64
2.2 s ± 2.84 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

* For simple arithmetic operations, memory bandwidth usually limits the performance
  * As opposed to, e.g., CPU speed
* Using a narrower dtype can be an easy 2x performance gain


## Types and Performance

* What about a more complex operation?

```python
>>> %timeit np.sin(a32)
1.5 s ± 4.77 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
>>> %timeit np.sin(a64)
9.12 s ± 19.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

* Using 32-bit was 6x faster in this case
* Factor 2x is often a good first estimate of potential speedup by halving the type width
  * Speedup might be more, might be less
  * Generally the relationship between type and performance is complex (see next slide)


## Performance

* Processors come with (short) vector units: AVX2, AVX512, ...
* A single processor operation is multiple math operations! 
* CPU Performance: single (fp32) vs double (fp64) precision
   * GROMACS: hybrid (fp32+fp64) vs fp64: **+40%**
* GPUs specs show how type selection affects performance
<img src="assets/a100.png" width="750" style="border:0;box-shadow:none">

   * LAMMPS+GPU: on single node, fp32 vs fp64: **+28%**


## Types and Correctness

* Why not use 32-bit floats all the time?
  * When you need the accuracy of 64-bit

```python
>>> np.float32(10**8 + 1) - np.float32(10**8)
0.0  # where did the 1 go?
```

```python
>>> np.sin(np.float32(np.pi))
-8.742278e-08  # not bad
>>> np.sin(np.float32(np.pi * 100000))
-0.015358375  # way off!
>>> np.sin(np.float64(np.pi * 100000))
-3.3960653996302193e-11  # much better (*)
```

* \* 64-bit works better here, but it's still good practice to ensure the arguments to trig functions are small


## Type Coercion

* Use `arr.dtype` to check the types of Numpy arrays

```python
>>> print(a32.dtype)
float32
>>> print((np.float64(2.)*a32).dtype)
float32
>>> print((a64*a32).dtype)
float64
```

* Use `arr.astype(dtype)` to forcibly cast an array to the type you want
* See [Numpy doc on automatic type conversion rules](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html)
* Use Python's builtin `type()` to check the result type of operations with native `float` and `int`


## Summary of Bits & Representation

* Using smaller types for numeric data can speed up your code
  * Most common conversion is to use `float32` instead of `float64`
* But smaller types can result in less accurate calculations
* Important to have tests in place before modifying your code's types!
* Formal [numerical stability](https://en.wikipedia.org/wiki/Numerical_stability) analysis may help you understand how your application will behave too (look for a session at FWAM)


## References & Further Reading

* [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754): the standard bit representation of floats
* [Roofline model](https://en.wikipedia.org/wiki/Roofline_model) for understanding performance
* [Intel Intrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html) for looking up the CPU cycle cost of instructions
* [Numerical stability](https://en.wikipedia.org/wiki/Numerical_stability) article on Wikipedia
* [Numpy doc](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html) on automatic type conversion rules
* [Kahan summation](https://en.wikipedia.org/wiki/Kahan_summation_algorithm) for reducing numerical error in sums of many floats



# Type concepts

### Dylan Simon (SCC)


# Type concepts

* *Not* type theory (a branch of mathematics involving propositional logic and category theory)
* Abstract tools to approach coding a bit differently
* "algebraic data types"
* Fun with math, set operations, combinatorics


### Motivation: dimensional analysis

* In calculations, units can often be used to find mistakes: \\(\frac{\texttt{mass}}{\texttt{time}^2} \ne \texttt{force} \\)
* Distinguishing different types of data (e.g., input, output) can help automatically detect coding mistakes

```python
def process(x0):
    x1 = step(x0)
    return x0
```


## Types

* So far we've been talking about storage and performance, bits:
   * `float`, `double`, `int32`, `string`
   *  `complex`, `struct`, `class`, `list` (of what?)
* Types are really about the values these bits represent
* Useful for thinking abstractly about your data (not the algorithm or implementation)


So what is a type?


## A type is a *set of values*

Think of a type as representing a set of possible values:

$$
\begin{align}
	\texttt{Bool} &= \\{\textsf{FALSE}, \textsf{TRUE}\\} & \left|\texttt{Bool}\right| &= 2 \\\\
	\texttt{UInt8} &= \\{0,1,\dots,255\\} & \left|\texttt{UInt8}\right| &= 2^8 \\\\
        \texttt{Int32} &= \\{-2^{31},\dots,2^{31}-1\\} & \left|\texttt{Int32}\right| &= 2^{32} \\\\
\end{align}
$$

By saying \\( x \\) has type \\( T \\) we mean
$$ x \in T $$

* \\( \left|T\right| \\) is the number of possible values in \\( T \\) (the *cardinality*)


## Common numeric types

$$
\begin{align}
        \texttt{Int} &\approx \mathbb{Z} \qquad \text{(integers)} \\\\
        \texttt{Float} &\approx \mathbb{Q} \approx \mathbb{R} \qquad \text{(rationals, reals)} \\\\
	\texttt{Float32} &\approx \pm 10^{\pm 38} \text{ with 7 digits} \\\\
	\left|\texttt{Float32}\right| &\le 2^{32} \\\\
	\left|\texttt{Float64}\right| &\le 2^{64}
\end{align}
$$

* Practically, cardinality is always finite (computers have finite memory)
* We may define types with infinite cardinality, but always countably infinite!


## A set of values you choose

No need to limit yourself to established types!

$$
	\\{1,2,3\\} \qquad
	\\{\textsf{YES}, \textsf{NO}, \textsf{MAYBE}\\} \qquad
	\\{\textsf{RED}, \textsf{GREEN}, \textsf{BLUE}\\} \\\\
	\mathbb{Q} \cap [0,1] ~ (\\{x \in \mathbb{Q} : 0 \le x \le 1 \\}) \\\\
	\mathbb{P} \qquad
	\mathbb{Q}^+ \\\\
	\texttt{Float} - \\{ \pm\textsf{Inf}, \textsf{NaN} \\} \quad
	(T - S = T \setminus S = \\{ x \in T : x \notin S \\})
$$

* Many languages represent "finite" data types with labeled values as *enumerations*


## Special types

A couple simple types may seem silly but are quite useful:

$$
\begin{align}
	\texttt{Unit} &= \\{()\\} & \left|\texttt{Unit}\right| &= 1 \\\\
	\texttt{Void} &= \emptyset = \\{\\} & \left|\texttt{Void}\right| &= 0
\end{align}
$$

* `Unit` is the singleton type with only one possible value (`None` in python, `Nothing` in Julia)
* `Void` is the empty type with no possible values (impossible, a value that can never exist, the return value of a function that never returns)
   * `Never`, `void` in C?


## Why is this useful?

Documentation, optimization, error checking, logic!

```python
def compute(order ∈ {1,2,3}):
  if order == 1: ...
  elif order == 2: ...
  else: ... # order == 3
  #if order == 0 (ERROR?)
```

* Can be helpful for describing and thinking about code even if the types are not perfectly represented in the programming language
* Once a variable has a type, its value must be in that type


## Type syntax

Different languages use a variety of syntax to represent types

| \\( x \in T \\)             | languages          |
|--------------------|--------------------|
| `x: T`, `x: int`   | Python, TypeScript |
| `x :: T`, `x::Int` | Haskell, Julia     |
| `T x`, `int x`     | C, C++, Fortran 77 |
| `T :: x`, `integer :: x` | Fortran 90   |


## Adding types: Unions

Sometimes we want to allow different types of values, so we make a new type by combining other types with a union:

$$
\begin{align}
	\texttt{Bool} \cup \texttt{Unit} &= \\{\textsf{FALSE}, \textsf{TRUE}, ()\\} \\\\
	\texttt{Int8} \cup \texttt{Int32} &= \texttt{Int32} \\\\
	(\texttt{Int8} \subset \texttt{Int32})
\end{align}
$$

* Set unions are not particularly useful, as they can usually be represented by a different type
   * C `union`
* Instead...


## Sum types (disjoint unions)

Just like a union, but keeps all values (not just distinct)

$$
\begin{align}
	T + S &= T \sqcup S \\\\
	\texttt{Bool} + \texttt{UInt32} &= \\{\textsf{FALSE},\textsf{TRUE},0,1,2,\dots\\} \\\\
	\texttt{UInt8} + \texttt{UInt32} &= \\{0_8, 1_8, \dots, 255_8, 0_{32}, 1_{32}, \dots\\} \\\\
	\left|T + S\right| &= \left|T\right| + \left|S\right|
\end{align}
$$

* Sometimes called a "tagged" union because values are tagged by which type they're from
* "discriminated": each value is either from `T` or `S` (and you can tell)


## Type parameters, more syntax

* Types can have parameters (arguments) of other types
* \\(+\\) is an operator (function) that builds existing types into a new one: \\( T+S = \texttt{Union}(T,S) \\)
* Syntax for type parameters (and unions):

| \\( T + S \\)      | language          |
|--------------------|--------------------|
| `Union[T,S]`   | Python |
| `T\|S` (`Union<T,S>`)    | TypeScript |
| `Union{T,S}`  | Julia |
| `variant<T, S>`    | C++ |
| `Either T S`  | Haskell |


## Other simple types

* Adding \\( \texttt{Unit} \\) to a type is often useful

$$
	\texttt{Unit} + \texttt{T} = \\{(), \dots\\} \\\\
	\texttt{Unit} + \texttt{Bool} = \\{(), \textsf{FALSE}, \textsf{TRUE}\\}
$$

* Provides a "missing" option (`NULL`, `None`, `nothing`, `NA`)
* Often has a special name:
   * `Optional[T] = Union[T,None]` (Python)
   * `optional<T>` (C++)
   * `Maybe T` (Haskell)


## Product types

* Unions can only have one value, one type OR the other
* Products allow one value from each type (AND)
* Represents every possible combination of two types (cross product, outer product)

$$
\begin{align}
	T \times S &= \\{ (x, y) : x \in T, y \in S \\} \\\\
	\texttt{Bool} \times \texttt{UInt8} &= \\{(\textsf{FALSE},0),(\textsf{TRUE},0),(\textsf{FALSE},1),(\textsf{TRUE},1),\dots\\} \\\\
	\texttt{Float} \times \texttt{Float} &\approx \mathbb{R}^2 = \mathbb{R} \times \mathbb{R} \qquad (\mathbb{C}) \\\\
	\left|T \times S\right| &= \left|T\right|\left|S\right|
\end{align}
$$

* Often represented by pairs or tuples: `(T,S)`, `T*S`, `Tuple[T,S]`, `pair<T,S>`


## Larger (and smaller) tuples

$$
	\prod_{i=1}^n T_i = T_1 \times T_2 \times \cdots \times T_n = \texttt{Tuple}(T_1, T_2, \dots, T_n) \\\\
		= \\{ (x_1,\dots,x_n) : x_1 \in T_1, \dots, x_n \in T_n \\} \\\\
	\left| \texttt{Tuple}(T_1, T_2, \dots, T_n) \right| = \prod_{i=1}^n \left| T_i \right|
$$

* `(1.2, 3.1, 5) : Tuple[Float,Float,Int]`
* Larger tuples with labeled fields can be "structs" or "records"


## Empty tuple?

$$
\begin{align}
	\texttt{Tuple}() &= ??? \\\\
	\left| \texttt{Tuple}() \right| &= \prod_{i=1}^0 \left|T_i\right| = 1 \\\\
	\texttt{Tuple}() &\cong \texttt{Unit} = \\{()\\}
\end{align}
$$


## Empty sum?

$$
\begin{align}
	\texttt{Union}() &= ??? \\\\
	\sum_{i=1}^n T_i &= T_1 + \cdots + T_n \\\\
	\sum_{i=1}^0 T_i &\cong \texttt{Void}
\end{align}
$$

* `Union{}` (Julia)


### Quiz

$$
	T + \texttt{Void} = ???
$$

<ol style="list-style-type: lower-alpha;">
<li>\( T \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Void} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Unit} \)</li>
<li class="fragment fade-out" data-fragment-index="1">none of the above</li>
</ol>

<div class="fragment fade-in" data-fragment-index="1">$$ \left|T\right| + 0 $$</div>


### Quiz

$$
	T \times \texttt{Unit} = ???
$$

<ol style="list-style-type: lower-alpha;">
<li>\( T \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Void} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Unit} \)</li>
<li class="fragment fade-out" data-fragment-index="1">none of the above</li>
</ol>

<div class="fragment fade-in" data-fragment-index="1">$$ \left|T\right| \times 1 $$</div>


### Quiz

$$
	T \times \texttt{Void} = ???
$$

<ol style="list-style-type: lower-alpha;">
<li class="fragment fade-out" data-fragment-index="1">\( T \)</li>
<li>\( \texttt{Void} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Unit} \)</li>
<li class="fragment fade-out" data-fragment-index="1">none of the above</li>
</ol>

<div class="fragment fade-in" data-fragment-index="1">$$ \left|T\right| \times 0 $$</div>


### Quiz

$$
	T + T = ???
$$

<ol style="list-style-type: lower-alpha;">
<li class="fragment fade-out" data-fragment-index="2">\( T \) <span class="fragment fade-in" data-fragment-index="1">\( = T \cup T \)</span></li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Void} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Unit} \)</li>
<li>none of the above</li>
</ol>

<div class="fragment fade-in" data-fragment-index="2">
$$ 2 \left|T\right| \\\\
  \texttt{Bool} \times T
$$
</div>


## Arrays, Lists

* Fixed-length arrays are equivalent to tuples:
   $$
	\texttt{Array}\_n(T) = \prod_{i=1}^n T = T^n \qquad \left|T^n\right| = \left|T\right|^n \\\\
	(x_1, x_2, \ldots, x_n) \in T^n \qquad x_i \in T \\\\
	T^0 \cong \texttt{Unit}
   $$
* (Reminder: focus on possible values, not representation)


## Arrays, Lists

* Variable-length arrays can be thought of in a couple (equivalent) ways:
   $$
   \begin{align}
	\texttt{Array}(T) &= \sum_{n=0}^\infty T^n = \texttt{Unit} + T + T^2 + \cdots \\\\
	\texttt{List}(T) &= \texttt{Unit} + (T \times \texttt{List}(T)) \\\\
	\texttt{Array}(\texttt{Bool}) &= \\{(), (\mathsf{F}), (\mathsf{T}), (\mathsf{F},\mathsf{F}), (\mathsf{T},\mathsf{F}), \dots \\}
   \end{align}
   $$
* Infinite type
* By restricting \\( \sum_{n=a}^b T^n \\) we can represent arrays of certain lengths (non-empty, at most 10, etc.)


## Array syntax

| \\( \texttt{Array}\_{[n]}(T) \\)      | language          |
|--------------------|--------------------|
| `List[T]`   | Python |
| `Array{T}`  | Julia |
| `Array<T>`, `T[]`  | TypeScript |
| `[T]`  | Haskell |
| `list<T>`, `vector<T>` | C++ |
| `T v[n]` | C |
| `v(n)`, `DIMENSION` | Fortran |


### Quiz

$$
	\texttt{Array}(\texttt{Void}) = ???
$$

<ol style="list-style-type: lower-alpha;">
<li class="fragment fade-out" data-fragment-index="1">\( \mathbb{N} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Void} \)</li>
<li>\( \texttt{Unit} \)</li>
<li class="fragment fade-out" data-fragment-index="1">none of the above</li>
</ol>

<div class="fragment fade-in" data-fragment-index="1">
$$
	\{()\}
$$
</div>


### Quiz

$$
	\texttt{Array}(\texttt{Unit}) = ???
$$

<ol style="list-style-type: lower-alpha;">
<li>\( \mathbb{N} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Void} \)</li>
<li class="fragment fade-out" data-fragment-index="1">\( \texttt{Unit} \)</li>
<li class="fragment fade-out" data-fragment-index="1">none of the above</li>
</ol>

<div class="fragment fade-in" data-fragment-index="1">
$$
	\{(), \left(()\right), \left((), ()\right), \left((), (), ()\right), \dots \}
$$
</div>


## "Real" (Rational) Numbers

$$
\begin{align}
	\texttt{Digit} &= \\{0,1,2,3,4,5,6,7,8,9\\} \\\\
	\mathbb{N} \cong \texttt{Natural} &= \texttt{Array}(\texttt{Digit}) \qquad 852 \cong (8,5,2) \\\\
	\mathbb{Z} \cong \texttt{Integer} &= \texttt{Bool} \times \texttt{Natural} \quad -852 \cong (\mathsf{T},(8,5,2)) \\\\
	\mathbb{Q} \cong \texttt{Rational} &= \texttt{Integer} \times \texttt{Natural} \\\\
	-8.5 &= \frac{-17}{2} \cong ((\mathsf{T},(1,7)),(2))
\end{align}
$$

Exercise: Strings?


## "Any" types

* Some languages have an "any" type representing union of all possible types, containing all possible values
* `Any`, `void *`

$$
	\texttt{Void} \subseteq T \subseteq \texttt{Any} \quad \forall T
$$


## Functions

Math has the concept of functions mapping
$$
	f(x) = x^2 \\\\
	f : \mathbb{R} \to \mathbb{R}
$$
Same idea here:
$$
	f \in T \to S \\\\
	x \in T \implies f(x) \in S \\\\
	g(x) = \text{if } x \text{ then } 1 \text{ else } 2 \\\\
	g \in \texttt{Bool} \to \texttt{Int}
$$


## Function syntax

| \\( T \to S \\)  | \\( \texttt{Any} \to \texttt{Any} \\)  | language          |
|------------------|-----------|--------------------|
| `Callable[[T], S]` |    | Python |
| `(x: T) => S` | `Function`  | TypeScript |
| `T -> S`  |          | Haskell |
| `S (*)(T)` |   | C (function pointer) |
| `function<S(T)>` | `Callable` | C++ |
|                | `Function` | Julia |


## Multiple arguments

| \\( T, S \to R \\)      | language          |
|--------------------|--------------------|
| `Callable[[T, S], R]`   | Python |
| `(x: T, y: S) => R` | TypeScript |
| `T -> S -> R`  | Haskell |
| `R (*)(T, S)` | C (function pointer) |
| `function<R(T, S)>` | C++ |


## Defining functions

```python
def f(x: T, y: S) -> R:
	z: R = # ...python...
	return z
```

```typescript
function f(x: T, y: S): R {
	let z: R = /* ...typescript... */;
	return z;
}
```

```julia
function f(x::T, y::S)::R
	z::R = # ...julia...
	z
end
```

```c
R f(T x, S y) {
	R z = /* ...c/c++... */;
	return z;
}
```

```haskell
f :: T -> S -> R
f x y = {- ...haskell... -}
```


## Exercise

* How would you represent the position and mass of a particle in the 3D unit box?
* What about an arbitrary number of particles?
* What's the type of a function that calculates the center of mass for these particles?


### Particle types

$$
\begin{align}
	\texttt{Float01} &= \texttt{Float} \cap [0,1] \\\\
	\texttt{Position} &= \texttt{Float01}^3 = \texttt{Tuple}(\texttt{Float01},\texttt{Float01},\texttt{Float01}) \\\\
	\texttt{Mass} &= \texttt{Float} \cap (0,\infty) \\\\
	\texttt{Particle} &= \texttt{Position} \times \texttt{Mass} \\\\
	\texttt{Particles} &= \texttt{Array}(\texttt{Particle}) \\\\
	\texttt{COMFun} &= \texttt{Particles} \to \texttt{Position}
\end{align}
$$


### Particle types (in python)

* Name your types (type "aliases"), even simple ones
* Use them to construct larger types

```python
Float01 = float # float bounded [0,1]
Position = Tuple[Float01,Float01,Float01] # x,y,z
Mass = float # positive
Particle = Tuple[Position,Mass]
Particles = List[Particle]

def centerOfMass(particles: Particles) -> Position:
```


## Checking types

* Much of the advantage of types comes from checking them to make sure they hold
* This can be done in one of two ways:
   * "Statically": before the program runs, by the compiler or static analysis tool
      * Lets you catch errors (typos, bugs) before they happen
   * "Dynamically": while the program runs, as values are created or used
      * Extra checks can slow down your code
* Most languages end up using a mix of both


## Classes as types

* In OO languages you can use classes to help constrain types
   * Additional constraints on the values beyond can be verified in the constructor
   * Dynamic checking: optional, only in "debug" mode

```python
class Order(int):
    def __init__(self, val: int):
        assert val in (1,2,3)

def compute(order: Order) -> float:
```


## Conclusions, tips

* Try to think about your problem starting with data: how do you represent your input, state, etc.
* Write down and name your types
* Build functions that transform between representations to process data
* Consider replacing error checking at the beginning of functions with constrained types



# Break

https://bit.ly/sciware-typing-2022

`pip install mypy`



# Practical Types in Python with mypy

### What, How, and Why of Type-Annotated Python


## Motivation

### Annotations are *FOR YOU*

- The interpreter doesn't care!

- You want to annotate types because they:
  - make your intentions clearer
  - make your expectations more consistent
  - help you think about code structure
  - reduce the load on your human memory
  - enable tooling that can help you even more


### Catching subtle errors

```Python
def turn_a_list_into_a_square_matrix(values):
    root = math.sqrt(len(values))
    if root < 1 or root % 1 != 0:
        return None
    array = np.asarray(values)
    array = array.reshape((root, root))
    return array

if __name__ == '__main__':
    input_int = 54
    untyped = turn_a_list_into_a_square_matrix(input_int)
```


### Catching subtle errors

```Python
def turn_a_list_into_a_square_matrix(values):
    root = math.sqrt(len(values))
    if root < 1 or root % 1 != 0:
        return None
    array = np.asarray(values)
    array = array.reshape((root, root))
    return array

if __name__ == '__main__':
    input_int = 54
    untyped = turn_a_list_into_a_square_matrix(input_int)
    ## oops! 54 isn't a list--so len(54) causes an error
    ## ...but did you catch the other error too?
```


### Useful contextual information

- Auto-completing members of known classes

<img src="assets/member-display.png" width="500" style="border:0;box-shadow:none">


- Reminding you what a variable should contain

<img src="assets/variable-id.png" width="600" style="border:0;box-shadow:none">


### Design & Refactor with confidence!

- Forces you to think about design
  - But gives you a framework for thinking
- As design evolves, type checker can make sure you've caught everything


### Today is Python Typing 101

- For further research, see the docs:
  - [Python typing basics](https://peps.python.org/pep-0483/)
  - [Full doc on Python type hinting](https://docs.python.org/3/library/typing.html)
  - [mypy documentation](https://mypy.readthedocs.io/en/stable/)
- Note these docs privilege exhaustiveness over readability...


## Outline

- Basics
  - Installation
  - Syntax
  - Allowed types
- Dealing with parameterized types
- Using the Type System
- Type Inference
- Maybe some live coding?


## Vocab

- **Static analysis** (SA)--determining possible behavior of code just from
its structure, without running it
- **Type Checker**/**Type Analyzer**--SA tool that reasons about variable and function types (e.g. `mypy`)
- **Linter**--SA tool that checks style, code reachability, & more
- **Duck typing**--"if it quacks like a duck, it's a duck"
  - If it has matching properties, it counts as a ___


## Basics


### Installing mypy

```bash
$ pip install mypy
$ mypy list_to_square.py
```

<img src="assets/running-mypy.png" width="1200" style="border:0;box-shadow:none">


### IDEs -- Turning On Typing

- VSCode:
  - Install Python and/or Pylance extensions
  - File -> Preferences -> Settings (ctrl-,)
    - For pylance extension:\
      Extensions -> Pylance -> Type Checking Mode
    - For python extension:\
      Extensions -> Python -> Linting: Mypy Enabled, Mypy Path
- Pycharm
  - Install mypy executable, then mypy plugin from JetBrains plugin site


## Annotating Types


### Syntax

- Postfix type hints:
  - Form is `<VARIABLE_NAME>: <TYPE_NAME>`
  - `int_valued_variable: int = 5`
  - Applies anywhere a variable is first used, including function parameters
- Function return values use an arrow:
  - `def f(x: int) -> float:`
  - This says `f` takes an `int` and returns a `float`
  - Typing for a function is called a *type signature*


### What types are available?

- Primitive types: Basic data\
  (Types that actually exist in the interpreter)
  - `int`
  - `float`
  - `bool`
  - `str`


- Non-primitives
  - `None` -- technically not a primitive
  - `Any` -- Matches anything; *turns off type checking*
  - `object` -- Matches anything; *doesn't* turn off checking
  - Any classes in your namespace
    - (e.g. `ddt.Client` if you did\
      `import dask.distributed as ddt`)


- Parameterized types
  - Built-in container types:
    - `List`
    - `Set`
    - `Tuple`
    - `Dict`
  - `Callable`
  - `Literal`
  - ...
- We'll talk about these in detail in a minute


### Typing and Objects (Classes)

- Any class defined in your namespace can be used as a type
  - Built-in classes
  - Classes from imports
  - Classes from your code
- Child classes count as the parent class


- Built-in classes work (but you may need to import the types explicitly):

```python
from io import TextIOWrapper

def write_to_file(msg: str, handle: TextIOWrapper) -> None:
    handle.write(msg)
```

[filehandle.py](./examples/filehandle.py)


- Child classes count as members of the parent class:

```python
class Parent(): pass
class Child(Parent): pass

def example() -> None:
    a: Parent = Parent()
    b: Parent = Child()  # no problem: Child counts as Parent
    c: Child = Parent()  # error: Parent does not count as Child
    d: Child = b         # Works! We know b *must* be a Child here
```

[classes.py](./examples/classes.py)


- Linters differ on using a class during its definition

```python
class MyClass():
    def __init__(self) -> None:
        pass

    def compare(self, other: MyClass) -> int:
        return 5
```

[defining_classes.py](./examples/defining_classes.py)

- `mypy` thinks this is fine
- VSCode complains about using `MyClass` in `compare`
  - To fix: put it in quotes (`other: 'MyClass'`)
  - Recognizes `MyClass` fine outside its definition


- `self` never needs type annotation: it's inferred
- `__init__` is inferred to return `None`
  - BUT `mypy` skips functions without type annotations
  - Fix: if you have no non-`self` parameters, explicitly return `None`
  - Or use `--strict`


## Parameterizing container types


- Container types need *parameters* to be useful
  - e.g. `List[int]`, not just `List`
  - (What's in the list? Defaults to `Any`)


### Recent syntax changes

- pre-3.10:
  - Capital letters (`List`, `Set` etc)
  - imported from `typing` package
- 3.10+:
  - Built-ins (`list`/`set`/`dict`/`tuple`) can be lower-case
  - And don't need to be imported
  - More complex types now come from `collections.abc`
- Examples below use the older syntax


### List & Set

- Parameters go in square brackets:\
  `List[str]` or `Set[int]`

```Python
from typing import List
def sum(items: List[int]) -> int:
    pass
```

Or in 3.10+:
```Python
def sum(items: list[int]) -> int:
    pass
```


### Tuple

- A `Tuple` has a fixed* number of ordered elements
  - Used whenever you pack values together\
    e.g. returning `(x, y)` as one unit
```Python
price_and_count: Tuple[float, int] = (1.5, 3)
```
  - (An empty tuple is typed as `Tuple[()]`)


### Dict

- Stores unique *keys* that point to *values*
- Must provide types for both\
  (`Dict[KEYTYPE, VALUETYPE]`)
```Python
heights_per_person: Dict[str, float] = {}
```
- Along with variable naming, this documents the data structure


### Union

- Sometimes a variable can be one of a few different types:
```Python
cash_on_hand: Union[int, float, None] = ...
```

- This allows flexibility while still providing guidance.
  - In 3.10, can just use an `or` pipe:
```Python
cash: int | float | None
```


### You can nest them...!

```python
cash_per_person: Dict[str, Union[int, float, None]] = {...}
```

But it gets long...

```python
points: Dict[str, Dict[int, List[float]]] = {...}
# for each student, for each test number, store how many points they got on each question
```

- ```points["Kushim"][1]``` is a list of how many points Kushim got on each question
on the first Accounting exam at Uruk University


### Type Aliases

- Instead we can define *type aliases*

```python
from typing import TypeAlias

Gradebook: TypeAlias = Dict[str, Dict[int, List[float]]]
my_gradebook: Gradebook = get_gradebook_for_semester()
grades_for_student = gradebook['Kushim']
```

 [typealias.py](./examples/typealias.py)

- Lets you use a shorter but more meaningful name for something complex
  - Note: explicitly adding `TypeAlias` is a 3.10 thing--previously it was inferred,
    which led to some ambiguity.


- Or go even further:

```python
from typing import TypeAlias

StudentName: TypeAlias = str
TestId: TypeAlias = int
PointsPerQuestion: TypeAlias = List[float]

Gradebook: TypeAlias = Dict[StudentName, Dict[TestId, PointsPerQuestion]]

my_gradebook: Gradebook = get_gradebook_for_semester()
kushim_points_test_one = gradebook['Kushim'][1]
```


### Why Use Type Aliases?

- Pros:
  - Meaningful names document *intention*
  - Shorter: easier to read and type
- Cons:
  - Sometimes mouseover hints don't drill down enough
    - (might just get `Gradebook`, not actual structure)
  - Might be better off with an actual class or a [dataclass](https://docs.python.org/3/library/dataclasses.html)


### Callable

- Describes the type of a function stored in a variable.
- Takes list of parameter types, then return type

```python
from typing import Callable

sum_then_square: Callable[[float, float], float]
sum_then_square = lambda x, y: (x + y) ** 2
```
[callable.py](./examples/callable.py)

- Useful for higher-order programming & function composition


### Literals

- `Literal` means a *specific* value
  - `Literal[15]` is `15`, not any other integer

```python
way: Union[Literal['North'], Literal['South'], Literal['East'], Literal['West']]
way = 'west'
```
[literal.py](./examples/literal.py)

- Did you catch the error there?
- You probably want an [Enum](https://docs.python.org/3/library/enum.html)
  - `Literal` is mostly the result of type inference


## How you interact with types


### At runtime

- You pretty much don't!
- Errors from your linter are not enforced at runtime
- Interpreter has its own type & object system
- Type hinting is entirely for static code analysis
  - You *could* use `TypeGuard`s (see bonus content)


### In your editor

- Highlighting of type errors
- mouseover information for variables, functions
- auto-completion of member reference
  - (`my_ClassA_var.` pops up methods from `ClassA`)
- auto-populates docstring skeleton


### With separate analyzer (mypy)

- Generates a report of detected type errors
- By default:
  - **ONLY** looks at functions having explicit type hinting
  - *Stops tracking* variables which are annotated `Any`
- `--strict` flag makes it more aggressive
- Useful as a continuous integration step


- Customize `mypy` behavior with command-line arguments
  - [Full command line documentation](https://mypy.readthedocs.io/en/stable/command_line.html)
  - In particular: `--strict` and `--disallow-any-expr`
  - `--strict` turns on a lot of checks that are skipped by default
  - `--disallow-any-expr` reports every use of `Any`


- `mypy` also prints out informative messages if you ask it to
  - `reveal_type(x)` prints the type `x` has when the statement is encountered during `mypy` analysis
  - For more advice, see [the Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)


### Brief review example

[list_to_square.py](./examples/list_to_square.py)


## Type Inference

- Type annotations are most useful for documenting functions, key variables
- The analyzer can often figure out a type through static analysis, without hints:

```Python
def random_integer() -> int:
    return 15   # TODO: Pick more-random number

def do_math() -> int:
    a = random_integer() # linter knows a is an int!
    b = random_integer()
    c = a + b
    return c
```
[inference.py](./examples/inference.py)


### Narrowing

- `Union` types can be understood more precisely when context eliminates some possibilities
- Type checker understands a few built-in functions
  - Type is narrowed *only* within a conditional branch
  - Linter understands how `assert`, `return`, & exceptions affect this

```python
def narrowing_example(my_var: Union[str, int]) -> int:
    if isinstance(my_var, str):
        # In this branch, we know my_var is a str
        return len(my_var)
    # All strs exit the function at the "return" statement
    # So by process of elimination, my_var must be an int
    # And mouseover will show 'int' here
    return my_var + 1
```
[narrowing.py](./examples/narrowing.py)


- `isinstance()` actually works at runtime, so `mypy` knows this is safe
- Also supported:
  - `issubclass(cls, MyClass)`
  - `if (type(a) is int)`
  - `if (variable is None)`
  - `if (callable(fn))` (though this doesn't distinguish `Callable`s with different signatures)
  - User-defined type guards


- `Optional[TYPE]` is short for `Union[TYPE, None]` and benefits from narrowing:

```python
def narrowing_example_2(a: Optional[int]) -> None:
    print(a) # here 'a' could be int or None
    if (a is None):
        raise Exception('Exception ends this branch!')
    a # here a must be int
```

- This is useful for handling user inputs


### Casting

- For when inference fails!
- If you know better than the analyzer, you can overrule it
- Use sparingly: there is usually a better way
  - Even if it's just type-hinting the receiving variable

```python
import xarray as xr
from typing import cast

def load_xarray(filename: str) -> xr.Dataset:
    unknown_results = xr.open_dataset(filename)
    # xarray doesn't publish types (yet), so open_dataset is not annotated.
    # But we know it returns a Dataset object.
    # So use cast(TYPE, VALUE) to tell the checker that VALUE is of type TYPE
    results = cast(xr.Dataset, unknown_results)
    return results
```
[casting_example.py](./examples/casting_example.py)


- If a variable is *explicitly* marked `Any`, it gets ignored from then on
- Even casting it won't turn type checks back on for it


### Generics

- Sometimes you can say *something* about a type without knowing *everything* about it.
- Suppose we have a function that adds a new item to the front of a typed list:
```python
def prepend_to_list(value: int, values: List[int]) -> List[int]:
    return [value] + values
```
  - Great, now do one for every other possible type of `list`...???


- Instead, use a *variable type parameter* `TypeVar`:

```python
from typing import TypeVar

T = TypeVar('T')
def prepend_to_list(value: T, values: List[T]) -> List[T]:
    return [value] + values
```

- This now works for any type!
- But some operations don't make sense for any arbitrary type?
  - There are ways to add restrictions to the type parameter


### Numpy

- Runtime uses more precise types (`dtypes`)
  - Based on actual bit representation
  - Closer to types in C
- Since 2021, `numpy` has `numpy.typing` ([official doc](https://numpy.org/doc/stable/reference/typing.html))
  - Annotating array shapes is not yet supported
  - 3rd-party extensions (`nptyping`) do allow typing array dimensions


## Big Example

[riemann.py](./examples/riemann/riemann_base.py)

[completed version](./examples/riemann/riemann-full.py)


## Bonus Content

- Here are some topics which are beyond today's main scope.


### Final

- Means you shouldn't change the variable's value
  - Like `const` in JavaScript/TypeScript, C/C++/C#, etc.

```python
  x: Final[int] = 15
  x = 22     # will generate a warning
```
[final.py](./examples/final.py)

- This is *great* for supporting [functional programming](https://en.wikipedia.org/wiki/Functional_programming)
and reducing mistakes
  - But it **is not** enforced at runtime!
- There are other not-strictly-type annotations available; see docs


### TypeGuards

- `TypeGuard`: a function that returns whether a variable is of a given type
  - Connected to narrowing
  - Code that both actually works at runtime...
  - ...and is also understood by the type analyzer


```python
def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)
```

- This returns true if & only if every element of `val` is a `str`
  - Other code can now call `is_str_list(some_list)` and branch on the result
  - in a branch where `is_str_list(x)` returned `True`, the type checker also knows `x` is a `List[str]`
- You can do a *lot* with these
  - [Official documentation](https://mypy.readthedocs.io/en/stable/type_narrowing.html#user-defined-type-guards)
  - [typeguard.py](./examples/typeguard.py)


### Generics and Constraints

- `TypeVar()` lets you add *subtype constraints* to limit what generic types you support
  - e.g. `TypeVar('T', int, float)` means `T` must be an `int` or `float`.
  - How is that different from `Union[int, float]`?
    - `List[T]`: all elements are `T` (either `int` or `float`)
    - `List[Union[int, float]]` could contain some `int`s and some `float`s


- You can also restrict to type families:
  - `TypeVar('S', bound=str)` means `S` has to extend `str` to qualify.
  - This supports the possibility of more specific types while guaranteeing that certain functionality will be available
- One `TypeVar` can only use either binding or subtype constraints
  - it doesn't make sense to use both


### Covariance and Contravariance

- [python doc](https://peps.python.org/pep-0483/#covariance-and-contravariance)
- [wikipedia](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science))


- Suppose I have an `Animal` class
  - both `Cat` and `Dog` inherit from `Animal`
- Is `List[Cat]` a subtype of `List[Animal]`?
  - What about `Callable[]`s?
  - Generally: how does class inheritance play with container types?


- *Covariant*: Means that if `A` is a subtype of `B`, then `Generic[A]` is always a subtype of `Generic[B]`
- *Contravariant*: Means that if `A` is a subtype of `B`, then `Generic[B]` is always a subtype of `Generic[A]`
  - (Note it's reversed!)
- *Invariant*: the relationship is inconsistent.


- Functions are "contravariant in parameters but covariant in returns":
  - `f() -> Cat` is a subtype of `f() -> Animal`
    - Any caller expecting an `Animal` can take a `Cat`.
    - This is covariance
  - *BUT* `f(x: Animal) -> None` is a *subtype* of `f(x: Cat) -> None`!
    - Of all the functions that operate on `Cat`s, only some work on all `Animal`s.
    - This is contravariance
- This mostly comes up with `Callable`s, function-valued variables, and [callbacks](https://en.wikipedia.org/wiki/Callback_(computer_programming))
- The most general *callback* takes the most *specific* class of inputs and returns the most *general* class of outputs


- Lists are *invariant*:
  - All items from a `List[Dog]` are legitimate items of a `List[Animal]`
    - So `List[Dog]` is a subtype *when acting as a source*
  - `List[Animal]` can *receive* all items that could be added to `List[Dog]`, but not vice versa
    - So `List[Animal]` is a subtype *when acting as a sink*
  - Relationship is not fixed -- thus invariant



# Survey

https://bit.ly/sciware-typing-2022
