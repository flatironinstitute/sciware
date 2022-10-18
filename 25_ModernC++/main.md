# Sciware

## Modern C++

https://sciware.flatironinstitute.org/25_ModernC++

https://github.com/flatironinstitute/sciware/tree/main/25_ModernC++


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
   - File formats, data management, hdf5 (Nov)
- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda

- Background on status of C++ as a language and current paradigms
- Important new(ish) language and standard library features
- Time-saving and readability techniques in generic programming



# Modern C++: effective and safe(r)!

Robert Blackwell (SCC)


## Old C++: some code to modernize!

https://godbolt.org/z/69zz3j4Te


## `auto` is everywhere

```c++
    auto a = 5; // int
    auto b = 5.0f; // float
    auto c = some_function(a, b); // ??? do we care?
    ...
    auto f(double x) { return x * 2; } // returns double
    auto f(double &x) { x *= 2; }      // modifies x in place
```

* *At compile time*, automatically deduce type of an object from the right-hand-side
* Infinitely useful -- common for template types, variables with flexible types (in generic
  programming, covered later!), structured unbindings, and range based loops, but play around
  and see what's good for you


## Ranged-based `for`

```c++
    std::vector<int> a{0, 1, 2, 3, 4};
    for (auto el : a)
        std::cout << el << " ";
    std::cout << std::endl;

    for (auto &el : a)
        el = 0;
```

* Builds on the auto type. Allows you to iterate on arbitrary containers easily!
* Easily signals intent (`const`, `&`, etc.)
* Much more compact
* Allows for easy swapping of container types (`array->vector->list`), and prevents overrunning buffers


## Structured binding

```c++
    auto myfunc() { ...; return {obja, objb}; }
    ...
    auto [obja, objb] = myfunc();

    std::pair<int, double> mypair{0, 1.}; // tuple to unpack
    auto [a, b] = mypair;                 // copies of elements
    auto &[c, d] = mypair;                // References to elements in mypair

    int e; double f;                      // already bound variables
    std::tie(e, f) = mypair;              // unpack bound variables into copies
```

* Allows for multiple return values of a function
* Can generically be used to unpack structs or other ordered data (tuples, pairs, arrays, etc)


## Return-value-optimization (RVO)

```c++
    // no-no in the olden days, but golden now
    std::vector<double> gimme_big_array() { ...; return big_array; };
    ...
    // no copy. just changes the data that x points to. single allocation and no copy.
    std::vector<double> x = gimme_big_array();
```

* Avoids expensive copies from return values of objects like containers
* Changes ownership of data rather than copying it
* Usually "just works" even for composited objects (like structs, tuples, etc)
* Library developers and advanced users might need to understand "move semantics"


## Now let's put it into practice!

https://godbolt.org/z/69zz3j4Te

* `auto` keyword
* Range-based `for`
* Structured binding
* Return value optimization
