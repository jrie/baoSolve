#-------------------------------------------------------------------------------
# Auhor: theSplit [ngb] Code competition 3
#-------------------------------------------------------------------------------

def getNextField(currentField, fieldsInRow, direction):
    if currentField > fieldsInRow:
        return currentField - 1
    elif currentField < fieldsInRow-1:
        return currentField + 1;
    else:
        if direction == 0:
            return 0
        else:
            return (fieldsInRow * 2) - 1


def outputRows(rowsData, fieldsInRow):
    print ";".join([str(num) for num in rowsData[:fieldsInRow]])
    print ";".join([str(num) for num in rowsData[fieldsInRow:]])



def printPlayboard(rowsA, rowsB):
    fieldsInRow = len(rowsA) / 2
    outputRows(rowsA, fieldsInRow)
    fieldSep = "--" * fieldsInRow
    print fieldSep
    outputRows(rowsB, fieldsInRow)

#-------------------------------------------------------------------------------

def playGame(rowsA, rowsB, fieldToStart, beVerbose):

    totalFields = len(rowsB)
    fieldsInRow = len(rowsB) / 2

    currentField = fieldToStart
    direction = 0

    if currentField < fieldsInRow:
        direction = 1
    else:
        direction = 0

    movesMade = 0
    stonesStolen = 0

    if (beVerbose):
        print "[GAME START]"

    while(True):

        stonesInHand = 0


        if (rowsB[currentField] >= 2):
            if (beVerbose):
                print "\n[------------------------ MAKETURN %d -----------------------]" %(movesMade+1)
                printPlayboard(rowsA, rowsB)
                print "\n"

            stonesInHand = rowsB[currentField]

            if (beVerbose):
                print "[STARTMOVE @ FIELD %d]" %(currentField+1)
                print "[STONES] %3d [FIELD %d]" %(stonesInHand, currentField+1)

            enemyStones = 0

            if (currentField < fieldsInRow):
                enemyField = (fieldsInRow)+currentField;
                enemyStones = rowsA[enemyField]

                rowsA[enemyField] = 0

                if (enemyStones != 0 and movesMade != 0):
                    stonesStolen += enemyStones
                    stonesInHand += enemyStones

                    if (beVerbose):
                        print "[CAPTURED] %3d STONES - OPPONENT FIELD %d" %(enemyStones, enemyField+1)

            rowsB[currentField] = 0

            if (beVerbose):
                print "-------------------------------------------------------------"

        else:
            if (beVerbose):
                print "[OUT OF MOVES] %d STONES @ FIELD %d" %(rowsB[nextField], nextField+1)

            break

        while (stonesInHand != 0):
            nextField = getNextField(currentField, fieldsInRow, direction)

            if nextField == 0:
                direction = 1
            elif nextField == totalFields - 1:
                direction = 0

            currentField = nextField
            rowsB[nextField] += 1
            stonesInHand -= 1;

            if (beVerbose):
                print "[MOVETO] %3d [STONES IN HAND %d @ FIELD %d]" %(nextField+1, stonesInHand, rowsB[nextField])

        if (beVerbose):
            print "\n"
            printPlayboard(rowsA, rowsB)
            print "\n[------------------------ ENDTURN %d -------------------------]" %(movesMade+1)

        movesMade += 1

    if (beVerbose):
        print "\n[GAME END SUMMARY]"
        print "STONES STOLEN: %d" %(stonesStolen)
        print "TURNS: %d\n" %(movesMade)
        print "-------------------------------------------------------------"
        print ("FINAL PLAYBOARD:")
        printPlayboard(rowsA, rowsB)
        print ""

    return [fieldToStart, stonesStolen, movesMade]


#-------------------------------------------------------------------------------

if __name__ == "__main__":
    rowsA = []  # Player A
    rowsB = []  # Player B (played)

    rowsAOriginal = []
    rowsBOriginal = []

    rowsABestGame = []
    rowsBBestGame = []

    beVerbose = False
    try:
        with open("playboard.csv", "r") as inputFile:

            row = 0
            game = 0

            for lineData in inputFile:

                if (lineData[0] == '\n'):
                    rowsA = []
                    rowsB = []

                    rowsAOriginal = []
                    rowsBOriginal = []

                    rowsABestGame = []
                    rowsBBestGame = []

                    row = 0
                    continue;

                row += 1

                data = [int(num) for num in lineData.rstrip().split(";")]

                if (row <= 2):
                    rowsA.extend(data)
                    rowsAOriginal.extend(data)
                else:
                    rowsB.extend(data)
                    rowsBOriginal.extend(data)

                if (row == 4):
                    game += 1

                    gameResult = [0,0,0] # [field started, stolen, turns made]
                    bestResult = [0,0,0]

                    # The field is zero based
                    for field in xrange(len(rowsB)-1, (len(rowsB) / 2)-1, -1):
                        gameResult = playGame(rowsA, rowsB, field, beVerbose)

                        if (gameResult[1] > bestResult[1]):
                            bestResult = gameResult
                            rowsABestGame = []
                            rowsABestGame.extend(rowsA)

                            rowsBBestGame = []
                            rowsBBestGame.extend(rowsB)

                        rowsA = []
                        rowsA.extend(rowsAOriginal)

                        rowsB = []
                        rowsB.extend(rowsBOriginal)

                    for field in xrange(0, len(rowsB) / 2, 1):

                        gameResult = playGame(rowsA, rowsB, field, beVerbose)

                        if (gameResult[1] > bestResult[1]):
                            bestResult = gameResult
                            rowsABestGame = []
                            rowsABestGame.extend(rowsA)

                            rowsBBestGame = []
                            rowsBBestGame.extend(rowsB)

                        rowsA = []
                        rowsA.extend(rowsAOriginal)

                        rowsB = []
                        rowsB.extend(rowsBOriginal)


                    print "BEST RESULT FOR GAME %4d: FIELD %d, %d STOLEN, %d TURNS\n\n" %(game, bestResult[0]+1, bestResult[1], bestResult[2])

                    print "[------------------------- REPLAY WINNING GAME WITH OUTPUT -------------------------]"
                    playGame(rowsA, rowsB, bestResult[0], True)
                    print "[------------------------------------ END REPLAY -----------------------------------]"

    except IOError as e:
        print "Could not find the file \"playboard.csv\". Please add it to the directory. Error Message: %s" %(e.strerror)
    except Error as e:
        print "Unknown error occured, message: %s" %(e.strerror)
