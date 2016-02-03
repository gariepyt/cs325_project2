# Greedy method for finding umber of arrays in 
# Written by: Tom Gariepy

import sys
import os
import time

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
			resArr, resCount = chGreedy(V, A)
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
			resArr1, resCount1 = chGreedy(V1, A)
			endTime1 = time.clock()
			totTime1 = endTime1 - startTime1

			# Getting A2 answers
			startTime2 = time.clock()
			resArr2, resCount2 = chGreedy(V2, A)
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
			resArr, resCount = chGreedy(V, A)
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
					retArr, retCount = chGreedy(curArray, curTotal)	#calling our function
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