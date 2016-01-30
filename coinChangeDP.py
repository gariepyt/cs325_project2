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
    changeIter = changeVal
    while changeIter > 0:
        coin = minCoinsUsed[changeIter]
        minUsed.append(coin)
        changeIter = changeIter - coin

    #print("Table min Count: ", minCoinCount)
    #print("Table min Used: ", minCoinsUsed)
    print("Minimum Coin Count: ", minCount)
    print("Minimum Coins Used: ", minUsed)
    return minCount, minUsed

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

                    # Run the Dynamic Programming Algorithm for Coin Change Problem
                    minCoinCount, minCoinsUsed = changedp(denomArray, changeValue)

                    # With returned results, write to output file, '[input_filename]change.txt
                    resultFile.write("[")
                    for item in minCoinsUsed:
                        if (item > minCoinsUsed[0]):
                            resultFile.write(", ")
                        resultFile.write("%s" % item)
                    resultFile.write("]\n")
                    resultFile.write(str(minCoinCount))
                    resultFile.write("\n")

    # Close any open files
    resultFile.close()
    inFile.close()

    # Exit the program


# Begin program
main()