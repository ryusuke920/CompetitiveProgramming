#include<stdio.h>
int main(void){
int N, dig, sum=0, NN;
scanf("%d", &N);
NN=N;
while(N){
    dig=N%10;
    sum+=dig;
    N/=10;
}
if(NN%sum==0) printf("Yes\n");
else printf("No\n");
return 0;
}