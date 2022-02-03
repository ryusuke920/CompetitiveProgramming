#include<stdio.h>
int main(void){
long a;
char s[11];
scanf("%d%s", &a, s);
if(a>=3200){
printf("%s\n", s);
}else{
 printf("red\n");   
}
return 0;
}