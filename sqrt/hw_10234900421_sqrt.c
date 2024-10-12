#include "stdio.h"

#define eps (1e-12)
long double x;

int main() {
    printf("please input a number: ");
    scanf("%Lf", &x);

    long double p = x / 2.0;
    while ((x / p - p) > eps || (p - x / p) > eps)
        p = (p + x / p) / 2.0;

    printf("the SQRT of %Lf => %.11Lf\n", x, p);

    return 0;
}