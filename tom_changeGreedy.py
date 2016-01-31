# Greedy method for finding umber of arrays in 
# Written by: Tom Gariepy

import sys
import os

def chGreedy(array, total):
	i = len(array) - 1
	curTotal = total
	countArr =  [0] * len(array)				#empty array for coin count
	totCount = 0

	while (curTotal > 0):					#while our total is positive
		if (array[i] <= curTotal):			#if the largest coin value can be subtracted from our total
			curTotal = curTotal - array[i]		#subtracting the coin
			countArr[i] = countArr[i] + 1		#updating our count array of coins
			totCount = totCount + 1			#updating our total count of coins
		else:
			i = i - 1				#moving to the next coin in the coin array

	return countArr, totCount

def prob4():
	V = [1, 5, 10, 25, 50]
	A = 2010
	while (A <= 2200):
		startTime = time.clock()
		resArr, resCount = chGreedy(V, A)
		endTime = time.clock()
		totTime = endTime - startTime
		print("A: " + str(A))
		print("Time: " + str(totTime))
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

					retArr, retCount = chGreedy(curArray, curTotal)	#calling our function

					print("Coin count: " + str(retArr))
					print("Minimal coins: " + str(retCount))

					resultFile.write(str(retArr) + "\n")
					resultFile.write(str(retCount) + "\n")

					inArr = inArr + 2
					inTot = inTot + 2

	else:
		print("ERROR: incorrect amount of arguments")


# main()

prob4()