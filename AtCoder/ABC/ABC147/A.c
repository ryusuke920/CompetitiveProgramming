#include<stdio.h>
int main(void){
    int num1=0, num2=0, num3=0, sum=0;
scanf("%d",&num1);
scanf("%d",&num2);
scanf("%d",&num3);
sum=num1 + num2 + num3;
if(sum >= 22){
printf("bust\n");
}else {
printf("win\n");
}
 return 0;
}