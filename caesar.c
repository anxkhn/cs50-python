#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>


int main(int argc, string argv[])
{
    int key = 0;
    for (int i = 0; i < strlen(argv[1]); i ++)
    {
        if (isalpha(argv[1][i]))
        {
            printf ("Enter a valid input.\n");
            return 1;
        }
    }
    if (argc != 2 || atoi(argv[1]) <= 0)
    {
        // warn user and re enter
        printf("Enter a single command-line. \n");
        return 1;
    }
    else
    {
        // convert key to integer then store the key
        key = atoi(argv[1])%26;
    }
    string word = get_string("plaintext:  ");
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        // Detection and crypting of words
        int x = word[i] ;
        if (x <= 'Z' && x >= 'A')
        {
            x = x + key;
            if (x > 'Z')
            {
                x = x - 26 ;
            }
        }
        if (x <= 'z' && x >= 'a')
        {
            x = x + key;
            if (x > 122 )
            {
                x = x - 26 ;
            }
        }
        word[i] = x ;
    }
    printf("ciphertext: %s\n", word);
}