#include<math.h>
#include<stdio.h>
#include<cs50.h>

int main(void)
{
    float cash ;
    do
        {
            cash = get_float("Change owed: ");
        }
    while (cash<0);
    int cents = round(cash * 100);
    int i=0;
    while (cents>=25)
        {
            cents = (cents-25);
            i++;
        }
    while (cents>=10)
        {
            cents = (cents-10);
            i++;
        }
    while (cents>=5)
        {
            cents = (cents-5);
            i++;
        }
    while (cents>0)
        {
            cents = (cents-1);
            i++;
        }
    printf("%i", i);
}