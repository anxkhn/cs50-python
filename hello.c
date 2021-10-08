#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //This is to get user's name
    string name = get_string("Hey, What is your name?\n");
    //This prints output with user's name
    printf("Hello, %s it's so nice to meet you!\n", name);
}