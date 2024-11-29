#include "stdio.h"

#define N 100010
int f[N][3]; // RGB

int main() {
    int n;
    scanf("%d", &n);

    f[1][0] = f[1][1] = f[1][2] = 1;

    for (int i = 2; i <= n; i++) {
        f[i][0] = f[i - 1][1] + f[i - 1][2];
        f[i][1] = f[i - 1][2];
        f[i][2] = f[i - 1][0] + f[i - 1][1] + f[i - 1][2];
    }

    printf("total ways: %d %d", f[n][0] + f[n][1] + f[n][2]);

    return 0;
}