#include<stdio.h>
int main(void){
int N ,sum=0;
scanf("%d",&N);
int V[N], C[N];
for(int i=0;i<N;i++) scanf("%d",&V[i]);
for(int k=0;k<N;k++) scanf("%d",&C[k]);
for(int j=0;j<N;j++){
    if( (V[j]-C[j]) > 0 ) sum+=(V[j]-C[j]);
}
printf("%d\n",sum);
return 0;
}