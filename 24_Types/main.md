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
        \texttt{Int} &\approx \mathbb{Z} \\\\
        \texttt{Float} &\approx \mathbb{Q} \approx \mathbb{R} & \left|\texttt{Float}\right| &\le 2^{32}
\end{align}
$$

By saying \\( x \\) has type \\( T \\) we mean
$$ x \in T $$
\\( \left|T\right| \\) is the number of possible values in \\( T \\) (the *cardinality*, possibly infinite, always countable)


## Special types

A couple simple types may seem silly but are quite useful:

$$
\begin{align}
	\texttt{Unit} &= \\{()\\} & \left|\texttt{Unit}\right| &= 1 \\\\
	\texttt{Void} &= \emptyset = \\{\\} & \left|\texttt{Void}\right| &= 0
\end{align}
$$

* `Unit` is the singleton type with only one possible value (`None` in python, `Nothing` in Julia)
* `Void` is the empty type with no possible values (never, impossible, a value that can never exist, the return value of a function that never returns)
   * `void` in C?
* All types with the same cardinality are isomorphic (can trivially substitute one for another by replacing values)


## A set of values you choose

No need to limit yourself to established types!

$$
	\\{1,2,3,4\\} \qquad
	\\{\textsf{YES}, \textsf{NO}, \textsf{MAYBE}\\} \\\\
	\\{\textsf{RED}, \textsf{GREEN}, \textsf{BLUE}\\} ~ \text{(enum)} \\\\
	[0,1] \cap \texttt{Float} ~ (\\{x : 0 \le x \le 1\\}) \\\\
	\mathbb{P} \cap \texttt{Int} \qquad
	\mathbb{R}^+ ~ (\\{x : x > 0\\}) \\\\
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


## Unions

$$
	\texttt{Bool} \cup \\{\textsf{UNKNOWN}\\} &= \\{\textsf{FALSE}, \textsf{TRUE}, \textsf{UNKNOWN}\\} \\\\
	\texttt{Int8} \cup \texttt{Int32} &= \texttt{Int32} & (\texttt{Int8} \subset \texttt{Int32})
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
	\left|T + S\right| &= \left|T\right| + \left|S\right| \\\\
	\texttt{UInt8} + \texttt{UInt32} &= \\{0_8, 1_8, \dots, 255_8, 0_{32}, 1_{32}, \dots\\} \\\\
		&\ne \texttt{UInt8} \cup \texttt{UInt32}
\end{align}
$$

* Sometimes called a "tagged" union because values are tagged by which type they're from
* "discriminated": each value is either from `T` or `S` (and you can tell)


## Type parameters, more syntax

* Types can have parameters (arguments) of other types
* \\(+\\) is an operator (function) that builds existing types into a new one: \\( T+S = \texttt{Union}(T,S) \\)
* Different languages have different syntax for these parameterized types (and different names for unions):

| \\( T + S \\)      | language          |
|--------------------|--------------------|
| `Union[T,S]`   | Python |
| `Union<T,S>` (`T\|S`)    | TypeScript |
| `Union{T,S}`  | Julia |
| `Either T S`  | Haskell |
| `variant<T, S>`    | C++ |


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
	\left|T \times S\right| &= \left|T\right|\left|S\right| \\\\
	\texttt{Float} \times \texttt{Float} &\approx \mathbb{R}^2 = \mathbb{R} \times \mathbb{R}
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

Quiz:
$$
	T + \texttt{Void} = ??? \\\\
	T \times \texttt{Unit} = ??? \\\\
	T \times \texttt{Void} = ???
$$


## Arrays = Lists

* Fixed-length arrays are equivalent to tuples:
   $$
	\texttt{Array}\_n(T) = \prod_{i=1}^n T = T^n \qquad \left|T^n\right| = \left|T\right|^n
   $$
* Variable-length arrays can be thought of in a couple (equivalent) ways:
   $$
   \begin{align}
	\texttt{Array}(T) &= \sum_{n=0}^\infty T^n = \texttt{Unit} + T + T^2 + \cdots \\\\
	\texttt{Array}(\texttt{Bool}) &= \\{(), (\mathsf{F}), (\mathsf{T}), (\mathsf{F},\mathsf{F}), (\mathsf{T},\mathsf{F}), \dots \\} \\\\
	\texttt{List}(T) &= \texttt{Unit} + (T \times \texttt{List}(T))
   \end{align}
   $$
* By restricting \( \sum_{n=a}^b \) we can represent arrays of certain lengths (non-empty, at most 10, etc.)


## Array syntax

| \\( \texttt{Array}\_{[n]}(T) \\)      | language          |
|--------------------|--------------------|
| `List[T]`   | Python |
| `Array{T}`  | Julia |
| `T[]`, `Array<T>`  | TypeScript |
| `[T]`  | Haskell |
| `list<T>`, `vector<T>` | C++ |
| `T x[n]` | C |
| `x(n)`, `DIMENSION` | Fortran |


## Real Numbers

$$
\begin{align}
	\texttt{Digit} &= \\{0,1,2,3,4,5,6,7,8,9\\} \\\\
	\mathbb{N} \cong \texttt{Natural} &= \texttt{Array}(\texttt{Digit}) \qquad 85 \cong (8,5) \\\\
	\mathbb{Z} \cong \texttt{Integer} &= \texttt{Bool} \times \texttt{Natural} \quad -85 \cong (\mathsf{T},(8,5)) \\\\
	\mathbb{Q} \cong \texttt{Rational} &= \texttt{Integer} \times \texttt{Natural} \\\\
	-8.5 &= \frac{-17}{2} \cong ((\mathsf{T},(1,7)),(2))
\end{align}
$$

Strings?


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
	f \in T \to R \\\\
	x \in T \implies f(x) \in R
$$


## Function syntax

| \\( T \to R \\)      | language          |
|--------------------|--------------------|
| `Callable[[T], R]`   | Python |
| `(x: T) => R`, `Function`  | TypeScript |
| `T -> R`  | Haskell |
| `R (*)(T)` | C (function pointer) |
| `function<R(T)>`, `Callable` | C++ |
| `Function` | Julia |


## Exercise

* How would you represent the position and mass of a particle in the 3D unit box?
* What about an arbitrary number of particles?
* What's the type of a function that calculates the center of mass for these particles?


## Types in practice

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
	R z = c;
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



