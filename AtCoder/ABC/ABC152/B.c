#include<stdio.h>
int main(void){
int a, b, ch=0, A, B=0;
scanf("%d%d", &a , &b);
A=a;
B=b;
for(int i=1;ch<A;i*=10){
    a+=i*B;
    ch++;
}
ch=0;
for(int i=1;ch<b;i*=10){
    B+=i*A;
    ch++;
}
if(A>b){
    printf("%d",a-A);
}else{
    printf("%d", B-b);
}
return 0;
}