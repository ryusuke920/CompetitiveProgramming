#include<stdio.h>
int main(void){
int N, sum=0;
scanf("%d",&N);
/*while(N){
    dig= N%10;
    sum+=dig;
    N/=10;
}*/
for(int i=0;i<=N;i++){
if(i>=1 && i<=9){
     sum++;
}else if(i>=100 && i<=999) {
    sum++;
}else if  (i>=10000 && i<=99999) {
    sum++;
}
}
printf("%d\n",sum);
return 0;
}