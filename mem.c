#include <stdio.h>

int main(void)
{
    int n =4;
    int x=n;
    int prd=1; 


while(n>=1)
{
    while(x>=1)
    {
        prd = prd * x;
        x--;
    }
    float sum;
    float term = 1/prd;
    sum = sum + term;
    n--;

}
printf("%f",sum);

}