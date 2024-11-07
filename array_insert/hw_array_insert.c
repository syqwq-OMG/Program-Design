#include <stdio.h>
#define SIZE 11
int main() {
    int bajianArray[SIZE] = {11, 12, 15, 19, 23, 26, 29, 38, 40, 100};
    int temp1, temp2, number;
    printf("\narray is:\n");
    for (int i = 0; i < 10; i++)
        printf("%5d", bajianArray[i]);
    printf("\n\nplease input the number to be inserted:");
    scanf("%d", &number);
    /*
        请补充代码使得，有序数组在插入一个新的数字之后，依然有序！！！
        注意前后的代码不能改变。
    */

    int *bja = bajianArray;
    bja[SIZE - 1] = number;
    int i = SIZE - 1;
    while (bja[i] < bja[i - 1])
        bja[i] ^= bja[i - 1], bja[i - 1] ^= bja[i], bja[i] ^= bja[i - 1], i--;

    for (int i = 0; i < 11; i++)
        printf("%5d", bajianArray[i]);
    printf("\n");
    return 0;
}