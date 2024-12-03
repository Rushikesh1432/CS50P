#include <stdio.h>
int main(){
   int s[10]={100,28,3,4,5,60,70,8,9,10};//Randomly arranged Array
    char c,m=1;
    for(int j=0;j<10;j++){//Outer loop
    c=0;
    for(int i=0;i<10-j;i++){//inner loop
    
        if((s[i]>s[i+1]) && i!=(10-1)){
            int temp = s[i];
            s[i]=s[i+1];
            s[i+1]=temp;
            c=1;
            printf("%d ",m++);
            
        }
        else continue;
    }
    if(c==0) break;}
    printf("\n");
for(int i=0;i<10;i++) printf("%d ",s[i]);


}