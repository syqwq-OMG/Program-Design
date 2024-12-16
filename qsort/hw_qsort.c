#include "stdio.h"
#include "time.h"
#include "stdlib.h"
#include "string.h"

const int N=50;

void swap(int *x,int *y){
    int t=*x;
    *x=*y;
    *y=t;
}

int idx(int l,int r,int choice){// l mid r 0 1 2
    if(choice==0) return l;
    if(choice==2) return r;
    return (l+r)>>1;
}

int qs(int arr[],int l,int r,int choice){
    if(l>=r) return 0;
    int x=arr[idx(l,r,choice)];
    // int x=arr[r];
    int i=l-1,j=r+1,cnt=0;
    while(i<j){
        do i++; while(arr[i]<x);
        do j--; while(arr[j]>x);
        if(i<j) swap(&arr[i],&arr[j]),cnt++;
    }
    // printf("(i:%d j:%d l:%d r:%d)",i,j,l,r);
    if(choice!=2)
        return qs(arr,l,j,choice)+cnt+qs(arr,j+1,r,choice);
    return qs(arr,l,i-1,choice)+cnt+qs(arr,i,r,choice);
}

int main(){
    int a[N+5];
    srand(time(0));
    for(int i=1;i<=N;i++) a[i]=rand()%100;

    int tmp[N+5],t;

    memcpy(tmp,a,sizeof a);
    t=qs(tmp,1,N,0);
    printf("left: %d\n",t);

    memcpy(tmp,a,sizeof a);
    t=qs(tmp,1,N,1);
    printf("mid: %d\n",t);

    memcpy(tmp,a,sizeof a);
    t=qs(tmp,1,N,2);
    printf("right: %d\n",t);

    return 0;
}