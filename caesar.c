#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    if (argc != 2)
        {
            return 1;
        }
        else
        {
        // check if the key is all numeric
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
            {
            if (isalpha(argv[1][i]))
                {
                return 1;
                }
            }
        }
    int key = atoi(argv[1])%26;
    return 0;
    string word = get_string("plaintext:  ");
    int len = strlen(word);

    for (int j = 0; j < len; j++)
    {
        // Detection and crypting of words
        int x = word[j] ;
        if (x <= 'Z' && x >= 'A')
        {
            x = x + key ;
            if (x > 'Z')
            {
                x = x - 26 ;
            }
        }
        if (x <= 'z' && x >= 'a')
        {
            x = x + key ;
            if (x > 122)
            {
                x = x - 26 ;
            }
        }
        word[j] = x ;
    }
    printf("ciphertext: %s\n", word);
}