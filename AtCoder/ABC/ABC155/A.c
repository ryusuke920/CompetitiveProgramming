#include<stdio.h>
int main(void){
int A, B, C;
scanf("%d%d%d",&A, &B, &C);
if((A==B && B==C && C==A)|| (A!=B && B!=C && C!=A)){
    printf("No\n");
}else{
    printf("Yes\n");
}
 return 0;
}