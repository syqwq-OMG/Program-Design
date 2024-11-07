#include "stdio.h"
#include "string.h"
#define N 1010

int main() {
    char p[N], s[N];
    printf("input the string:"); scanf("%s", s);
    printf("input the substr to search:"); scanf("%s", p);

    int flg = 0, lenp = strlen(p), lens = strlen(s);
    for(int i=0;i<=lens-lenp && !flg;i++){
        flg=1;
        for(int j=0;j<lenp;j++)
            if(s[i+j]!=p[j]) { flg=0;break; }
    }

    if (flg) puts("FOUND substr in string");
    else puts("substr NOT found in string");

    return 0;
}