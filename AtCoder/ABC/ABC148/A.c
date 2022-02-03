#include<stdio.h>
int main(void){
    int num1=0, num2=0, num3=0;
scanf("%d",&num1);
scanf("%d",&num2);
if(num1 != 1 && num2 !=1){
num3=1;
}else if(num1 != 2 && num2 !=2){
num3=2;
}else if(num1 != 3 && num2 !=3){
num3=3;
}
 printf("%d\n", num3);
 return 0;
}