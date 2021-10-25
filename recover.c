#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>


typedef uint8_t  BYTE;

int main(int argc, char *argv[])
{
    // invalid command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    //error check for opening
    char *files = argv[1];
    FILE *inptr = fopen(files, "r");
    if (inptr == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }
// BUFFER SIZE
    BYTE buffer[512];
// FILE NAMING SYSTEM
    char outputjpeg[8] = "000.jpg";
// TEMP COUNTER
    int counter = 0;
// TEMP BOOL
    bool copy;
    FILE *outptr = fopen(outputjpeg, "w");
    //check 512 bites packages into the buffer
    while (fread(buffer, 512, 1, inptr) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] == 0xe0) || (buffer[3] == 0xe1)
                || (buffer[3] == 0xe2) || (buffer[3] == 0xe3) || (buffer[3] == 0xe4) || (buffer[3] == 0xe5) || (buffer[3] == 0xe6)
                || (buffer[3] == 0xe7) || (buffer[3] == 0xe8) || (buffer[3] == 0xe9) || (buffer[3] == 0xea) || (buffer[3] == 0xeb)
                || (buffer[3] == 0xec) || (buffer[3] == 0xed) || (buffer[3] == 0xee) || (buffer[3] == 0xef))
        {
            if (counter != 0)
            {
                fclose(outptr);
                sprintf(outputjpeg, "%03i.jpg", counter);
                outptr = fopen(outputjpeg, "w");
            }
            counter ++;
            copy = true;
        }
        if (copy)
        {
        fwrite(buffer, 512, 1, outptr);
        }
    }
    fclose(inptr);
    fclose(outptr);
    return 0;
}