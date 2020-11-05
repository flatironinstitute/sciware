# Improve testint.c

Take a look at the file

[testint.c](https://github.com/flatironinstitute/learn-sciware-dev/blob/master/12_Functions/examples/testint.c)

What does it do? (*Hint*: If you add a line to print `val * val / 2` at the end and run it, what do you get?)

What would a natural function be here? What are its arguments?

Write a test function that verifies that the function does what it's supposed to do.

How would you name the variables? Remember that it can be useful to split up one complex expression into several smaller ones and introduce new variables this way.

Are there natural default values for any of the arguments? If so, what would be a good way to specify it in C, since the language doesn't have a simple way to achieve this?

*Bonus*: You can pass functions (really function pointers) as arguments to other functions in C, as shown in this example
```c
#include <stdio.h>

double evaluate_at_two(double f(double)) {
    return f(2);
}

double square(double x) {
    return x * x;
}

int main(void) {
    printf("%lf\n", evaluate_at_two(square));

    return 0;
}
```

Use this to make your function even more general by allowing it to send in another function instead of `exp(-x * x / 2)`.
