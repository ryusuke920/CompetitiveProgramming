#include<stdio.h>
int main(void){
char b[10], ch[10]={'A', 'C', 'G', 'T'};
scanf("%c", b);
for(int i=0;i<4;i++){
    if(b[0]==ch[i]){
    printf("%c\n", ch[3-i]);
    }
}
return 0;
}