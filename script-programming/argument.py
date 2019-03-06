import sys
print "script name", sys.argv[0]
print "number of arguments", len(sys.argv)
print "Arguments are", sys.argv

def plus(x,y):
    return x+y
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print plus(num1,num2)
