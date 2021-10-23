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
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Find average
            float average = (float)(red + green + blue) / 3;
            int average1 = (int) round(average);

            // Replace original rgb values with average
            image[i][j].rgbtRed = average1;
            image[i][j].rgbtGreen = average1;
            image[i][j].rgbtBlue = average1;
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
            // Find values of original rgb
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // FInd new sepia toned rgb values
            int sepiaRed = round(.393 * red + .769 * green + .189 * blue);
            int sepiaGreen = round(.349 * red + .686 * green + .168 * blue);
            int sepiaBlue = round(.272 * red + .534 * green + .131 * blue);

            // Checks to make sure each rgb value is valid (less then 255) and replaces it. Else sets to 255
            if (sepiaRed < 255)
            {
                image[i][j].rgbtRed = sepiaRed;
            }
            else
            {
                image[i][j].rgbtRed = 255;
            }

            if (sepiaGreen < 255)
            {
                image[i][j].rgbtGreen = sepiaGreen;
            }
            else
            {
                image[i][j].rgbtGreen = 255;
            }

            if (sepiaBlue < 255)
            {
                image[i][j].rgbtBlue = sepiaBlue;
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

    RGBTRIPLE *holder = calloc(3, 1);
    if (holder == NULL)
    {
        return;
    }

    // Iterates though each row and each column for half way
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

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_image[height][width];
    // First 2 loops iterate through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int finalRed = 0;
            int finalGreen = 0;
            int finalBlue = 0;
            int counter = 0;

            // Iterate through each neighbor around the pixel you're looking at
            for (int r = -1; r <= 1; r++)
            {
                for (int c = -1; c <= 1; c++)
                {
                    // If the i-value or j-value is invalid, ignore the pixel
                    if (i + r >= 0 && i + r <= height - 1 && j + c >= 0 && j + c <= width - 1)
                    {
                        finalRed = finalRed + image[i + r][j + c].rgbtRed;
                        finalGreen = finalGreen + image[i + r][j + c].rgbtGreen;
                        finalBlue = finalBlue + image[i + r][j + c].rgbtBlue;
                        counter++;
                    }
                }
            }
            // At the end of looking at all the neighbors, total up and average out the pixel's triple values and store in temp image
            temp_image[i][j].rgbtRed = (int) round((float) finalRed / (float) counter);
            temp_image[i][j].rgbtGreen = (int) round((float) finalGreen / (float) counter);
            temp_image[i][j].rgbtBlue = (int) round((float) finalBlue / (float) counter);

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
