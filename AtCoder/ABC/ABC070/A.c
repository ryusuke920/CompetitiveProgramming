#include<stdio.h>
int main(void){
int N;
scanf("%d", &N);
if((N%100)%10 == N/100) printf("Yes\n");
else printf("No\n");
return 0;
}