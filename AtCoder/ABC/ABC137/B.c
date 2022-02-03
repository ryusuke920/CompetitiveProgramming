#include<stdio.h>
int main(void){
int K, X;
scanf("%d%d", &K, &X);
for(int i=X-K+1; i<=X+(K-1); i++){
    printf("%d\n",i);
}
return 0;
}