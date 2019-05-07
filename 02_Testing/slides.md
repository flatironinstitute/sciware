# Intro to Testing Scientific Software



## What is a "test"?

* Something you can run (a program, script, function)
* ...distinct from your "real" code (unnecessary)
* ...that runs relatively quickly (while you wait)
* ...that executes some portion of your "real" code
* ...that checks something (?)
* ...and returns success if things are good, or some kind of error otherwise.


## Sanity checks, debugging assertions

Many languages provide some kind of `assert`:

```python
def assert(expr):
    if __debug__:
        if not expr: raise AssertionError
```

```c
#ifndef NDEBUG
#define assert(expr) if (!expr) abort()
#endif
```


```python
x = load_file("input")

y = process(x)

write_file("output", y)
```

A very simple kind of "test" inserts checks into an existing code flow


```python
x = load_file("input")
assert(len(x) == 345)
y = process(x)
assert(len(y) < len(x) and y[0] > 0)
write_file("output", y)
```

This validates some assumptions, but isn't very flexible (hard-coded `x`)



## How does testing apply to science?



## What do tests looks like?

```sh
#!/bin/sh
true
```


```
import mypackage

return True
```


```python
data = np.random.randn(1000)
maxlag = 5
# calculate autocovariance:
C = cnmf.pre_processing.axcov(data, maxlag)

numpy.testing.assert_allclose(C, numpy.concatenate(
    (numpy.zeros(maxlag), numpy.array([1]), numpy.zeros(maxlag))))
```
[source](https://github.com/flatironinstitute/CaImAn/blob/master/caiman/tests/test_pre_processing.py)


```c++
std::vector<int> ints = {{ 1,3,6,7,9,10,12,14 }};

for(int i = 0; i <= 30; ++i)
    {
    auto res = detail::binaryFind(ints,i);
    //Do linear search for i to check
    bool found = false;
    for(const auto& el : ints)
        if(el == i)
            {
            found = true;
            break;
            }
    if(found)
        {
        CHECK(res);
        CHECK(i == *res);
        }
    else CHECK(!res);
    }
```
[source](https://github.com/ITensor/ITensor/blob/v2/unittest/algorithm_test.cc#L31)


```python
"""
Tests that 0.25 <= xi_max(Q) <= 0.5, whatever Q
"""
Q_range = np.arange(1, 21, dtype=int)
for Q in Q_range:
    xi_max = compute_xi_max(Q)
    assert xi_max <= 0.5
    assert xi_max >= 0.25
```
[source](https://github.com/kymatio/kymatio/blob/master/kymatio/scattering1d/tests/test_filters.py#L195)


```c++
netket::Binning<double> binning(16);
std::vector<double> vals;
for (int i = 0; i < N; i++) {
    double x = GaussianWalk(x, gen, 2);
    binning << x;
    vals.push_back(x);
}

double mean = binning.Mean();
double minval = *std::min_element(vals.begin(), vals.end());
double maxval = *std::max_element(vals.begin(), vals.end());
REQUIRE(mean >= minval);
REQUIRE(mean <= maxval);
```
[source](https://github.com/netket/netket/blob/master/Test/Stats/unit-stats.cc#L59)


```python
observed = in_silico_mutagenesis_sequences("ATCCG")
expected = [
    (0, 'C'), (0, 'G'), (0, 'T'),
    (1, 'A'), (1, 'C'), (1, 'G'),
    (2, 'A'), (2, 'G'), (2, 'T'),
    (3, 'A'), (3, 'G'), (3, 'T'),
    (4, 'A'), (4, 'C'), (4, 'T')]

self.assertListEqual(observed, expected)
```
[source](https://github.com/FunctionLab/selene/blob/master/selene_sdk/predict/tests/test_model_predict.py#L12)


```c++
array<long, 2> A(2, 3);

EXPECT_THROW(A(0, 3), key_error);
EXPECT_THROW(A(range(0, 4), 2), key_error);
EXPECT_THROW(A(range(10, 14), 2), key_error);
EXPECT_THROW(A(range(), 5), key_error);
EXPECT_THROW(A(0, 3), key_error);
```
[source](https://github.com/TRIQS/triqs/blob/2.1.x/test/triqs/arrays/bound_check.cpp)


```python
m0 = matrix([[1,0],[0,2]])
m1 = matrix([[0,1],[2,0]])
A = BlockMatrix(['up','dn'],[m0,m1])

A2 = A + A
assert (A2["up"] == 2*m0).all() and (A2["dn"] == 2*m1).all(), "Addition failed"
A2 += A
assert (A2["up"] == 3*m0).all() and (A2["dn"] == 3*m1).all(), "In-place addition failed"
A2 = A - A
assert (A2["up"] == 0*m0).all() and (A2["dn"] == 0*m1).all(), "Subtraction failed"
```
[source](https://github.com/TRIQS/triqs/blob/2.1.x/test/pytriqs/base/block_matrix.py#L23)



## How do you implement tests?

#### Testing libraries

* functions, utilities for writing tests
* checks for (in)equality
* log messages, produce errors
* random input generation, looping


#### Testing frameworks

* organize, describe tests
* way to run tests (or some subset thereof)
* capture output, aggregate results

Many tools include both, and languages can include builtin features or standard libraries
