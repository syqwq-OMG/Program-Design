#include "stdio.h"

int a0, a1, b0, b1, s = 0, c_in = 0, ans = 0;

int main() {
    printf("A0=");
    scanf("%d", &a0);
    printf("A1=");
    scanf("%d", &a1);
    printf("B0=");
    scanf("%d", &b0);
    printf("B1=");
    scanf("%d", &b1);

    s = a0 ^ b0 ^ c_in;
    ans |= (s << 0);
    c_in = (a0 & b0) | ((a0 ^ b0) & c_in);

    s = a1 ^ b1 ^ c_in;
    ans |= (s << 1);
    c_in = (a1 & b1) | ((a1 ^ b1) & c_in);

    ans |= c_in << 2;

    printf("%d%d+%d%d=", a1, a0, b1, b0);
    if (ans >> 2)
        printf("%d%d%d\n", ans >> 2, (ans >> 1) & 1, ans & 1);
    else
        printf("%d%d\n", (ans >> 1) & 1, ans & 1);

    return 0;
}