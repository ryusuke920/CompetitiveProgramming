#include<stdio.h>
int main(void){
int N, ch=0;
int A[110];
scanf("%d", &N);
for(int i=0;i<N;i++){
scanf("%d", &A[i]);
if(A[i]%2==1 || A[i]%6==0 || A[i]%10==0){
ch+=1;
}
}
if(ch==N){
printf("APPROVED");
}else{
printf("DENIED");
}
return 0;
}