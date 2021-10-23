#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Extract values of colors
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Find average
            int avg = ceil(((r+g+b) / 3));

            // Replace original rgb values with average
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Extract values of colors
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // make sepia
            int sr = ceil(.393 * r + .769 * g + .189 * b);
            int sg = ceil(.349 * r + .686 * g + .168 * b);
            int sb = ceil(.272 * r + .534 * g + .131 * b);
            // Checks to make sure each rgb value is valid (less then 255) and replaces it. Else sets to 255
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
// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
