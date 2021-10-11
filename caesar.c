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
        if ((word[i] <= 'Z' && word[i] >= 'A') || (word[i] <= 'z' && word[i] >= 'a'))
        {
            word[i] = word[i] + (key%26);
        }
    }
    printf("ciphertext: %s\n", word);
}