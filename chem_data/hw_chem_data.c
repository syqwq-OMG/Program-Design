#include "math.h"
#include "stdio.h"
#include "string.h"

double data[] = {45, 66, 74, 32,  1,  44, 78, 32, 34, 56,  12, 98,
                 65, 34, 1,  689, 57, 45, 24, 23, 78, 278, 72, 345};

double max(double x, double y) { return x > y ? x : y; }
double min(double x, double y) { return x < y ? x : y; }

void normalize(double *arr, int len, int par) {
    double sum = 0, maxx = arr[0], minn = arr[0];
    for (int i = 0; i < len; i++)
        sum += arr[i], maxx = max(maxx, arr[i]), minn = min(minn, arr[i]);
    double mean = (double)sum / len;
    if (par == 1) {
        for (int i = 0; i < len; i++)
            arr[i] = (arr[i] - mean) / (maxx - minn);
    } else {
        double sigma = 0;
        for (int i = 0; i < len; i++)
            sigma += (arr[i] - mean) * (arr[i] - mean);
        sigma = sqrt(sigma / len);

        for (int i = 0; i < len; i++)
            arr[i] = (arr[i] - mean) / sigma;
    }
}

int main() {
    int p;
    scanf("%d", &p);
    int len = sizeof(data) / sizeof(data[0]);
    normalize(data, len, p);
    for (int i = 0; i < len; i++)
        printf("%lf ", data[i]);
    puts("");

    return 0;
}