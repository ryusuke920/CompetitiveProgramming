#include<stdio.h>
int main(void){
  long long int a, b, n;
  scanf("%lld%lld%lld",&a, &b, &n);
  if(n>=b) n=b-1;
  long long int ans=(a*n)/b;
printf("%lld\n",ans);
return 0;
}