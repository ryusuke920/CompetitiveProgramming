#include<stdio.h>
int main(void){
int N;
double sum=0.0;
scanf("%d",&N);
for(int i=1; i<=N; i++){
        sum+=i%2;
}
printf("%0.10f",sum/N);
return 0;
}