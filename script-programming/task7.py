def sumAndDivide(a,b):
    sum = a + b
    print ("The sum is %s" %(sum))
    print ("Is %s divisable by 2?" %(sum))
    if sum % 2 == 0:
        print "yes it is"
    else:
        print "nope"
a = int(raw_input("First number: "))
b = int(raw_input("Second number: "))

sumAndDivide(a,b)
