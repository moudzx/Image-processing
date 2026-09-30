# Trixie

A small retro-styled image editor that runs entirely in your browser. One HTML file, no build step, no dependencies, and your images never leave your device.
## [Website](https://moudzx.github.io/Trixie)

<img width="3072" height="4608" alt="Screenshot 2026-09-30 at 10-19-19 Trixie - retro image lab" src="https://github.com/user-attachments/assets/69521716-91a9-430f-a7d4-5063e817a646" />


## Run it

Open `index.html` in any modern browser, or host it as a static page anywhere.

The title uses the Press Start 2P font from Google Fonts. Offline, it falls back to a generic monospace font and everything else works as normal.

## Getting an image in

- **Load image** button
- **Sample**, a generated test picture
- Drag and drop a file anywhere on the page
- Paste from the clipboard (Ctrl/Cmd+V)

Large images are scaled down so the longest side is at most 960 px. Edits and exports use that working size.

## Features

### Adjust (live sliders)
Exposure, Contrast, Saturation, Hue, Warmth, Gamma, Vignette, Grain. These combine with any filter and can be reset in one click.

### Presets
Vintage, Noir, Cool, Warm, Fade, Vivid, Arcade, Dusk. Each sets the sliders and a filter, and you can keep tweaking afterwards.

### Filters
None, Grayscale, Sepia, Invert, Brightness, Contrast, Threshold, Box blur, Gaussian blur, Sharpen, Emboss, Edge (Sobel), Equalize, Pixelate, Mirror, Posterize, Palette, Scanlines, RGB glitch, Solarize, Duotone, Unsharp mask, Denoise.

The Palette filter maps the image to a retro palette (Game Boy, CGA, Amber CRT, PICO-8, Vapor) with optional Bayer dithering. Convolution filters show their kernel.

### Edit tools
- **Stack result** bakes the current filter and adjustments in so you can keep building on it
- Undo, Redo, Reset to the original
- **Crop**: drag a rectangle on the input image, then press *Crop selection*
- Rotate, Flip H, Flip V
- Resize: 25%, 50%, 75%, 150%, 200%
- **Auto levels**
- **Hold: original**: press and hold to compare with the input

### Text and border
Add a caption (size, color, top/middle/bottom) and a border (width, color).

### Colors
- Pixel inspector: hover either image to read RGB and hex values
- **Extract palette**: up to 8 dominant colors, click a swatch to copy its hex code
- Luminance histogram (line: input, bars: output)

### Save
| Format | Notes |
|--------|-------|
| PNG | Lossless, keeps transparency |
| JPG | Quality slider, transparency flattened to white |
| WebP | Quality slider |
| BMP | 24-bit, transparency flattened to white |

Export scale is 1x, 2x, 4x or 8x using nearest-neighbour, so pixel art stays crisp. **Copy PNG** puts the image on the clipboard (the browser may ask for permission).

## Keyboard shortcuts

| Keys | Action |
|------|--------|
| Ctrl/Cmd+Z | Undo |
| Ctrl/Cmd+Y or Ctrl/Cmd+Shift+Z | Redo |
| Ctrl/Cmd+V | Paste an image |

## Notes

- Filters work directly on raw pixel data in JavaScript (canvas `ImageData`), with no libraries.
- Denoise is the slowest filter on large images, especially at radius 2.
- Some browsers cannot encode WebP. If so, Trixie tells you and you can pick another format.
- The look follows your system light/dark setting. Dark is a muted purple, light is a Game Boy-style green.

# Image-processing workshops associated

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
