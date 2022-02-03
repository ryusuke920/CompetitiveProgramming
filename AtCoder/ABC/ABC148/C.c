#include<stdio.h>
int main(void){
long long int A,B, gcd, multi;
scanf("%lld%lld", &A, &B);
multi=A*B;
for(int i=1;i<=A && i<=B;i++){
    if(A%i==0 && B%i==0){
        gcd=i;
    }
}
printf("%lld\n", multi/gcd);
return 0;
}