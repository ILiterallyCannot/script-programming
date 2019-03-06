import sys

def switch_case(arguement):
    switcher = {
        0: "add",
        1: "subtract",
        2: "multiply",
        3: "divide",
        4: "quit"
    }
    print switcher.get(arguement, "Invalid request")
def add(num1,num2):
    result=num1+float(num2)
    print "the total is %s" % result

def subtract(num1,num2):
    result=num1-float(num2)
    print "the total is %s" % result

def multiply(num1,num2):
    result= num1*float(num2)
    print "the total is %s" % result

def divide(num1,num2):
    try:
        result = num1/float(num2)
        print "the total is %s" % result

    except ZeroDivisionError:
        print "You gonna break this computer if you try to divide by zero!"
        print "Try anyway? "
        txt = raw_input("y/n ")
        if txt == "y":
            while True:
                sys.stdout.write("9")
                sys.stdout.flush()
            else:
                sys.exit()



def main():
    while True:
        print "0) add\n1) sub\n2) multiply\n3) divide\n4) quit"
        print "Enter your choice"
        choice = int(raw_input("Choose an option: "))
        num1 = int(raw_input("Enter number 1: "))
        num2 = int(raw_input("Enter number 2: "))
        if choice == 0:
            add(int(num1), int(num2))
        elif choice ==1:
            subtract(int(num1), int(num2))
        elif choice ==2:
            multiply(int(num1), int(num2))
        elif choice ==3:
            divide(int(num1), int(num2))
        elif choice==4:
            sys.exit()
        else:
            "Invalid option"
main()
