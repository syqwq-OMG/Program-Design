#include "stdio.h"

int main() {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);

    (a + b > c && b + c > a && c + a > b)
        ? printf("the perimeter of the triangle is: %d\n", a + b + c)
        : printf("CANNOT make up a triangle\n");

    return 0;
}
