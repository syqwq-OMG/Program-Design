#include <float.h> // FLT_EPSILON
#include <math.h>  // fabs()
#include <stdio.h>
#include <stdlib.h> //malloc()
#define EPS 0.2     // eps range
#define INF 0x3f3f3f3f

int main() {
    int n;
    int maxx = -INF, minn = INF;
    float sum = 0.0f, mean;

    printf("please input len of numbers(int):");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    float *ol = (float *)malloc(n * sizeof(float));

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (int i = 0; i < n; i++)
        maxx = maxx < arr[i] ? arr[i] : maxx,
        minn = minn > arr[i] ? arr[i] : minn;

    for (int i = 0; i < n; i++) {
        ol[i] = (float)(arr[i] - minn) / (maxx - minn), sum += ol[i];
        printf("%.6f ", ol[i]);
    }
    puts("");
    mean = sum / n;
    printf("--mean=%.6f--allow eps:%.6f--\n", mean, EPS);

    for (int i = 0; i < n; i++) {
        float eps = fabs(ol[i] - mean);
        if (eps > EPS)
            printf("Outlier point:%.6f, eps:%.6f\n", ol[i], eps);
    }

    return 0;
}