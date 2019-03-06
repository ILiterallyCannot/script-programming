import sys
try:
    x = float(raw_input("Give a number: "))
    y = float(raw_input("Give another number: "))
except ValueError:
    print("One or both of your parameters are wrong type!")
    sys.exit()

def div():
    try:
        theResult = 0
        theResult = x/y
        return theResult
    except:
        print("Error: Can not divide by 0")
        sys.exit()
print div()
