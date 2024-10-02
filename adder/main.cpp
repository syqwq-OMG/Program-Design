#include "stdio.h"
#define INT_DIGIT_NUM 32

int *half_adder(int a, int b) {
    // static int ret[2] = {a & b, a ^ b};
    static int ret[2];
    ret[0] = a & b, ret[1] = a ^ b;
    return ret;
}

int full_adder(int A, int B) {
    int ans = 0;

    int c_in = 0;
    for (int i = 0; i < INT_DIGIT_NUM - 2; i++) {
        int a = A & 1, b = B & 1;

        int *c_s = half_adder(a, b);
        ans |= ((c_s[1] ^ c_in) << i);
        c_in = c_s[0] | (c_in & c_s[1]);

        A >>= 1, B >>= 1;
    }
    ans ^= c_in << (INT_DIGIT_NUM - 1);

    return ans;
}

int main() {
    int x, y;
    scanf("%d%d", &x, &y);

    printf("%d + %d = %d\n", x, y, full_adder(x, y));

    return 0;
}
