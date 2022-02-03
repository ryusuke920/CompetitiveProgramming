#include<stdio.h>
int main(void){
int N, A, B;
scanf("%d%d%d", &N, &A, &B);
if( (N*A)>=B ){
printf("%d\n",B);
}else{
printf("%d\n",N*A);
}
return 0;
}