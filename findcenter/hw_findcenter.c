#include "stdio.h"
#include "stdlib.h"

int n;

int dis(int i1, int i2, int *tx, int *ty) {
    int x1 = tx[i1], x2 = tx[i2], y1 = ty[i1], y2 = ty[i2];
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

int dis_sum(int idx, int *tx, int *ty, int len) {
    int sum = 0;
    for (int i = 1; i <= len; i++)
        sum += dis(idx, i, tx, ty);
    return sum;
}

int main() {
    printf("input points number: ");
    scanf("%d", &n);

    int *x = (int *)malloc(sizeof(int) * (n + 1));
    int *y = (int *)malloc(sizeof(int) * (n + 1));

    printf("input point x: ");
    for (int i = 1; i <= n; i++)
        scanf("%d", &x[i]);

    printf("input point y: ");
    for (int i = 1; i <= n; i++)
        scanf("%d", &y[i]);

    puts("finding...");

    int idx = 1, minn = dis_sum(1, x, y, n);
    for (int i = 2; i <= n; i++) {
        int t = dis_sum(i, x, y, n);
        if (t < minn)
            idx = i, minn = t;
    }

    printf("center point: (%d, %d)\n", x[idx], y[idx]);

    free(x);
    free(y);

    return 0;
}