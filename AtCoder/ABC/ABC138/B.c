#include<stdio.h>
int main(void){
int a, N;
scanf("%d", &N);
double sum=0;
for(int i=0;i<N;i++){
    scanf("%d", &a);
    sum+=(double)1/a;
}
printf("%.6f\n",1/sum);
return 0;
}