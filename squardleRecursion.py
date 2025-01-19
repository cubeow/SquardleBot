import pyautogui
import ast
squardleBoard = [[['-'], ['A'], ['C'], ['K'], ['-']],
[['K'], ['J'], ['A'], ['L'], ['Y']],
[['N'], ['E'], ['R'], ['E'], ['C']],
[['B'], ['U'], ['L'], ['V'], ['D']],
[['-'], ['M'], ['Q'], ['S'], ['-']]]

with open("scrabbleWordList.txt") as file:
    allWords = ast.literal_eval(file.read())

def checkAdjacentLetter(pos, letter, pathTaken):
    # loops through the whole thing to find the adjacent letters
    allRoutes = []
    for rowIndex, row in enumerate(squardleBoard):
        for columnIndex, cell in enumerate(row):
            if abs(rowIndex-pos[0]) <= 1 and abs(columnIndex-pos[1]) <= 1 and [rowIndex, columnIndex] not in pathTaken:
                if cell[0] == letter.upper():
                    allRoutes.append(pathTaken + [[rowIndex, columnIndex]])
    return allRoutes

def findWordRecursion(word):
    # Gets coordinates of all squares with first letter of word
    allStartingPoints = []
    for rowIndex, row in enumerate(squardleBoard):
        for columnIndex, cell in enumerate(row):
            if cell[0] == word[0].upper():
                allStartingPoints.append([rowIndex, columnIndex])
    

    currentWorkingPath = []
    currentLocation = []
    for startingPoint in allStartingPoints:
        # iterates through each starting point
        currentWorkingPath = [startingPoint]
        currentLocation = startingPoint
        backups = []
        while True:
            # checks if any backups are needed to be checked
            if len(backups) > 0:
                for letter in word[len(backups[0]):]:
                    result = checkAdjacentLetter(currentLocation, letter, currentWorkingPath)
                    if len(result) > 0:
                        currentLocation = result[0][-1]
                        currentWorkingPath.append(currentLocation)
                        backups += result[1:]
                    else:
                        backups = backups[1:]
                        break
            # normal loop. Goes through the rest of the letters in the word
            for letter in word[len(currentWorkingPath):]:
                result = checkAdjacentLetter(currentLocation, letter, currentWorkingPath)
                if len(result) > 0:
                    currentLocation = result[0][-1]
                    currentWorkingPath.append(currentLocation)
                    if len(result) > 1:
                        backups += result[1:]
                else:
                    break
            if len(backups) > 0:
                if len(backups[0]) == len(word):
                    return [word, currentWorkingPath]
            # if there's no backups, then you are finished with the while loop
            if len(backups) == 0:
                break
            # if there are backups, set the variables accordingly and delete the one you are going to use
            else:
                currentLocation = backups[0][-1]
                currentWorkingPath = backups[0]
                if len(backups) > 1:
                    backups = backups[1:]
        # if you have found coordinates to an entire word, then return it
        if len(currentWorkingPath) == len(word):
            return [word, currentWorkingPath]
allList = []
for i in allWords:
    print(i)
    if i.isalpha():
        result = findWordRecursion(i)
        if result is not None:
            if len(result) > 0 and len(result[0]) >= 4:
                allList.append(result[0])
print(allList)
for i in allList:
    pyautogui.write(i, interval=0.01)
    pyautogui.press("enter")
