'''
Program : readRBG.py
Date    : 2023.01.19
Purpose : Read and output RGB data of an image
'''

import sys
import os
import pathlib
from PIL import Image
import json

# Transfer jpg to png


def jpg2png(originImg, newImg):
    try:
        im = Image.open(originImg)
        im.save(newImg, 'png')
    except FileNotFoundError as fne:
        print(fne)

# Read RGB


def readRGB(originImg):
    im = Image.open(originImg)
    rgb_whole_img = list(im.getdata())

    R_total = 0
    G_total = 0
    B_total = 0
    for rgb in rgb_whole_img:
        rgb = tuple(rgb)
        R_total = R_total+rgb[0]
        G_total = G_total+rgb[1]
        B_total = B_total+rgb[2]

    csv_file = "image_RGB_list.csv"
    csv_file_exist = pathlib.Path(csv_file).exists()
    with open(csv_file, 'a') as f_csv:
        if not csv_file_exist:
            f_csv.write("Image Name,R_total,G_total,B_total\n")
        f_csv.write(f"{os.path.basename(originImg)},{R_total},{G_total},{B_total}\n")

    im.close()


def main():
    img_file_name = "test.png"
    img_file_path = pathlib.Path(__file__).parent.joinpath("img").joinpath(img_file_name)

    if pathlib.Path(img_file_path).exists() is False:
        print("The images folder does not exist!")
        sys.exit()

    readRGB(img_file_path)


if __name__ == "__main__":
    main()
