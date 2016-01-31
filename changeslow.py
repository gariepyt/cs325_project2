# Greedy method for finding umber of arrays in 
# Written by: Tom Gariepy

import sys
import os

def chSlow(array, total):
	minCoins = total
	minArr = [0] * len(array)

	for i in range(0, len(array)):
		if (array[i] <= total):
			resArr, resCoins = chSlow(array, total - array[i])
			resCoins = resCoins + 1
			resArr[i] = resArr[i] + 1

			if resCoins < minCoins:
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

				while (inArr < len(inData)):
					curArray = inData[inArr]

					curArray = curArray.replace('[', '')
					curArray = curArray.replace(']', '')

					curArray = map(int, curArray.split(','))

					curTotal = int(inData[inTot])

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
