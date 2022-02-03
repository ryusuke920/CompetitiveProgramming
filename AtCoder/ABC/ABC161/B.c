#include<stdio.h>
int main(void){
int N ,M ,sum=0, count=0;
scanf("%d%d",&N,&M);
int A[N];
for(int i=0;i<N;i++) {
    scanf("%d",&A[i]);
    sum+=A[i];//総得票数
}
for(int i=0;i<N;i++){
    if(A[i]*(4*M) >= sum ) count++;
}
if(count>=M) printf("Yes\n");
else printf("No\n");
return 0;
}