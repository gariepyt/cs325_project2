# Dynamic Programming implementation for the Coin Change Problem
# Author: Jeffrey Schachtsick
# Last Update: 01/29/2016
# Description: Read from a file the set of coins available and the amount
#       to make change for.  Once read, push those to a function to run
#       execution of the Coin Change Problem using Dynamic Programming.
#       Finally, the result of the Coin Change problem should output the
#       minimum set of coins from each denomination and the minimum number
#       of coins.

import sys
import os
import time

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
    print("Minimum Coin Count: ", minCount)
    print("Minimum Coins Used: ", minUsed)
    return minCount, minUsed

def prob6():
	V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
	# A = 200000000
	A = 2000
	outName = "greedyResults_prob6.csv"
	with open(outName, 'wt') as resultFile:
		resultFile.write("A,Greedy (Time),Greedy (coin)\n")

		# while (A <= 2000000000):
		while (A <= 2200):
			startTime = time.clock()
			resArr, resCount = changedp(V, A)
			endTime = time.clock()
			totTime = endTime - startTime
			print("A: " + str(A))
			print("Time: " + str(totTime))
			print("Answer: " + str(resCount))

			resultFile.write(str(A) + "," + str(totTime) + "," + str(resCount) + "\n")

			A = A + 1
			# A = A + 200000000

def prob5():
	V1 = [1, 2, 6, 12, 24, 48, 60]
	V2 = [1, 6, 13, 37, 150]
	# A = 200000000
	A = 20
	outName = "greedyResults_prob5.csv"
	with open(outName, 'wt') as resultFile:
		resultFile.write("A,Greedy (A1 Time),Greedy (A1 coin),Greedy (A2 Time),Greedy (A2 coin)\n")
		# while (A <= 2000000000):
		while (A <= 34):
			# Getting A1 answers
			startTime1 = time.clock()
			resArr1, resCount1 = changedp(V1, A)
			endTime1 = time.clock()
			totTime1 = endTime1 - startTime1

			# Getting A2 answers
			startTime2 = time.clock()
			resArr2, resCount2 = changedp(V2, A)
			endTime2 = time.clock()
			totTime2 = endTime2 - startTime2

			print("A: " + str(A))
			print("Time1: " + str(totTime1))
			print("Answer1: " + str(resCount1))
			print("Time2: " + str(totTime2))
			print("Answer2: " + str(resCount2))

			resultFile.write(str(A) + "," + str(totTime1) + "," + str(resCount1) + "," + str(totTime2) + "," + str(resCount2) + "\n")

			A = A + 1
			# A = A + 200000000

def prob4():
	V = [1, 5, 10, 25, 50]
	# A = 200000000
	A = 20
	outName = "greedyResults_prob4.csv"
	with open(outName, 'wt') as resultFile:
		resultFile.write("A,Greedy (Time),Greedy (coin)\n")

		# while (A <= 2000000000):
		while (A <= 55):
			startTime = time.clock()
			resArr, resCount = changedp(V, A)
			endTime = time.clock()
			totTime = endTime - startTime
			print("A: " + str(A))
			print("Time: " + str(totTime))
			print("Answer: " + str(resCount))

			resultFile.write(str(A) + "," + str(totTime) + "," + str(resCount) + "\n")

			# A = A + 200000000
			A = A + 5

def main():

	if (len(sys.argv) == 2):				#file i/o stuff checking for file
		fName = sys.argv[1]
		inName = fName + ".txt"
		outName = fName + "change.txt"

		fileCheck = os.path.isfile(inName)
		if (fileCheck == False):
			print("ERROR: " + inName + " not found.")
			return 1

		with open(outName, 'wt') as resultFile:

			with open(inName, 'rt') as inputFile:

				inData = inputFile.read().splitlines()

				inArr = 0
				inTot = 1

				while (inArr < len(inData)):			#Reading the file
					curArray = inData[inArr]

					curArray = curArray.replace('[', '')	#getting rid of extra stuff
					curArray = curArray.replace(']', '')

					curArray = map(int, curArray.split(','))	#reading in the array , deleminated

					curTotal = int(inData[inTot])			#amount desired

					t0 = time.time()
					retArr, retCount = changedp(curArray, curTotal)	#calling our function
					t1 = time.time()
					totalTime = t1-t0

					print("Time elapsed: ", totalTime)
					print("Coin count: " + str(retArr))
					print("Minimal coins: " + str(retCount))

					resultFile.write(str(retArr) + "\n")
					resultFile.write(str(retCount) + "\n")

					inArr = inArr + 2
					inTot = inTot + 2

	else:
		print("ERROR: incorrect amount of arguments")

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