#include "stdio.h"
#include "string.h"
#define N 100010

int main(){
    int k;
    char s[N],cs[N];
    printf("please input the key:\n"); scanf("%d",&k);
    printf("please input the string(only include a-z A-Z):\n"); scanf("%s",s);

    int len=strlen(s),p='z'-'a'+1;
    cs[len]='\0';
    for(int i=0;i<len;i++){
        char t=s[i];
        if(t>='a'&&t<='z'){
            t='a'+(t-'a'+k)%p;
            t+='A'-'a';
        }else if(t>='A'&&t<='Z'){
            t='A'+(t-'A'+k)%p;
            t+='a'-'A';
        }
        cs[i]=t;
    }

    printf("after encoder: %s",cs);

    return 0;
}