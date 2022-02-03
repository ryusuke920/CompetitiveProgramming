#include<stdio.h>
int main(void){
int N ; 
long long int sum=0, count=0;
scanf("%d",&N);
for(int i=1;i<=N;i++){
    if((i%3==0) || (i%5==0) || (i%15==0)) count+=i;
    sum+=i;
}
printf("%lld\n",sum-count);
return 0;
}