#include<stdio.h>
int main(void){
long long int H, W;
scanf("%lld%lld",&H, &W);
if(H==1 || W==1){
printf("1\n");
}else if(H%2==1 && W%2==1 ){
printf("%lld\n", (H*W)/2+1);
}else{
printf("%lld\n", (H*W)/2);   
}
return 0;
}