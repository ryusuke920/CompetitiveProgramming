#include<stdio.h>
int main(void){
long long A, B, K;
scanf("%lld %lld %lld",&A, &B, &K);
if(A+B<=K){
    printf("0 0\n");
}else if(K>=A){
    printf("0 %lld\n", B-K+A);
}else{
    printf("%lld %lld\n", A-K, B);
}
return 0;
}