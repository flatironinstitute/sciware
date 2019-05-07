# Intro to Testing Scientific Software



## What is a "test"?

* Something you can run (a program, script, function)
* Distinct from your "real" code (unnecessary)
* That runs relatively quickly (while you wait)
* That executes some portion of your "real" code
* That checks something (?)
* And returns success if things are good, or some kind of error otherwise





## How does testing apply to science?



## How do you implement tests?

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
[source](https://github.com/ITensor/ITensor/blob/v2/unittest/algorithm_test.cc)
