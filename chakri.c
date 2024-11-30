#include <stdio.h>
int main(){
    int s;
    scanf("%d",&s);
    if(s%2!=0){  
    for(int i=0;i<(s/2);i++){
        for(int j=0;j<(s);j++){
            printf("S ");
        }printf("\n");}

    for(int i=0;i<(s/2);i++){
    printf("S ");
    }
    printf("O ");
for(int i=0;i<(s/2);i++){
    printf("S ");
}printf("\n");

    for(int i=0;i<(s/2);i++){
        for(int j=0;j<(s);j++){
            printf("S ");
        }printf("\n");}}
        else printf("Enter only odd numbers");

}
/*
1 2 11 17 19 1 3 

*/