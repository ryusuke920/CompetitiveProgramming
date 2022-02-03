#include<stdio.h>
int main(void){
int N, ch=0;
scanf("%d", &N);
for(int i=1;i<=9;i++){
    for(int j=1;j<=9;j++){
       if(N != i*j){
   ch+=1;
    } 
  }
}
if(ch ==81){
  printf("No\n");
}else{
  printf("Yes\n");
}
return 0;
}