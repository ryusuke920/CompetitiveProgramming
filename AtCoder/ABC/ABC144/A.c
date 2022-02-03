#include<stdio.h>
int main(void){
int n1,n2,sum;
scanf("%d%d",&n1,&n2);
if((n1>=1 && n1<=9) &&(n2>=1 && n2<=9)){
sum=n1*n2;
printf("%d",sum);
}else {
printf("-1");
}
return 0;
}