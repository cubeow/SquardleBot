from scipy.spatial.distance import pdist, squareform
import numpy as np

def fillEmptySquares(sampleList):
    # sampleList = [['K\n', 8, 127], ['E\n', 126, 246], ['A\n', 126, 9], ['C\n', 245, 9]]


    allCoords = []
    for row in sampleList:
        allCoords.append([row[1], row[2]])

    dist_matrix = squareform(pdist(allCoords))
    np.fill_diagonal(dist_matrix, np.inf)
    min_idx = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)

    closest_points = [allCoords[min_idx[0]], allCoords[min_idx[1]]]
    distance = np.linalg.norm(np.array(closest_points[0]) - np.array(closest_points[1]))

    largestX = -1000000
    largestY = -1000000
    smallestX = 100000
    smallestY = 100000



    for i in allCoords:
        if i[0] > largestX:
            largestX = i[0]
        if i[1] > largestY:
            largestY = i[1]
        if i[0] < smallestX:
            smallestX = i[0]
        if i[1] < smallestY:
            smallestY = i[1]

    stuffToAdd = []

    for x in range(round((largestX - smallestX)/distance)+1):
        for y in range(round((largestY - smallestY)/distance)+1):
            passed = False
            for row in sampleList:
                if np.linalg.norm(np.array([row[1], row[2]]) - np.array([x*distance + smallestX, y*distance + smallestY])) <= 20:
                    passed = True
            if passed == False:
                stuffToAdd.append(["-", float(x*distance + smallestX), float(y*distance + smallestY)])

    return stuffToAdd + sampleList

# print(fillEmptySquares("a"))