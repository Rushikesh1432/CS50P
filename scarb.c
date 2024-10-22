#include <stdio.h>

#include <string.h>
#include <ctype.h>

 int scores[]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
 int super(string word);

int main(void)
{
    char *player1;
    scanf("%c",&player1);
    char *player2;
    scanf("%c",&player2);
    //string player1 = get_string("player1:");
    //string player2 = get_string("player2:");
    int a=super(player1);
    int b=super(player2);

    if(a>b)
    {
        printf("player 1 wins\n");
    }
    else if(a<b)
    {
        printf("player 2 wins\n");

    }
    else
    {
        printf("draw\n");
    }

}

int super(char* word)
{
    int score=0;

    for(int i=0;i<strlen(word);i++)
    {
        if(isupper(word[i]))
        {
            score += scores[word[i]-'A'];
        }

        if(islower(word[i]))
        {
            score += scores[word[i]-'a'];
        }

    }
    return score;
}