import cv2
from PIL import Image
import cv2
import importlib
import numpy as np
import pytesseract
from fillEmptySpaces import fillEmptySquares



def cleanSquardleImage(type):
    img = cv2.imread("/Users/sagewong/git/SquardleBot/temp/screen.png", 1)

    startX = 706
    startY = 1297
    cropped_image = img[startX:startY, 2233:2816]
    og_img = cropped_image.copy()

    # Gets the dimensions
    rows, cols, _ = cropped_image.shape
    
    # Loops through every pixel to make the box color black
    for i in range(rows):
        for j in range(cols):
            if (cropped_image[i, j] == [224, 224, 224]).any():
                cropped_image[i, j] = [0, 0, 0]
    
    # creates a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Makes the letters thicker
    eroded_image = cv2.erode(cropped_image, kernel)
    # swaps light pixels and dark pixels
    inverse_image = cv2.bitwise_not(eroded_image)
    # All pixels below value of 50 are made black and all above are made white
    thresh, threshed_img = cv2.threshold(inverse_image, 50, 255, cv2.THRESH_BINARY)

    # reduces channel to 2 dimensions so that it can be used in the findContours function
    converted_img = cv2.cvtColor(threshed_img, cv2.COLOR_BGR2GRAY)
    # finds the boxes
    cnts = cv2.findContours(converted_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cleans the boxes data
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # attempted initial sorting
    cnts = sorted(cnts, key=lambda x: (cv2.boundingRect(x)[0]))
    # pixels of padding applied to make the letter seem smaller
    antiPadding = 20
    # an empty list of the words
    wordList = []

    # creates a wordList containing the stringified image and it's x and y coordinates
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        roi = cv2.copyMakeBorder(og_img[y+antiPadding:y+h-antiPadding, x+antiPadding:x+w-antiPadding], 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=[224, 224, 224])
        wordList.append([pytesseract.image_to_string(roi, config="--psm 10"), x, y])
    wordList = fillEmptySquares(wordList)

    clusters = []
    # clusters the wordList elements by x positioning
    for i in wordList:
        anyMatching = False
        for index, j in enumerate(clusters):
            if abs(j[0][0] - i[1]) < 10:
                clusters[index] = [[j[0][0]], j[1] + [i]]
                anyMatching = True
        if anyMatching == False:    
            clusters.append([[i[1]], [i]])
        if len(clusters) == 0:
            clusters.append([[i[1]], [i]])

    newClusters = clusters.copy()
    # sorts the y values
    for index, i in enumerate(newClusters):
        newClusters[index][1] = sorted(newClusters[index][1], key=lambda x: x[2])
    newClusters = sorted(newClusters, key=lambda x: x[0])

    newNewClusters = []
    # removes the now unnecessary cluster header
    for i in newClusters:
        newNewClusters.append(i[1])
    
    # transforms the list into a 2d matrix representative of a squaredle board
    length = len(newNewClusters[0])
    newestList = [[] for i in range(len(newNewClusters[0]))]
    letteredList = [[] for i in range(len(newNewClusters[0]))]
    print(newestList)
    for j in range(length):
        for i in newNewClusters:
            newestList[j] = newestList[j] + [[i[j][0].replace("\n", "").replace("|", "I").replace("0", "O").replace("@", "O"), i[j][1] + startX, i[j][2] + startY]]
            letteredList[j] = letteredList[j] + [[i[j][0].replace("\n", "").replace("|", "I").replace("0", "O").replace("@", "O")]]
    return newestList, letteredList
