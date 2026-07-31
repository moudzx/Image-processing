# Image-processing

Raw image recovery and 24-bit BMP images filter library in C & Python-matplotlib based digital image processing toolkit.

## Python

### Digital Image Processing (CS/ECE 454) Workshop by Prof. Emmanuel Agu

<img width="1080" height="1080" alt="photo_2026-06-22_07-55-42" src="https://github.com/user-attachments/assets/436a5ecf-f4f9-4351-b5e9-ed803cb27998" />


### Description
Python-matplotlib based digital image processing toolkit, based on : 

- Spatial filtering
- Edge detection
- Histogram analysis
- Intensity windowing
- Thresholding
- Pixel-level transformations.



## C

### Implementation of the **Filter (More)** and **Recover** problem from Harvard's CS50x.

## Filter

This project applies different image filters to 24-bit BMP images using C.

The program supports four filters:

* **Grayscale (`-g`)** – Converts the image to grayscale.
* **Reflect (`-r`)** – Reflects the image horizontally.
* **Blur (`-b`)** – Applies a box blur to each pixel.
* **Edges (`-e`)** – Detects edges using the Sobel operator.

```bash
./filter -g images/yard.bmp output.bmp
```

Other filters:

```bash
./filter -r images/yard.bmp output.bmp
./filter -b images/yard.bmp output.bmp
./filter -e images/yard.bmp output.bmp
```

- Grayscale

Each pixel's red, green, and blue values are averaged:

```text
average = (red + green + blue) / 3
```

The resulting average is assigned to all three color channels.

- Reflect

Pixels on each row are swapped from left to right, producing a horizontal mirror effect.

- Blur

Each pixel is replaced with the average color of itself and its neighboring pixels.

A copy of the original image is used so that modifying one pixel does not affect the calculations for other pixels.

- Edges

The edge detection filter uses the **Sobel operator** with horizontal (`Gx`) and vertical (`Gy`) kernels to detect changes in pixel intensity.

The resulting value is calculated using:

```text
sqrt(Gx² + Gy²)
```

and capped at `255`.

## Recover

<img width="800" height="599" alt="recovered_image" src="https://github.com/user-attachments/assets/bb057e1f-df25-4deb-a72c-61546f5b9c4e" />


Recover is a C program that recovers JPEG images from a forensic image file containing raw data from a memory card.

The program reads the memory card data in blocks of 512 bytes, identifies JPEG file signatures, and writes each recovered JPEG to a separate file.


Run it with the forensic image:

```bash
./recover card.raw
```

The program generates recovered images with names such as:

```text
000.jpg
001.jpg
002.jpg
...
```

https://cs50.harvard.edu/x/
