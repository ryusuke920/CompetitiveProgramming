#include<stdio.h>
int main(void){
int P, Q, R;
scanf("%d%d%d", &P, &Q, &R);
if((P+Q)<=(Q+R)&&(P+Q)<=(P+R)){
    printf("%d\n", P+Q);
}else if((Q+R)<=(P+Q)&&(Q+R)<=(P+R)){
    printf("%d\n", Q+R);
}else{
    printf("%d\n", P+R);
}
return 0;
}