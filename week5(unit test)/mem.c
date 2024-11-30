#include <stdio.h>
#include <string.h>

int main(void)   
{
    char s[1000];
    fgets(s,100,stdin);
    
    int n=strlen(s);
     for(int i=0;i<n;i++){
       for(int j=i+1;j<n;j++){
        if(s[i]>s[j]){
            int temp=s[j];
            s[j]=s[i];
            s[i]=temp;
        }}}
     printf("%s",s);
}    