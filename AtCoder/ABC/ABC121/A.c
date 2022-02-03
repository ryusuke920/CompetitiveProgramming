#include<stdio.h>
int main(void){
int H, W, h ,w;
scanf("%d%d%d%d", &H, &W, &h, &w);
printf("%d\n", H*W-(h*W+w*H-h*w));
return 0;
}