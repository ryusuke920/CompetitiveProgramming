#include<stdio.h>
int main(void){
long double a, b, c, d;
scanf("%Lf%Lf%Lf",&a, &b, &c);
d=c-a-b;
if(d>0 && d*d > 4*a*b) printf("Yes\n");
else printf("No\n");
return 0;
}
/*A=sqrt(a)*sqrt(a);//A=√a*√a
B=sqrt(b)*sqrt(b);//B=√b*√b
C=sqrt(c)*sqrt(c);//C=√c*√c
AB=2*sqrt(a)*sqrt(b);//AB=2√a*√b*/
//A+B+2√A*√B < C
//4*A*B < (C-A-B)*(C-A-B)
//4*A*B < C*C + B*B + A*A -2*(A*C + B*C - A*B)
//if(AB*AB < C*C + A*A + B*B- 2*(A*C + B*C - A*B)) printf("Yes\n");