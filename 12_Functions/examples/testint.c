/* gcc -o testint testint.c -lm */

#include <stdio.h>
#include <math.h>

int main(void) {
    double val;

    val = 0;
    for(size_t i = 0; i < 100; ++i) {
        double temp;
        temp = -2+4*(i/100.0);
        val += exp(-temp*temp/2)*4/100.0;
    }
    printf("-2, 2, 100 = %.15lf\n", val);

    val = 0;
    for(size_t i = 0; i < 1000; ++i) {
        double temp;
        temp = -2+4*(i/1000.0);
        val += exp(-temp*temp/2)*4/1000.0;
    }
    printf("-2, 2, 1000 = %.15lf\n", val);

    val = 0;
    for(size_t i = 0; i < 1000; ++i) {
        double temp;
        temp = -4+8*(i/1000.0);
        val += exp(-temp*temp/2)*8/1000.0;
    }
    printf("-4, 4, 1000 = %.15lf\n", val);

    val = 0;
    for(size_t i = 0; i < 10000; ++i) {
        double temp;
        temp = -4+8*(i/10000.0);
        val += exp(-temp*temp/2)*8/10000.0;
    }
    printf("-4, 4, 10000 = %.15lf\n", val);

    val = 0;
    for(size_t i = 0; i < 10000; ++i) {
        double temp;
        temp = -8+16*(i/10000.0);
        val += exp(-temp*temp/2)*16/10000.0;
    }
    printf("-8, 16, 10000 = %.15lf\n", val);

    return 0;
}
