def compareNumbers(a,b):
    if a > b:
        print ("%s is greater" % (a))
    elif a == b:
        print("The numbers are equal")
    else:
        print ("%s is greater" % (b))
a = input("First number: ")
b = input("Second number: ")
compareNumbers(a,b)
