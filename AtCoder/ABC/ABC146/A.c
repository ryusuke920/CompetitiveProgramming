#include<stdio.h>
int main(void){
char s[4], date[8][4]={"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
scanf("%s",s);
for(int i=0;i<7;i++){
    if(date[i][0] == s[0] && date[i][1] ==s[1]){
printf("%d\n", 7-i);
    }
}
 return 0;
}