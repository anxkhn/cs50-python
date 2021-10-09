#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // First prompt to enter the population size
    int n = get_int("What's the starting population size?\n");
    int x = 0;
    do
        {
            // Checks if in the first run , the value needes to be updated. Else increment x.
            if (x>0)
                {
                    n = get_int("Starting population size too low, please enter a higher value.\n");
                }
            else
                {
                    x++;
                }
        }
    while (n < 9);
    // Prompt to take end population size
    int f = get_int("What's the ending population size?\n");
    // TODO: Calculate number of years until we reach threshold
    // d = difference variable
    int d = f - n;
    if (d < 0)
        {
            printf("Invalid Input\n");
        }
    else
        {
            // y = years required
            int y = 0 ;
            // this loop checks for difference to be zero and increments the years on each round
            while (d >= 0)
                {
                    d = (d - y/3 + y/4) ;
                    y++;
                }

            // TODO: Print number of years
            printf("Years:%i\n", y);
        }
}
