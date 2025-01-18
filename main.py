import os
import cv2
import random

os.system("screencapture screen.png")

img = cv2.imread("screen.png", 1)

rows, cols, _ = img.shape
print("rows: " + str(rows))
print("cols: " + str(cols))

cropped_image = img[706:1297, 2233:2816]

cv2.imshow('Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
