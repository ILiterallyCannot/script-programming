import sys

def div(x,y):
    try:
        theResult = x/float(y)
        return theResult
    except:
        print("Error: Can not divide by 0")
        sys.exit()

try:
    print div(3,3,3)
except TypeError:
    print("2 parameters needed")
