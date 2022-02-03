#include<stdio.h>
int main(void){
int n;
scanf("%d",&n);
char A[n], B[n];
scanf("%s%s", A, B);
for(int i=0; i<n; i++){
    printf("%c%c", A[i], B[i]);
}
printf("\n");
return 0;
}