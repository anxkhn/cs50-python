#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}


int compute_score(string word)
{
    // return score for string
    int len = strlen(word);
    //checks letters from a to z and adds POINTS
    int sum = 0;
    for (int i = 0; i < len; i++)
    {
        if (islower(word[i]))
        {
            //for debugging purposes            printf("A %i\n", word[i]);
            word[i] = word[i] - 32;
            //for debugging purposes            printf("B %i\n", word[i]);
        }

        if (word[i] <= 90 && word[i] >= 65)
        {
            //for debugging purposes            printf("C %i\n", word[i]);
            int z = word[i] - 65;
            sum = sum + POINTS[z];
            //for debugging purposes            printf("D %i\n", word[i]);
        }

    }

    //for debugging purposes
    //printf("E %i\n", sum);

    return sum;
}