#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width / 2; j++) {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++) {
         for (int j = 0; j < width; j++) {
             copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int red = 0;
            int green = 0;
            int blue = 0;
            int count = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    int row = i + di;
                    int col = j + dj;
                    if (row >= 0 && row < height && col >= 0 && col < width) {
                        red += copy[row][col].rgbtRed;
                        green += copy[row][col].rgbtGreen;
                        blue += copy[row][col].rgbtBlue; count++;
                    }
                }
            }
            image[i][j].rgbtRed = (red + count / 2) / count;
            image[i][j].rgbtGreen = (green + count / 2) / count;
            image[i][j].rgbtBlue = (blue + count / 2) / count;
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            copy[i][j] = image[i][j];
        }
    }
    int Gx[3][3] = { {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1} };
    int Gy[3][3] = { {-1, -2, -1}, { 0, 0, 0}, { 1, 2, 1} };
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int redX = 0;
            int greenX = 0;
            int blueX = 0;
            int redY = 0;
            int greenY = 0;
            int blueY = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    int row = i + di;
                    int col = j + dj;
                    if (row >= 0 && row < height && col >= 0 && col < width) {
                        int gx = Gx[di + 1][dj + 1]; int gy = Gy[di + 1][dj + 1];
                        redX += copy[row][col].rgbtRed * gx;
                        greenX += copy[row][col].rgbtGreen * gx;
                        blueX += copy[row][col].rgbtBlue * gx;
                        redY += copy[row][col].rgbtRed * gy;
                        greenY += copy[row][col].rgbtGreen * gy;
                        blueY += copy[row][col].rgbtBlue * gy;
                    }
                }
            }
            int red = round(sqrt(redX * redX + redY * redY));
            int green = round(sqrt(greenX * greenX + greenY * greenY));
            int blue = round(sqrt(blueX * blueX + blueY * blueY));
            if (red > 255) {
                 red = 255;
            }
            if (green > 255) {
                green = 255;
            } if (blue > 255) {
                blue = 255;
            }
            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
}
