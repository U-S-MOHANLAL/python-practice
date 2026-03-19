def printTriangle(line):
    currentLine = 1
    while line > 0:
        star = ''
        iterateLine = currentLine
        while iterateLine != 0:
            star = star + '*'
            iterateLine = iterateLine - 1
        print(star)
        line = line - 1
        currentLine = currentLine + 1

printTriangle(6)