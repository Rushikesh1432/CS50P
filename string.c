#include <stdio.h>
int main(){
    char s[1000];
    scanf("%s",&s);

    for(int i=0;s[i]!='\0';i++){
        for(int j=0;s[j]!='\0';j++){
            if(s[i]>=s[i+1]){
                char temp=s[i];
                s[i]=s[i+1];
                s[i+1]=s[i];
            }
            else{
                
            }
            
        }
    }
    printf("%s",s);
}