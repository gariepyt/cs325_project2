# Dynamic Programming implementation for the Coin Change Problem
# Author: Jeffrey Schachtsick
# Last Update: 01/29/2016
# Description: Read from a file the set of coins available and the amount
#       to make change for.  Once read, push those to a function to run
#       execution of the Coin Change Problem using Dynamic Programming.
#       Finally, the result of the Coin Change problem should output the
#       minimum set of coins from each denomination and the minimum number
#       of coins.

# Imports
import os
import sys
import csv
import time

# User provides the location of the input file
def userSpecify():
    """
    :return: Path to input file
    """
    valid = False
    while valid != True:
        userPath = raw_input("\nIf the input file is local to program directory, enter the input file."
                             "\nOtherwise, please enter the path to the input file here: ").strip()
        if os.path.exists(userPath):
            print("Path has been validated")
            valid = True
        else:
            print("Invalid File Path, File Doesn't Exist!  Please try again.")
            continue
        return userPath

# Get input file name, by stripping items from the path
def stripPath(filePath):
    """
    :param filePath: Path of the input file.
    :return: string with input file name (without the .txt suffix)
    """
    # Parse each path location to a list
    path_list = filePath.split(os.sep)
   #print("Path List: ", path_list)
    # take the last item from the list
    inputText = path_list[-1]
    #print("This is the input text: ", inputText)
    # Remove the suffix
    if inputText.endswith('.txt'):
        inputName = inputText[:-4]
    #print("Input name is: ", inputName)
    return inputName


# Coin Change Problem in Dynamic Programming algorithm
# Source of algorithm from http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
def changedp(denomArray, changeVal):
    """
    :param denomArray: Array of integers representing denominations of coins
    :param changeVal: Integer representing the amount to make change with
    :return: array of minimum denominations, and integer of number of coins used.
    """
    # Initialize teh table with minimum coins used and the coin count
    minCoinsUsed = [0]*(changeVal + 1)
    minCoinCount = [0]*(changeVal + 1)

    # Loop through each type coin to process the table.
    for coins in range(changeVal + 1):
        coinCount = coins
        latestCoin = 1
        for i in [coinDenom for coinDenom in denomArray if coinDenom <= coins]:
            if (minCoinCount[coins - i] + 1 < coinCount):
                coinCount = minCoinCount[coins - i] + 1
                latestCoin = i
        minCoinCount[coins] = coinCount
        minCoinsUsed[coins] = latestCoin

    # Parse the table
    minCount = minCoinCount[changeVal]
    minUsed = []
    for each in denomArray:
        minUsed.append(0)
    changeIter = changeVal
    while changeIter > 0:
        coin = minCoinsUsed[changeIter]
        k = 0
        for j in denomArray:
            if (coin == j):
                minUsed[k] += 1
            k += 1

        #minUsed.append(coin)
        changeIter = changeIter - coin

    #print("Table min Count: ", minCoinCount)
    #print("Table min Used: ", minCoinsUsed)
    # print("Minimum Coin Count: ", minCount)
    # print("Minimum Coins Used: ", minUsed)
    return minCount, minUsed

def prob6():
    V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    # A = 200000
    A = 20
    outName = "dpResults_prob6.csv"
    with open(outName, 'wt') as resultFile:
        resultFile.write("A,DP (Time),DP (coin)\n")
    
        # while (A <= 2000000):
        while (A <= 30):
            startTime = time.clock()
            resCount, resArr = changedp(V, A)
            endTime = time.clock()
            totTime = endTime - startTime
            print("A: " + str(A))
            print("Time: " + str(totTime))
            print("Answer: " + str(resCount))

            resultFile.write(str(A) + "," + str(totTime) + "," + str(resCount) + "\n")

            # A = A + 200000
            A = A + 1

def prob5():
    V1 = [1, 2, 6, 12, 24, 48, 60]
    V2 = [1, 6, 13, 37, 150]
    # A = 200000
    A = 20
    outName = "dpResults_prob5.csv"
    with open(outName, 'wt') as resultFile:
        resultFile.write("A,DP (A1 Time),DP (A1 coin),DP (A2 Time),DP (A2 coin)\n")
        # while (A <= 2000000):
        while (A <= 34):    
            # Getting A1 answers
            startTime1 = time.clock()
            resCount1, resArr1 = changedp(V1, A)
            endTime1 = time.clock()
            totTime1 = endTime1 - startTime1

            # Getting A2 answers
            startTime2 = time.clock()
            resCount2, resArr2 = changedp(V2, A)
            endTime2 = time.clock()
            totTime2 = endTime2 - startTime2

            print("A: " + str(A))
            print("Time1: " + str(totTime1))
            print("Answer1: " + str(resCount1))
            print("Time2: " + str(totTime2))
            print("Answer2: " + str(resCount2))

            resultFile.write(str(A) + "," + str(totTime1) + "," + str(resCount1) + "," + str(totTime2) + "," + str(resCount2) + "\n")
            
            # A = A + 200000
            A = A + 1

def prob4():
    V = [1, 5, 10, 25, 50]
    # A = 200000
    A = 20
    outName = "dpResults_prob4.csv"
    with open(outName, 'wt') as resultFile:
        resultFile.write("A,DP (Time),DP (coin)\n")
    
        # while (A <= 2000000):
        while (A <= 55):
            startTime = time.clock()
            resCount, resArr = changedp(V, A)
            endTime = time.clock()
            totTime = endTime - startTime
            print("A: " + str(A))
            print("Time: " + str(totTime))
            print("Answer: " + str(resCount))

            resultFile.write(str(A) + "," + str(totTime) + "," + str(resCount) + "\n")

            # A = A + 100000
            A = A + 5

# Main function for management of functions.
def main():
    """
    :input: None
    :return: None
    """

    # Set variables

    # Get and validate path of the input file
    path = userSpecify()

    # Strip the path to get only the input file name
    inputName = stripPath(path)

    # Create and open the file output file
    outFile = inputName + "change.txt"
    with open(outFile, 'wt') as resultFile:

        # Open the input file and read each line
        with open(path, 'rt') as inFile:
            fStream = csv.reader(inFile)
            for row in fStream:
                if (len(row) > 1):
                    row[0] = row[0].replace('[', '')
                    row[len(row) - 1] = row[len(row) - 1].replace(']', '')
                    line1 = list(map(int, row))
                    #print("Row: ", row)
                if (len(row) == 1):
                    line2 = list(map(int, row))
                    line2 = line2[0]
                    #print("Line 2: ", line2)

                    # When in line2 Read in contents to memory and run
                    denomArray = line1
                    changeValue = line2

					# time1 = time.clock()
                    # Run the Dynamic Programming Algorithm for Coin Change Problem
                    minCoinCount, minCoinsUsed = changedp(denomArray, changeValue)
					# time2 = time.clock()
					# totalTime = time2-time1

					# print("Time elapsed: " + totalTime)

                    # With returned results, write to output file, '[input_filename]change.txt
                    resultFile.write(str(minCoinsUsed) + "\n")
                    resultFile.write(str(minCoinCount) + "\n")

    # Close any open files
    resultFile.close()
    inFile.close()

    # Exit the program

if (len(sys.argv) == 2):
    if (sys.argv[1] == "prob4"):
        prob4()
    elif (sys.argv[1] == "prob5"):
        prob5()
    elif (sys.argv[1] == "prob6"):
        prob6()
    else:
        main()
else:
    print("ERROR: incorrect amount of arguments")