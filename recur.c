#include <stdio.h>
int main(int a){
    
 
    int j=a;
    int prd=1;
    while(a>0){
        prd=prd*a;
        a--;
    }
    printf("%d\n",prd);
    j--;
    
    
        main(j);
    
    

    
}