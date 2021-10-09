#include<cs50.h>
#include<stdio.h>

int main(void)
{
    // User input
    int n ;
    // Loop to get output within range.
    do
    {
        n = get_int("Enter Number :\n");
    }
    while (0 >= n || n >= 9) ;
    // Loop to print output
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n - i - 1); j++)
        {
            //Prints blank Space
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            // Prints required HASH
            printf("#");
        }
        printf("  ");
        for (int j = 0; j <= i; j++)
        {
            //Prints new hash
            printf("#");
        }
        //Prints new line
        printf("\n");
    }
}