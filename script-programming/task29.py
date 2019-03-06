import sys
import csv
def switch_case(arguement):
    switcher = {
        0: "read",
        1: "add",
        2: "remove"
    }
    print switcher.get(arguement, "Invalid request")
def readfile():
    f = open("task29list.txt", "r")
    lines=f.readlines()
    lines.sort()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        print lines[i]
    f.close()

def addtofile():
    txt=raw_input("Add an item to the list!: ")
    f = open("task29list.txt", "a")
    f.write("%s \r\n" % txt)
    print "You added %s" % txt
    f.close()
    readfile()

def removefromfile():
    readfile()
    f = open("task29list.txt", "r")
    a = []
    lines=f.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        a.append(lines[i])
    open('task29list.txt', 'w').close()
    print a
    item=raw_input("Remove an item to the list!: ")
    a.remove(item)
    with open("task29list.txt", "w") as f:
        for item in a:
            f.write("{}\n".format(item))
    readfile()
def main():
    while True:
        print "0) read the file\n1) add to the file\n2) remove from the file\n3) quit"
        print "Enter your choice"
        choice = int(raw_input("Choose an option: "))
        if choice == 0:
            readfile()
        elif choice ==1:
            addtofile()
        elif choice ==2:
            removefromfile()
        elif choice ==3:
            sys.exit()
        else:
            "Invalid option"
main()
