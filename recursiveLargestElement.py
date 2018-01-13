numberList = [1,2,6,4,5]

def recursiveFindMax(numList):
	if not list:
		return 0
	if len(numList) == 1:
		return numList[0]
	else:
		return max(numList[0], recursiveFindMax(numList[1:]))

print recursiveFindMax( numberList )