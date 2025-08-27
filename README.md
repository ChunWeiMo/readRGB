# Image RGB Data Extractor

## Overview
`readRBG.py` is a Python script that reads RGB (Red, Green, Blue) data from an image file and calculates the total sum of R, G, and B values across all pixels. The results are saved to a CSV file named `image_RGB_list.csv`. The script also includes a utility function to convert JPG images to PNG format.

## Features
- Extracts total R, G, and B values from an image.
- Saves RGB data to a CSV file (`image_RGB_list.csv`) with columns: `Image Name`, `R_total`, `G_total`, `B_total`.
- Supports PNG images (and JPG conversion to PNG).
- Handles file existence checks and errors gracefully.
- Appends new data to the CSV file without overwriting existing entries.

## Requirements
To run the script, you need the following Python libraries:
- `sys` (standard library)
- `os` (standard library)
- `pathlib` (standard library)
- `Pillow` (PIL) for image processing

Install the `Pillow` library using pip:
```bash
pip install Pillow
```

## Usage

Ensure the img folder exists and contains the input image (test.png by default).

Run the script using Python 3:

```bash
python3 readRBG.py
```