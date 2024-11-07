#include "stdio.h"
#include "string.h"
#define N 1010

int main() {
    char p[N], s[N];
    printf("input the string:");
    scanf("%s", &s[1]);
    printf("input the substr to search:");
    scanf("%s", &p[1]);

    // for(int i=0;i<=strlen(s);i++) printf("%c",s[i]);

    int plen = strlen(&p[1]), slen = strlen(&s[1]);
    int ne[N];
    memset(ne, 0, sizeof ne);

    for (int i = 2, j = 0; i <= plen; i++) {
        while (j && p[i] != p[j + 1]) j = ne[j];
        if (p[i] == p[j + 1]) j++;
        ne[i] = j;
    }

    int flg = 0;
    for (int i = 1, j = 0; i <= slen; i++) {
        while (j && s[i] != p[j + 1]) j = ne[j];
        if (s[i] == p[j + 1]) j++;
        if (j == plen) {
            flg = 1;
            break;
        }
    }

    if (flg)
        puts("found substr in string");
    else
        puts("substr not found in string");

    return 0;
}