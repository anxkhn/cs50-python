#include<math.h>
#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(void)
{
    string word = get_string("Text: ");
    int len = strlen(word);
    int count_l = 0;
    int count_w = 1;
    int count_s = 0;
    for (int i = 0; i < len; i++)
    {
        if ((word[i] <= 'Z' && word[i] >= 'A') || (word[i] <= 'z' && word[i] >= 'a'))
        {
            count_l++;
        }
        if (word[i] == ' ')
        {
            count_w++;
        }
        if ((word[i] == '.') || (word[i] == '?') ||(word[i] == '!'))
        {
            count_s++;
        }
    }
    float L = count_l*100.0/count_w;
    float S = count_s*100.0/count_w;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index < 1 )
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}