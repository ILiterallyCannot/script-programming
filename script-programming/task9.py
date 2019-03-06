list1 = [1,2,3,5,4] #the function should return 5
list2 = [1,4,9,2]   #the function should return 9
def listmax(numList):
    theMax = 0
    for i in numList:
        if i > theMax:
            theMax = i
    return theMax

print(listmax(list1))
print(listmax(list2))
