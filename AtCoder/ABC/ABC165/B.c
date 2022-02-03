#include<stdio.h>
int main(void){
    long long int X;
    int count=0;
    scanf("%lld",&X);
    for(long long int i=100;i<X; count++){
        i*=1.01;
    }
    printf("%d\n",count);
return 0;
}