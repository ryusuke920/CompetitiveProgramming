#include<stdio.h>
int main(void){
int A, B;
scanf("%d%d", &A, &B);
if(A+B >= A-B && A+B >= A*B){
    printf("%d", A+B);
}else if(A-B >= A+B && A-B >= A*B){
    printf("%d", A-B);
}else{
    printf("%d", A*B);
}
return 0;
}