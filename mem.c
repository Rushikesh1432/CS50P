#include <stdio.h>

int main(void)
{

const float cost = 1000.00;

char inp;
printf("Are you a member:");
scanf("%c",&inp);

if(inp == 'y')
{
    char mem;
    printf(" 'g' for gold \n 's' for silver \n 'n' for none \n  ");
    printf("Which membership do you own:");
    scanf("%c",  &mem);

    if( mem == 'g')
    {
        printf("GOLD:Amt to pe paid %f",cost-(cost*0.25));
    }
    else if(mem =='s')
    {
        printf("SILVER:Amt to be paid %f",cost-(cost*0.15));
    }
    else
    {
        printf("bronze: amt to be paid %f",cost-(cost*0.1));
    }







}
else
{
    printf("NOT A MEM: Amt to be paid %f",cost-100);
}






























}