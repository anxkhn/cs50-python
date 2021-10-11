#include<math.h>
#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(void)
{
    //Request user to enter some text
    string word = get_string("Text: ");
    //Get String Length (for loops)
    int len = strlen(word);
    // Initial number of letters
    int count_l = 0;
    // Inital number of words = Spaces + 1 (logical)
    int count_w = 1;
    // Initial bumber of sentences
    int count_s = 0;
    for (int i = 0; i < len; i++)
    {
        // Detection and counting of letters
        if ((word[i] <= 'Z' && word[i] >= 'A') || (word[i] <= 'z' && word[i] >= 'a'))
        {
            count_l++;
        }
        // Detection and counting of words
        if (word[i] == ' ')
        {
            count_w++;
        }
        // Detection and countings of sentences
        if ((word[i] == '.') || (word[i] == '?') || (word[i] == '!'))
        {
            count_s++;
        }
    }
    // average number of letters per 100 words in the text
    float L = count_l * 100.0 / count_w;
    //average number of sentences per 100 words in the text
    float S = count_s * 100.0 / count_w;
    // Coleman-Liau index calculation (with rounding to nearest integer)
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    // Print Before Grade 1
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    // Print Grade 16+
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    // Print Grade (1-15 cases)
    else
    {
        printf("Grade %i\n", index);
    }
}