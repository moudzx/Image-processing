#include <stdio.h>
#include <stdint.h>


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover path\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s\n", argv[1]);
        return 1;
    }

    uint8_t buffer[512];
    FILE *img = NULL;
    int jpg_count = 0;

    while (fread(buffer, 1, 512, card) == 512)
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 &&  buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous JPEG
            if (img != NULL)
            {
                fclose(img);
            }

            // Create filename
            char filename[8];
            sprintf(filename, "%03i.jpg", jpg_count);

            // Open new JPEG
            img = fopen(filename, "w");

            jpg_count++;
        }

        // Write block if we're inside a JPEG
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }

    if (img != NULL)
    {
        fclose(img);
    }

    fclose(card);

    return 0;
}
