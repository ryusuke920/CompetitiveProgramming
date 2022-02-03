#include<stdio.h>
int main(void){
long long N, min=9999999999999999, a, b;
scanf("%lld", &N);
for(long long i=1; i*i<=N; i++){
     if(N%i==0){
    a=i-1;
    b=(N/i)-1;
     if((a+b)<min){
    min=(a+b);
    }
  }
}
printf("%lld\n", min);
return 0;
}