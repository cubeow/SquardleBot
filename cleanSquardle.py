import cv2
from PIL import Image

def cleanSquardle():
    img = cv2.imread("/Users/sagewong/git/SquardleBot/screen.png", 1)
    cropped_image = img[706:1297, 2233:2816]

    rows, cols, _ = cropped_image.shape

    for i in range(rows):
        for j in range(cols):
            if (cropped_image[i, j] != [26, 26, 26]).any():
                cropped_image[i, j] = [255, 255, 255]
    cv2.imwrite("cropped_image.png", cropped_image)
    return Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
