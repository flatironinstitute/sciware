# Sciware

# Types



# Thinking about Types

(*Not* type theory)


## Types

If you think about types at all, you probably think about storage, bits:
   * `float`, `double`, `int32`, `string`

But you interact with lots of other types, too:
   * `list` (of what?), `complex`, `struct`

So what is a type?


## A type is a *set of values*

Think of a type as representing a set of possible values:

$$
\begin{align}
	\texttt{bool} &= \\{\textsf{FALSE}, \textsf{TRUE}\\} & \left|\texttt{bool}\right| &= 2 \\\\
	\texttt{uint8} &= \\{0,1,\dots,255\\} & \left|\texttt{uint8}\right| &= 2^8 \\\\
        \texttt{int32} &= \\{-2^{31},\dots,2^{31}-1\\} & \left|\texttt{int32}\right| &= 2^{32} \\\\
        \texttt{int} &\approx \mathbb{Z} \\\\
        \texttt{double} &\approx \mathbb{Q} \approx \mathbb{R}
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

* `unit` is the singleton type with only one possible value (`None` in python, `void` in C)
* `void` is the empty type with no possible values (never, impossible, a value that can never exist, the return value of a function that never returns)
* All types with the same cardinality are isomorphic (can trivially substitute one for another by replacing values)


## A set of whatever values you want

No need to limit yourself to established types!
You may have types like:

$$
	\\{1,2,3,4\\} \\\\
	\\{\textsf{YES}, \textsf{NO}, \textsf{MAYBE}\\} \\\\
	\\{\textsf{RED}, \textsf{GREEN}, \textsf{BLUE}\\} \\\\
	[0,1] \cap \texttt{double} ~ (\\{x : 0 \le x \le 1\\}) \\\\
	\mathbb{P} \cap \texttt{int} \\\\
	\mathbb{R}^+ ~ (\\{x : x \ge 0\\}) \\\\
	\texttt{double} \setminus \\{ \textsf{NaN}, \pm\textsf{Inf} \\} \\\\
	(T \setminus S = \{ x \in T : x \notin S \} = T - S)
$$


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

Can be helpful for describing and thinking about code even if the types are not perfectly represented in the programming language


## Disjoint union (sum) types

Sometimes a value can be different things, so we make a new type by combining other types with a union:

$$
	T + S = T \sqcup S \\\\
	\texttt{bool} + \texttt{uint32} = \\{\textsf{FALSE},\textsf{TRUE},0,1,2,\dots\\} \\\\
	\left|T + S\right| = \left|T\right| + \left|S\right| \\\\
	\texttt{uint8} + \texttt{uint32} = \\{0_8, 1_8, \dots, 255_8, 0_{32}, 1_{32}, \dots\\} \ne \texttt{uint8} \cup \texttt{uint32}
$$

Sometimes called a "tagged" union because values are tagged by which type they're from
