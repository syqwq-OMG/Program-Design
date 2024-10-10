#include "stdio.h"

int a, b, c, d;

int main() {
    scanf("%d%d%d%d", &a, &b, &c, &d);
    if (a > b && a > c && a > d)
        printf("max val: %d\n", a);
    else if (b > c && b > d)
        printf("max val: %d\n", b);
    else if (c > d)
        printf("max val: %d\n", c);
    else
        printf("max val: %d\n", d);

    return 0;
}