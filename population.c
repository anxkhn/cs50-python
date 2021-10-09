#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // i is for initial population size
    int i ;
    do
        {
            //Propmt to initial population size.
            i = get_int("What's the starting population size?\n");
        }
    while (i < 9);
    // f is for final population size
    int f ;
    do
        {
            // Prompt to ask end population size
            f = get_int("What's the final population size?\n");
        }
    while (f < i);
    // y = years required
    int y = 0 ;
    //This loop is to calculate the no of years.
    while (i < f)
        {
            i = i + ( i/3 - i/4 ) ;
            y++;
        }
    //Print number of years.
    printf("Years: %i", y);
}
