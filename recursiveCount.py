numberList = [1,2,3,4,5]

def recursiveCount(numList):
	if not numList:
		return 0
	else:
		return 1 + recursiveCount(numList[1::2]) + recursiveCount(numList[2::2])

print recursiveCount( numberList )