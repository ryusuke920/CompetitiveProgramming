#include<stdio.h>
int main(void){
int A[3], ch, a, b, c;
for(int i=0;i<3;i++){
scanf("%d",&A[i]);//昇順に並べる
}
for(int i=0;i<3;i++){
    for(int j=i+1;j<3;j++){
        if(A[i]>A[j]){
    ch=A[j];
    A[j]=A[i];
    A[i]=ch;
        }
    }
}
a=A[1]-A[0];
b=A[2]-A[1];
c=A[2]-A[0];

if(a+b>=a+c && b+c>=a+c)printf("%d\n",a+c);
else if(a+c>=a+b && b+c>=a+b)printf("%d\n",a+b);
else printf("%d\n",b+c);
return 0;
}