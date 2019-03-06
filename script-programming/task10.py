list1=[1,2,3,4,5,6]
list2=[]

def reverse():
    while list1:
        list2.append(list1.pop())
    print list2

reverse()
