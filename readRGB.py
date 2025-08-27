'''
Program : readRBG.py
Date    : 2023.01.19
Purpose : Read and output RGB data of an image
'''

import sys
import os
from PIL import Image

# Transfer jpg to png
def jpg2png(originImg, newImg):
    try:
        im = Image.open(originImg)
        im.save(newImg, 'png')
    except FileNotFoundError as fne:
        print(fne)

# Read RGB
def readRGB(originImg):
    try:
        im = Image.open(originImg)
        list1=list(im.getdata())            #read RGB data of the whole image
        f=open("image_RGB_list.txt",'a')
        R_total=0
        G_total=0
        B_total=0
        for i in list1:                     #sum RGB respectively
            i=tuple(i)
            R_total=R_total+i[0]
            G_total=G_total+i[1]
            B_total=B_total+i[2]
        f.write(str(R_total)+"\t"+str(G_total)+"\t"+str(B_total)+"\n")
        f.close()
        im.close()
    except FileNotFoundError as fne:
        print(fne)
        

def main():
    if __name__== "__main__":
        # print(sys.argv[1][:-3]+'png')
        # jpg2png(sys.argv[1], sys.argv[1][:-3]+'png')
        readRGB(sys.argv[1])             #cmd >>   python readingRGB.py xxx.jpg
        pass

# main program
main()