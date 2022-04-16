# Sciware

# Types



# Applying Types

* *Not* type theory (a branch of mathematics involving propositional logic and category theory
* c.f., algebraic data types


## Types

If you think about types at all, you probably think about storage, bits:
   * `float`, `double`, `int32`, `string`

But you interact with lots of other types, too:
   * `list` (of what?), `complex`, `struct`, `class`

So what is a type?


## A type is a *set of values*

Think of a type as representing a set of possible values:

$$
\begin{align}
	\texttt{bool} &= \\{\textsf{FALSE}, \textsf{TRUE}\\} & \left|\texttt{bool}\right| &= 2 \\\\
	\texttt{uint8} &= \\{0,1,\dots,255\\} & \left|\texttt{uint8}\right| &= 2^8 \\\\
        \texttt{int32} &= \\{-2^{31},\dots,2^{31}-1\\} & \left|\texttt{int32}\right| &= 2^{32} \\\\
        \texttt{int} &\approx \mathbb{Z} \\\\
        \texttt{float} &\approx \mathbb{Q} \approx \mathbb{R}
\end{align}
$$

By saying \\( x \\) has type \\( T \\) we mean
$$ x \in T $$
\\( \left|T\right| \\) is the cardinality of \\( T \\): the number of possible values


## Special types

A couple simple types may seem silly but are quite useful:

$$
\begin{align}
	\texttt{unit} &= \\{()\\} & \left|\texttt{unit}\right| &= 1 \\\\
	\texttt{void} &= \emptyset = \\{\\} & \left|\texttt{void}\right| &= 0
\end{align}
$$

* `unit` is the singleton type with only one possible value (`None` in python, `Nothing` in Julia, `void` in C)
* `void` is the empty type with no possible values (never, impossible, a value that can never exist, the return value of a function that never returns)
* All types with the same cardinality are isomorphic (can trivially substitute one for another by replacing values)


## A set of values you choose

No need to limit yourself to established types!

$$
	\\{1,2,3,4\\} \qquad
	\\{\textsf{YES}, \textsf{NO}, \textsf{MAYBE}\\} \\\\
	\\{\textsf{RED}, \textsf{GREEN}, \textsf{BLUE}\\} ~ \text{(enum*)}  \\\\
	[0,1] \cap \texttt{float} ~ (\\{x : 0 \le x \le 1\\}) \\\\
	\mathbb{P} \cap \texttt{int} \qquad
	\mathbb{R}^+ ~ (\\{x : x \ge 0\\}) \\\\
	\texttt{float} \setminus \\{ \textsf{NaN}, \pm\textsf{Inf} \\} \quad
	(T \setminus S = \\{ x \in T : x \notin S \\} = T - S)
$$

\*Many languages represent finite data types with labeled values as "enumerations"


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


## Sum types (disjoint unions)

Sometimes a value can be different things, so we make a new type by combining other types with a union:

$$
\begin{align}
	T + S &= T \sqcup S \\\\
	\texttt{bool} + \texttt{uint32} &= \\{\textsf{FALSE},\textsf{TRUE},0,1,2,\dots\\} \\\\
	\left|T + S\right| &= \left|T\right| + \left|S\right| \\\\
	\texttt{uint8} + \texttt{uint32} &= \\{0_8, 1_8, \dots, 255_8, 0_{32}, 1_{32}, \dots\\} \\\\
		&\ne \texttt{uint8} \cup \texttt{uint32}
\end{align}
$$

* Sometimes called a "tagged" union because values are tagged by which type they're from
* "discriminated", unlike a C `union`: each value is either `T` or `S` (and you can tell)


## Type parameters, more syntax

* Types can have parameters (arguments) of other types
* \\(+\\) is an operator (function) that builds existing types into a new one: \\( T+S = \textsf{Union}(T,S) \\)
* Different languages have different syntax for these parameterized types (and different names for unions):

| \\( T + S \\)      | language          |
|--------------------|--------------------|
| `Union[T,S]`   | Python |
| `Union<T,S>` (`T\|S`)    | TypeScript |
| `Union{T,S}`  | Julia |
| `Either T S`  | Haskell |
| `variant<T, S>`    | C++ |


## More simple types

* Adding \texttt{unit} to a type is often useful

$$
	\texttt{unit} + \texttt{T} = \\{(), \dots\\} \\\\
	\texttt{unit} + \texttt{bool} = \\{(), \textsf{F}, \textsf{T}\\}
$$

* Provides a "missing" option (`NULL`, `None`, `nothing`, `NA`)
* Often has a special name: `Optional[T] = Union[T,None]`


## Product types

* Unions can only have one value, either one type or the other
* Products allow one value from each time
* Represents every possible combination of two types (cross product, outer product)

$$
\begin{align}
	T \times S &= \\{ (x, y) : x \in T, y \in S \\} \\\\
	\texttt{bool} \times \texttt{uint8} &= \\{(\textsf{F},0),(\textsf{T},0),(\textsf{F},1),(\textsf{T},1),\dots\\} \\\\
	\left|T \times S\right| &= \left|T\right|\left|S\right| \\\\
	\texttt{float} \times \texttt{float} &\approx \mathbb{R}^2 = \mathbb{R} \times \mathbb{R}
\end{align}
$$

* Often represented by pairs or tuples: `(T,S)`, `T*S`, `Tuple[T,S]`, `pair<T,S>`


## Larger (and smaller) tuples

$$
	\prod_{i=1}^n T_i = T_1 \times T_2 \times \cdots \times T_n = \texttt{Tuple}(T_1, T_2, \dots, T_n) \\\\
		= \\{ (x_1,\dots,x_n) : x_1 \in T_1, \dots, x_n \in T_n \\} \\\\
	\texttt{Tuple}() = ? \\\\
	\left| \texttt{Tuple}() \right| = \prod_{i=1}^0 \left|T_i\right| = 1 \\\\
	\texttt{Tuple}() = \texttt{unit} = \\{()\\}
$$


## Empty sum?

$$
	\sum_{i=1}^0 T_i = \texttt{void}
$$

* Julia: `Union{}`


## Functions


