#include<stdio.h>
int main(void){
int N,a[10000], sum=0;
scanf("%d", &N);
for(int i=0;i<N;i++){
    scanf("%d",&a[i]);
    sum+=a[i];
}
printf("%d\n",sum-N);
return 0;
}