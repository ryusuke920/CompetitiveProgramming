#include<stdio.h>
int main(void){
int N ,M ,sum=0, count=0;
scanf("%d%d",&N,&M);
int A[M];
for(int i=0;i<M;i++) {
    scanf("%d",&A[i]);
    sum+=A[i];
}
if(N-sum<0) printf("-1\n");
else printf("%d\n",N-sum);
return 0;
}