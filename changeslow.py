# Greedy method for finding umber of arrays in 
# Written by: Tom Gariepy

import sys
import os
import time

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

def prob6():
	V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
	A = 20
	outName = "slowResults_prob6.csv"
	with open(outName, 'wt') as resultFile:
		resultFile.write("A,Slow (Time),Slow (coin)\n")
	
		while (A <= 30):
			startTime = time.clock()
			resArr, resCount = chSlow(V, A)
			endTime = time.clock()
			totTime = endTime - startTime
			print("A: " + str(A))
			print("Time: " + str(totTime))
			print("Answer: " + str(resCount))

			resultFile.write(str(A) + "," + str(totTime) + "," + str(resCount) + "\n")

			A = A + 1

def prob5():
	V1 = [1, 2, 6, 12, 24, 48, 60]
	V2 = [1, 6, 13, 37, 150]
	A = 20
	outName = "slowResults_prob5.csv"
	with open(outName, 'wt') as resultFile:
		resultFile.write("A,Slow (A1 Time),Slow (A1 coin),Slow (A2 Time),Slow (A2 coin)\n")
		while (A <= 34):
			# Getting A1 answers
			startTime1 = time.clock()
			resArr1, resCount1 = chSlow(V1, A)
			endTime1 = time.clock()
			totTime1 = endTime1 - startTime1

			# Getting A2 answers
			startTime2 = time.clock()
			resArr2, resCount2 = chSlow(V2, A)
			endTime2 = time.clock()
			totTime2 = endTime2 - startTime2

			print("A: " + str(A))
			print("Time1: " + str(totTime1))
			print("Answer1: " + str(resCount1))
			print("Time2: " + str(totTime2))
			print("Answer2: " + str(resCount2))

			resultFile.write(str(A) + "," + str(totTime1) + "," + str(resCount1) + "," + str(totTime2) + "," + str(resCount2) + "\n")
			
			A = A + 1

def prob4():
	V = [1, 5, 10, 25, 50]
	A = 20
	outName = "slowResults_prob4.csv"
	with open(outName, 'wt') as resultFile:
		resultFile.write("A,Slow (Time),Slow (coin)\n")
	
		while (A <= 55):
			startTime = time.clock()
			resArr, resCount = chSlow(V, A)
			endTime = time.clock()
			totTime = endTime - startTime
			print("A: " + str(A))
			print("Time: " + str(totTime))
			print("Answer: " + str(resCount))

			resultFile.write(str(A) + "," + str(totTime) + "," + str(resCount) + "\n")

			A = A + 5

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


					t0 = time.time()
					retArr, retCount = chSlow(curArray, curTotal)
					t1 = time.time()
					totalTime = t1-t0

					print("Time elapsed: " + totalTime)
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
