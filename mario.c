#include<cs50.h>
#include<stdio.h>

int main(void)
{
    // User input
    int n ;
    do
    {
        n = get_int("Enter Number :\n");
    }
    while ( 0 >= n || n >= 9 ) ;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n-i-1); j++)
        {
            printf(".");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
    printf("\n");
    }
}