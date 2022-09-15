# Sciware

## Command line and Shell interaction

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
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/).


## Future Sessions

- Planning for the next few months:
   - Modern C++
   - File formats, data management, hdf5
- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda

- Thinking about types: concepts, syntax
- Concrete types, storage, performance
- Types in python: mypy



# Type concepts

### Dylan Simon (SCC)


# Applying Types

* *Not* type theory (a branch of mathematics involving propositional logic and category theory)
* algebraic data types


## Motivation

TODO: start with example with bug that types would catch (repeat at end)


## Types

* If you think about types at all, you probably think storage, bits:
   * `float`, `double`, `int32`, `string`
   * `list` (of what?), `complex`, `struct`, `class`
* Types are not about how many bits, but about the values these bits represent
* Types are for thinking abstractly about your data (not the algorithm or implementation)


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
        \texttt{Int} &\approx \mathbb{Z} \\\\
        \texttt{Float} &\approx \mathbb{Q} \approx \mathbb{R} \\\\
	\texttt{Float32} &\approx \pm 10^{\pm 38} \text{ with 7 digits} \\\\
	\left|\texttt{Float32}\right| &\le 2^{32} \\\\
	\left|\texttt{Float64}\right| &\le 2^{64}
\end{align}
$$

* Practically, cardinality is always finite (computers have finite memory)
* We may define types with infinite cardinality, but always countably infinite!


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
   * `void` in C?
* All types with the same cardinality are isomorphic (can trivially substitute one for another by replacing values)


## A set of values you choose

No need to limit yourself to established types!

$$
	\\{1,2,3\\} \qquad
	\\{\textsf{YES}, \textsf{NO}, \textsf{MAYBE}\\} \\\\
	\\{\textsf{RED}, \textsf{GREEN}, \textsf{BLUE}\\} \\\\
	\texttt{Float} \cap [0,1] ~ (\\{x \in \texttt{Float} : 0 \le x \le 1 \\}) \\\\
	\texttt{Int} \cap \mathbb{P} \qquad
	\mathbb{Q}^+ ~ (\\{x : x > 0\\}) \\\\
	\texttt{Float} \setminus \\{ \textsf{NaN}, \pm\textsf{Inf} \\} \quad
	(T \setminus S = \\{ x \in T : x \notin S \\} = T - S)
$$

* Many languages represent "finite" data types with labeled values as *enumerations*


## Why is this useful?

Documentation, optimization, error checking, logic!

```python
def compute(order ∈ {1,2,3}):
  if order == 1:
    ...
  elif order == 2:
    ...
  else: # order == 3
    ...
```

* Can be helpful for describing and thinking about code even if the types are not perfectly represented in the programming language
* Once a variable is given a type, any value it has must be in that type


## Type syntax

Different languages use a variety of syntax to represent types

| \\( x \in T \\)             | languages          |
|--------------------|--------------------|
| `x: T`, `x: int`   | Python, TypeScript |
| `x :: T`, `x::Int` | Julia, Haskell     |
| `T x`, `int x`     | C, C++, Fortran 77 |
| `T :: x`, `integer :: x` | Fortran 90   |


## Adding types: Unions

$$
\begin{align}
	\texttt{Bool} \cup \\{\textsf{UNKNOWN}\\} &= \\{\textsf{FALSE}, \textsf{TRUE}, \textsf{UNKNOWN}\\} \\\\
	\texttt{Int8} \cup \texttt{Int32} &= \texttt{Int32} \\\\
	(\texttt{Int8} \subset \texttt{Int32})
\end{align}
$$

* Simple unions are not particularly useful, as they can usually be represented by a different type
   * Some exceptions: C `union`
* Instead...


## Sum types (disjoint unions)

Sometimes we want to allow different types of values, so we make a new type by combining other types with a union:

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
| `Union<T,S>` (`T\|S`)    | TypeScript |
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
		= \\{ (x_1,\dots,x_n) : x_1 \in T_1, \dots, x_n \in T_n \\}
$$

Larger tuples with labeled fields are "structs" or "records"

$$
\begin{align}
	\texttt{Tuple}() &= ??? \\\\
	\left| \texttt{Tuple}() \right| &= \prod_{i=1}^0 \left|T_i\right| = 1 \\\\
	\texttt{Tuple}() &= \texttt{Unit} = \\{()\\}
\end{align}
$$


## Empty sum?

$$
\begin{align}
	\sum_{i=1}^n T_i &= T_1 + \cdots + T_n \\\\
	\sum_{i=1}^0 T_i &= \texttt{Void}
\end{align}
$$

* `Union{}` (Julia)


### Quiz
$$
\begin{align}
	T + \texttt{Void} &= ??? \\\\
	T \times \texttt{Unit} &= ??? \\\\
	T \times \texttt{Void} &= ??? \\\\
	T + T &= ???
\end{align}
$$


### Answers
$$
\begin{align}
	T + \texttt{Void} &= T & \left|T\right| + 0 \\\\
	T \times \texttt{Unit} &= T & \left|T\right| \times 1 \\\\
	T \times \texttt{Void} &= \texttt{Void} & \left|T\right| \times 0 \\\\
	T + T &= \texttt{Bool} \times T & 2 \left|T\right|
\end{align}
$$


## Arrays, Lists

* Fixed-length arrays are equivalent to tuples:
   $$
	\texttt{Array}\_n(T) = \prod_{i=1}^n T = T^n \qquad \left|T^n\right| = \left|T\right|^n \\\\
	(x_1, x_2, \ldots, x_n) \in T^n \qquad x_i \in T \\\\
	T^0 = \texttt{Unit}
   $$
* (Remember: focus on possible values, not representation)


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
| `T x[n]` | C |
| `x(n)`, `DIMENSION` | Fortran |


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


## Subtypes

If one type is a subset of another, we call it a subtype:

$$
	S \subseteq T \qquad \forall x, x \in S \Rightarrow x \in T \\\\
	S \times U \subseteq T \times U \\\\
	S + U \subseteq T + U \\\\
	\texttt{Array}(S) \subseteq \texttt{Array}(T) \\\\
	T \subseteq T + U \\\\
	\texttt{Int8} \subset \texttt{Int16} \subset \texttt{Int32}
$$

* Similar to inheritance: if \\( C \\) inherits from \\( B \\), then \\( C \subset B \\)


## Functions

$$
	f(x) = x^2 \\\\
	f : \mathbb{R} \to \mathbb{R} \\\\
	f \in T \to S \\\\
	x \in T \implies f(x) \in S \\\\
	g(x) = \text{if } x \text{ then } 0 \text{ else } 1 \\\\
	g \in \texttt{Bool} \to \textt{Int}
$$


## Function syntax

| \\( T \to S \\)      | language          |
|--------------------|--------------------|
| `Callable[[T], S]`   | Python |
| `(x: T) => S`, `Function`  | TypeScript |
| `T -> S`  | Haskell |
| `S (*)(T)` | C (function pointer) |
| `function<S(T)>`, `Callable` | C++ |
| `Function` | Julia |


## Exercise

* How would you represent the position and mass of a particle in the 3D unit box?
* What about an arbitrary number of particles?
* What's the type of a function that calculates the center of mass for these particles?


## Multiple arguments

* Approaches to functions with multiple arguments:

$$
	f \in (T \times S) \to R \qquad \text{single tuple argument} \\\\
	f \in T \to S \to R \qquad \text{currying}
$$

| \\( T, S \to R \\)      | language          |
|--------------------|--------------------|
| `Callable[[T, S], R]`   | Python |
| `(x: T, y: S) => R`, `Function`  | TypeScript |
| `T -> S -> R`  | Haskell |
| `R (*)(T, S)` | C (function pointer) |
| `function<R(T, S)>`, `Callable` | C++ |


## Defining functions

```python
def f(x: T, y: S) -> R:
	z: R = python
	return z
```

```typescript
function f(x: T, y: S) => R {
	let z: R = typescript;
	return z;
}
```

```julia
function f(x::T, y::S)::R
	z::R = julia
	z
end
```

```c
R f(T x, S y) {
	R z = c/c++;
	return z;
}
```

```haskell
f :: T -> S -> R
f x y = haskell
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

* In many languages you can use classes to represent your own types
* If you want additional constraints on the values beyond their storage types, you can verify these in the constructor (\\( 0 \le x \le 1 \\))
* It's nice if storage representation for values is opaque (users of the class don't interact directly with the value), but this can be impractical for performance in some cases


only data not operations (members not methods)
classes do a lot more than this


dimensional analysis? (1 slide)


any (python union all types)


how you interpret bits orthogonal


how i think about writing code, data first


error checking at beginning of functions


motivation to start


back to bits at end:
  ieee


type coersion:
  check types through expression


representation, performance:
  double vs float
  less precision, more iterations
  general: reducing domain increases performance
  example 


# Practical Types in Python with mypy



## Motivation

### Catching subtle errors

```Python
def make_a_square_untyped(values):
    root = math.sqrt(len(values))
    int_root = int(root)
    if root < 1 or root != int_root:
        return None
    array = np.asarray(values)
    array = array.reshape((root, root))
    return array

if __name__ == '__main__':
    input_int = 54
    untyped = make_a_square_untyped(input_int)
```


### Useful contextual information

[NEEDS SCREENSHOT]



### Full documentation

- [The Python documentation](https://docs.python.org/3/library/typing.html)
- [mypy documentation](https://mypy.readthedocs.io/en/stable/)

Note that these are both exhaustive (often with reference to PEPs, etc). We'll
try to give you a much gentler introduction to the parts you'll actually need
right away.


## Basics

### Installing mypy

```bash
$ pip install mypy
```

Can now run with:

```bash
$ mypy file_to_examine.py
```


### Known types

- Primitive types: Basic data
  - `int`
  - `float`
  - `bool`
  - `str`
  - `None`
  - `Any` (this does need to be imported if you want to annotate it explicitly)
- Complex types that "just work"
  - `object`
  - Specific classes that are in your namespace (e.g. `np.ndarray`)


- Container types
  - `List`
  - `Dict`
  - `Tuple`
  - `Set`
  - `Callable`
  - `Literal`
  - ...
- Container types need *parameters*
  - e.g. `List[int]`, not just `List`
- Generally need to be imported from `typing` package
- Recent changes: 3.10 lets you lowercase, and allows importing from `collections.abc`
- Our examples will work in 3.10 or earlier versions


### Syntax

- Postfix type hints:
  - `int_valued_variable: int = 5`
  - Applies to any variable definition, including function parameters
- Function return values use an arrow:
  - `def f(x: int) -> float:`
  - This says `f` is a function that takes an int and returns a float

### Parameterizing container types

- What's in that `List`?
  - `my_int_list: List[int] = []`
- `Dict[]` takes the key and value
  - `x = Dict[str, float]`
- `Callable[]` annotates functions with a parameter list and return type
  - `f: Callable[[float], float] = lambda x: x**2`
- These can stack (though it gets confusing):
  - `grades = Dict[str, Dict[int, List[int]]]` is a dictionary that maps a string key
  to a dictionary that maps integer keys to a list of integers...
  - Concretely, then, `math_test_responses = grades['Lehman']` would be a list of Lehman's responses
  for test 1, test 2, ...


### Semantic value of Python types at runtime

...there isn't any!

Python typing is entirely for static code analysis. It goes away at runtime.


## Using type analysis

- Baked in to your editor
  - e.g. mouseover information for variables, functions
  - auto-completion of member reference (`my_ClassA_var.` pops up a list of methods from `ClassA`)
  - auto-populates docstring skeleton
- By running `mypy` on the command line
  - Generates a report of detected type errors
  - **ONLY** looks at functions that have some explicit type hinting


### Simple Worked Example

NOTE: Can also do this as a dynamic process using the code in simple_example.py.
Start w/ untyped_buggy, move to untyped, add type hints.
Demo running mypy on cli?

```python
def make_a_square_typed(values: List[int]) -> Union[np.ndarray, None]:
    root = math.sqrt(len(values))
    int_root = int(root)
    if root < 1 or root != int_root:
        return None
    array: np.ndarray = np.asarray(values)
    array = array.reshape((int_root, int_root))
    return array
```


## Type Inference

- If the analyzer can figure out what something's type is, it will tell you
```Python
def returns_int():
    return 15

a = returns_int()
```
Mousing over `a` in fact reveals it's not even an `int` but a `Literal[15]`


```Python
def really_returns_int(a):
    return int(a)

a = really_returns_int(26)
```
Mousing over `a` here shows `int` like you'd expect


### Quick note on Literal, Final

- `Literal` means a *specific* value
- `Final` tells the linter that something shouldn't be changed
  ```Python
  x: Final[int] = 15
  x = 22
  ```
  - This will give you a warning in your editor, but remember it isn't enforced at runtime


### Narrowing

- Static analyzer is reading your code and can give you greater precision
- `Union` types can be interpreted more precisely if the context eliminates some possibilities

```python
def narrowing_example(a: Union[str, int]) -> str:
    if isinstance(a, str):
        return a
    else:
        # type checker now knows a is an int, because it wasn't a str
        return str(a)
```


- `Optional` is a shorthand for `Union[__, None]` and benefits from narrowing:
```python
def narrowing_example(a: Optional[int]) -> None:
    print(a) # here 'a' could be int or None
    if (a == None):
        raise Exception('Maybe handle this more gracefully than by throwing an exception!')
    a # here a must be int, and mouseover shows it
```


### TypeGuards

- A `TypeGuard` is a function that helps narrowing by checking if a variable meets criteria to be a given type.
- Use `TypeGuard[]` as return type of a boolean function to invoke type checking on its result.
- e.g.:
```python
def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)
```
  - Other code can now call `is_str_list(some_list)` and branch on the result
  - This lets you specify logic that works at runtime and is understood by the checker at write time
- Don't worry about it


### Casting

- For when inference fails!
- If you know better than the analyzer, you can tell it what something is

```python
def casting_example(parameters) -> None:
    x0 = parameters['x0'] # here x0 is typed as 'Any' since we don't know what it is
    x0 = cast(float, parameters['x0']) # here it's a float: I said so
```


## Generics

- Sometimes you can say *something* about a type without knowing *everything* about it.
```python
def get_max(values: List[int]) -> int:
    pass
```
  - It'll be a drag to make one of those for every type in existence.


- Instead, you can use a *variable type parameter* using `TypeVar`:
```python
from typing import TypeVar

T = TypeVar('T')
def get_max(values: List[T]) -> T:
    pass
```
- This now works for any type (as long as you can write logic that makes sense)
- `TypeVar()` lets you add *constraints* to limit what generic types you support
  - This is beyond the scope of this tutorial


## Types and Classes

- If your namespace recognizes a class, you can use it as a type
- `None` is *not* a valid value for a class variable! (Even if it works in other languages)


### Inheritance

- Inheriting classes count as members of the parent class:
```python
b: MyClass = MyClass()
c: MyOtherClass = MyOtherClass()
d: MyOtherClass = b # fails; MyClass is not a MyOtherClass
b = 5 # fails (naturally; 5 is not a MyClass)
b = d # succeeds -- inheritance means any MyOtherClass is a MyClass
```
- Don't be fooled: pretty much everything counts as an `object`
  - `b: object = 5` works, unlike the above


### Defining your own class

- Once you've defined a class, it can be used
- Linter standards differ on whether you can use a class during definition
  - example:
```python
class MyClass():
    def __init__(self):
        pass

    def compare(self, other: MyClass) -> int:
        return 5
```
  VSCode PyLance will complain about this, but mypy thinks it's fine
  - You can get around it for VSCode by adding quotes: `... other: 'MyClass')`
- `self` never needs type annotation: it's inferred
  - BUT an `__init__(self)` won't be type-checked in mypy unless it has
  annotated parameters or you explicitly say it returns `None`.


### I/O Types? Anything special to say here?

There are types for them? Honestly, maybe we just use them as an example somewhere.


## Big Example

See `reimann.py` in this directory; we can work through
adding types and just review this code for some of the neat tricks.
(The file as currently uploaded is the target final version--I might consider doing this
as a live-coding session building toward this target from some untyped code.)

It includes typed lambdas/using `Callable`, `Enum`s, optionally `dataclass` usage.
Benefits greatly from typing and other static analysis features.

