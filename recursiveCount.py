numberList = [1,2,3,4,5]

def recursiveSum(numList):
	if not numList:
		return 0
	else:
		return 1 + recursiveSum(numList[1::2]) + recursiveSum(numList[2::2])

print recursiveSum( numberList )