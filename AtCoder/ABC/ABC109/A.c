#include<stdio.h>
int main(void){
int A,B=0;
scanf("%d%d",&A,&B);
if(A%2==1&&B%2==1){
    printf("Yes\n");
}else{
    printf("No\n");
}
return 0;
}