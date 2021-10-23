#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

//    Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //    go thru each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //    get values of colors
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            //    Find average
            float average = (float)(r + g + b) / 3;
            int avg = (int) round(average);

            //    Replace values
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

//    Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //    go thru each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //    get values of colors
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            //    make sepia
            int sr = round(.393 * r + .769 * g + .189 * b);
            int sg = round(.349 * r + .686 * g + .168 * b);
            int sb = round(.272 * r + .534 * g + .131 * b);
            //    Checks (255) error
            if (sr < 255)
            {
                image[i][j].rgbtRed = sr;
            }
            else
            {
                image[i][j].rgbtRed = 255;
            }

            if (sg < 255)
            {
                image[i][j].rgbtGreen = sg;
            }
            else
            {
                image[i][j].rgbtGreen = 255;
            }

            if (sb < 255)
            {
                image[i][j].rgbtBlue = sb;
            }
            else
            {
                image[i][j].rgbtBlue = 255;

            }
        }
    }
    return;
}
//    Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE *holder = calloc(3, 1);
    if (holder == NULL)
    {
        return;
    }

    //    flip code
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, n = width / 2; j < n; j++)
        {
            *holder = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = *holder;
        }
    }
    free(holder);
    return;
}

//    Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_image[height][width];
    //    two loops
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int fRed = 0;
            int fGreen = 0;
            int fBlue = 0;
            int base = 0;

            //    get avg
            for (int r = -1; r <= 1; r++)
            {
                for (int c = -1; c <= 1; c++)
                {
                    //    corner case
                    if (i + r >= 0 && i + r <= height - 1 && j + c >= 0 && j + c <= width - 1)
                    {
                        fRed = fRed + image[i + r][j + c].rgbtRed;
                        fGreen = fGreen + image[i + r][j + c].rgbtGreen;
                        fBlue = fBlue + image[i + r][j + c].rgbtBlue;
                        base++;
                    }
                }
            }
            //    final
            temp_image[i][j].rgbtRed = (int) round((float) fRed / (float) base);
            temp_image[i][j].rgbtGreen = (int) round((float) fGreen / (float) base);
            temp_image[i][j].rgbtBlue = (int) round((float) fBlue / (float) base);

        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp_image[i][j];
        }
    }

    return;
}