#include<stdio.h>
int main(void){
int X;
scanf("%d", &X);
printf("%d\n",(X/500)*1000+(X%500)/5*5);
return 0;
}