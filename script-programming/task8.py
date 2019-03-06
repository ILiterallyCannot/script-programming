list1 = [1,2,3,4,5] #the function should return 15
list2 = [1,4,2,9]   #the function should return 16
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum(list1))
print(listsum(list2))
