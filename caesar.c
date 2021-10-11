#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    // checking if there exsist two arguments (one caesar.c and other is user input)
    if (argc != 2)
    {
        return 1;
    }
    else
    {
        // checking if the input is valid (numeric only)
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (isalpha(argv[1][i]))
            {
                return 1;
            }
        }
    }
    // atoi = convert input string to an int variable
    int key = atoi(argv[1]) % 26 ;
    // ask user input for encryption word
    string word = get_string("plaintext:  ");
    // get user input world lenght
    int len = strlen(word) ;
    //loop to repeat for every index of string
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
    // print output text
    printf("ciphertext: %s\n", word);
}