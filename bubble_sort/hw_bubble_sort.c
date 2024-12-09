#include "stdio.h"

void swap(int* x,int* y){
    int t=*x;
    *x=*y;
    *y=t;
}
#define swap(_x,_y) swap(&(_x),&(_y))

int sort(int* arr, int len){
    int cnt=0;
    for(int i=0;i<len;i++)
        for(int j=0;j<i;j++)
            if(arr[j]>arr[i])
                swap(arr[j],arr[i]),cnt++;
    return cnt;
}

int main(){
    int a[]={64, 22,34, 25, 12, 22, 11, 90,100};
    int l=sizeof(a)/sizeof(a[0]);
    int c=sort(a,l);

    for(int i=0;i<l;i++) printf("%d ",a[i]);
    puts("");
    printf("swap times: %d\n",c);

    return 0;
}