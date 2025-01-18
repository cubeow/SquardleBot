import mss
import cv2
import random
from PIL import Image
import os
from cleanSquardle import cleanSquardle

import pytesseract

os.system("screencapture screen.png")

img = cv2.imread("/Users/sagewong/git/SquardleBot/screen.png", 1)

cropped_pil = cleanSquardle()

print(pytesseract.image_to_string(cropped_pil))

