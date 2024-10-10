#include "stdio.h"

// 31 28/29 31 30 31 30 31 31 30 31 30 31
int yy, mm, dd, ans = 0;

int main() {
    int zero = 0, jan = zero + 31, feb = jan + 28;

    printf("input year: ");
    scanf("%d", &yy);

    if ((yy % 100 == 0 && yy % 400 == 0) || (yy % 100 != 0 && yy % 4 == 0))
        feb += 1;

    int march = feb + 31,
        april = march + 30, may = april + 31, june = may + 30, july = june + 31,
        aug = july + 31, sept = aug + 30, oct = sept + 31, nov = oct + 30;

    printf("input month: ");
    scanf("%d", &mm);
    printf("input date: ");
    scanf("%d", &dd);

    if (mm == 1)
        ans += zero;
    else if (mm == 2)
        ans += jan;
    else if (mm == 3)
        ans += feb;
    else if (mm == 4)
        ans += march;
    else if (mm == 5)
        ans += april;
    else if (mm == 6)
        ans += may;
    else if (mm == 7)
        ans += june;
    else if (mm == 8)
        ans += july;
    else if (mm == 9)
        ans += aug;
    else if (mm == 10)
        ans += sept;
    else if (mm == 11)
        ans += oct;
    else
        ans += nov;

    ans += dd;

    printf("%d-%d-%d is the %d th day of the year\n", yy, mm, dd, ans);

    return 0;
}