import mss
import cv2
import random
from PIL import Image
import os
import importlib
import cleanSquardle
importlib.reload(cleanSquardle)
from cleanSquardle import cleanSquardleImage
import numpy as np
import pytesseract

os.system("screencapture screen.png")

img = cv2.imread("/Users/sagewong/git/SquardleBot/screen.png", 1)

# arrayedSquardleRepresentation. First index of each element contains the letter. second contains the x position, third contains the y position
arrayedSquardleRepresentation, letteredSquardleRepresentation = cleanSquardleImage("none")
for i in letteredSquardleRepresentation:
    print(i)