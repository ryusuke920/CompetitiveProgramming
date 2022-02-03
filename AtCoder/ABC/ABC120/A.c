#include<stdio.h>
int main(void){
int A, B, C;
scanf("%d%d%d", &A, &B, &C);
if(B/A>C){
    printf("%d",C);
}else{
    printf("%d",B/A);
}
return 0;
}