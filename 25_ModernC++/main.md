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



# Working with data effectively and safely

Robert Blackwell (SCC)


## auto

* In variable declaration, automatically deduce type of an object from the right-hand-side
* Extremely useful for complicated template types, variables with flexible types (in generic
  programming, covered later!), structured unbinding, and range based loops
* In C++14, also can be the return type of a function

```c++
    auto a = 5; // int
    auto b = 5.0f; // float
    auto c = some_function(a, b); // ??? do we care?
```


## ranged based for

* Builds on the auto type. Allows you to iterate on arbitrary containers easily!
* Can also loop over references, and more
* Doesn't care about container type, so long as it's iterable
* Allows for easy swapping of container types (array->vector->list), and prevents overrunning buffers
* Easily signals intent (const, by ref, etc)
* Much more compact

```c++
    std::vector<int> a{0, 1, 2, 3, 4};
    for (auto el : a)
        std::cout << el << " ";
    std::cout << std::endl;

    for (auto &el : a)
        el = 0;
```


## Structured binding

* Allows for multiple return values of a function
* Can generically be used to unpack structs or other ordered data (tuples, pairs)
* `std::tie` can be used if you know the types to unpack or otherwise wish to return into
  existing variables

```c++
    auto myfunc() { return {obj1, obj2}; }
    auto [obja, objb] = myfunc();

    std::tuple<int, int, double> mytup{0, 1, 2.};   // tuple to unpack
    int a, b; double c;                             // already bound variables
    std::tie(a, b, c) = mytup;                      // unpack bound variables into copies
    auto [e, f, g] = mytup;                         // copies of elements
    auto &[h, i, j] = mytup;                        // References to elements in mytup
```


## Return-value-optimization (RVO)

* Avoids expensive copies from return values of objects like containers
* Allows for fast returning of values rather than passing in object pointers/references as
  arguments and modifying them (as in the early C++ days)
* Essentially works by allocating data and "moving" it rather than copying it, i.e. changing
  the object that owns the data
* Usually "just works" even for composited objects (like structs, tuples, etc). Library
  developer types who make custom containers and other big objects might need to understand
  "move semantics"

```c++
    std::vector<double> gimme_big_array() { ...; return big_array; }; // no-no in the olden days
    ...
    std::vector<double> x = gimme_big_array(); // no copy. just changes the data that x points to.
```


## Live coding example
