#include<math.h>
#include<stdio.h>
#include<cs50.h>

int main(void)
{
    float cash ;
    do
    {
        // Get user input in x.xx format
        cash = get_float("Change owed: ");
    }
    while (cash < 0);
    int cents = round(cash * 100);
    int i = 0;
    //checks for 25 c
    while (cents >= 25)
    {
        cents = (cents - 25);
        i++;
    }
    // checks for 10 c
    while (cents >= 10)
    {
        cents = (cents - 10);
        i++;
    }
    // checks for 5 c
    while (cents >= 5)
    {
        cents = (cents - 5);
        i++;
    }
    // checks for 1 c
    while (cents >= 1)
    {
        cents = (cents - 1);
        i++;
    }
    // Prints the output
    printf("%i", i);
}