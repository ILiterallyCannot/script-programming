import sys
x = float(raw_input("Give a number: "))
y = float(raw_input("Give another number: "))

def div():
    try:
        theResult = 0
        theResult = x/y
        return theResult
    except:
        print("Error: Can not divide by 0")
        sys.exit()
print div()
