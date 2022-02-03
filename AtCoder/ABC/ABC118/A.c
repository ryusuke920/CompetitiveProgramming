#include<stdio.h>
int main(void){
int A, B;
scanf("%d%d", &A, &B);
if(B%A==0){
    printf("%d",A+B);
    }else{
        printf("%d", B-A);
    }
return 0;
}