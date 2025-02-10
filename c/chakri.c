
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    char* name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
int vote(char* name);
void print_winner(void);

int main(int argc, char* argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = scanf("%d");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        char* name = scanf("%s");

        // Check for invalid vote
        if (vote(name)==1)
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
int vote(char* name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return 0;
        }
    }

    return 1;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int totalVotes = 0;

    // Check to see who has the highest number of votes
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > totalVotes)
        {
            totalVotes = candidates[i].votes;
        }
    }

    // Prints the names of who has the highest number of votes
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == totalVotes)
        {
            printf("%s\n", candidates[i].name);
        }
    }
}
