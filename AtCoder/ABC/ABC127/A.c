#include<stdio.h>
int main(void){
int A, B;
scanf("%d%d", &A, &B);
if(A>=13){
printf("%d\n", B);
}else if(A<=5){
printf("0\n");
}else{
printf("%d\n", B/2);
}
return 0;
}