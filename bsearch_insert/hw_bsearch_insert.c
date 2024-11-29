#include "stdio.h"
#include "stdlib.h"

void display(int *arr, int len) {
    printf("[+] now arr: < ");
    for (int i = 1; i <= len; i++)
        printf("%d ", arr[i]);
    puts(">");
}

void swap(int *x, int *y) {
    int t = *x;
    *x = *y;
    *y = t;
}
#define swap(_x, _y) swap(&(_x), &(_y))

void insert(int x, int *arr, int *len) {
    int p = ++(*len);
    arr[p] = x;
    while (p > 1 && arr[p] < arr[p - 1]) {
        swap(arr[p], arr[p - 1]);
        p--;
    }
    display(arr, *len);
}
#define insert(_x, _arr, _len) insert(_x, _arr, &(_len))

// find index of biggest element
// leq than x in a sorted array
int bs(int x, int *arr, int len) {
    int l = 1, r = len;
    while (l < r) {
        int mid = (l + r + 1) >> 1;
        if (arr[mid] <= x)
            l = mid;
        else
            r = mid - 1;
    }
    return l;
}

int main() {
    int n, l = 0;
    printf("[?] input times: ");
    scanf("%d", &n);
    int *a = (int *)malloc((n + 1) * sizeof(int));

    for (int i = 1; i <= n; i++) {
        int t;
        printf("[?] input num to add: ");
        scanf("%d", &t);
        int idx = bs(t, a, l);
        if (idx == 0 || a[idx] != t)
            insert(t, a, l);
        else
            printf("[x] %d is already in arr!\n", t);
    }

    free(a);

    return 0;
}