numberList = [1,2,3,4,5]

def recursiveSum(numList):
	if not numList:
		return 0
	else:
		return numList[0] + recursiveSum(numList[1:])

print recursiveSum( numberList )