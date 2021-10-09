#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // First prompt to enter the population size
    int i ;
    do
        {
            i = get_int("What's the starting population size?\n");
        }
    while (i < 9);
    int f ;
    do
        {
            // Prompt to take end population size
            f = get_int("What's the final population size?\n");
        }
    while (f < i);
    // y = years required
    int y = 0 ;
    // this loop checks for difference to be zero and increments the years on each round
    int d = f - i ;
    while (d > 0)
        {
            d = (d - i/3 + i/4) ;
            y++;
        }
        // TODO: Print number of years
    printf("Years: %i", y);
}
