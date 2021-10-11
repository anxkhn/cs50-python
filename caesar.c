#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    int key = 0;
    if (argc != 2 || atoi(argv[1]) < 0)
    {
        // warn user and re enter
        printf("Enter a single command-line arg: non-negative integer.\n");
        return 1;
    }
    else
    {
        // convert key to integer then store the key
        key = atoi(argv[1]);
    }
    string word = get_string("plaintext:  ");
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        // Detection and crypting of words
        int x = word[i] ;
        if (x <= 'Z' && x >= 'A')
        {
            x = x + (key%26);
            if (x > 'Z')
            {
                x = x - 26 ;
            }
        }
        if (x <= 'z' && x >= 'a')
        {
            x = x + (key%26);
            if (x > 122 )
            {
                x = x - 26 ;
            }
        }
        word[i] = x ;
    }
    printf("ciphertext: %s\n", word);
}