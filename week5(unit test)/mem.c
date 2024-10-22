#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d",&n);
    float sum=0;
    


while(n>=1)
{
    int x=n;
    int prd=1; 
    while(x>=1)
    {
        prd = prd * x;
        x--;
    }
    
   
    sum = sum + (1.0/prd);
    n--;

}
printf("%.5f",sum);

}