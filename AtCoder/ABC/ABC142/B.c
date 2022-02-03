#include<stdio.h>
int main(void){
int N, K, sum=0;
scanf("%d%d", &N, &K);
int h[N];
for(int i=0;i<N;i++){
scanf("%d", &h[i]);
if(h[i]>=K){
    sum+=1;
  }
}
printf("%d", sum);
return 0;
}