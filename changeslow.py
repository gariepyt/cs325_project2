# Greedy method for finding umber of arrays in 
# Written by: Tom Gariepy

import sys
import os

def chSlow(array, total):
	minCoins = total
	minArr = [0] * len(array)

	for i in range(0, len(array)):
		if (array[i] <= total):						#if the coin can be successfully be subrtracted from total amount
			resArr, resCoins = chSlow(array, total - array[i])	#subtracting that coin
			resCoins = resCoins + 1					#adding to the count of total coins
			resArr[i] = resArr[i] + 1				#adding to the count of said coin				

			if resCoins < minCoins:					#if our combination is optimized update our table
				minCoins = resCoins
				minArr = resArr

	return minArr, minCoins


def main():

	if (len(sys.argv) == 2):
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

				while (inArr < len(inData)):				#reading our input file
					curArray = inData[inArr]

					curArray = curArray.replace('[', '')		#Reading through the extras
					curArray = curArray.replace(']', '')

					curArray = map(int, curArray.split(','))	#the array containing our coin values

					curTotal = int(inData[inTot])			#amount desired to be optimized

					retArr, retCount = chSlow(curArray, curTotal)

					print("Coin count: " + str(retArr))
					print("Minimal coins: " + str(retCount))

					resultFile.write(str(retArr) + "\n")
					resultFile.write(str(retCount) + "\n")

					inArr = inArr + 2
					inTot = inTot + 2

	else:
		print("ERROR: incorrect amount of arguments")


main()
