x=1
try:
    print "NameError test: x=1, y does not exist. \n"
    print "Printing x: "
    print x
    print "\nPrinting y: "
    print y
except NameError:
    print "NameError! \n"

list=["apples","oranges","bananas","forks"]
try:
    print "\nPrinting a test list:"
    print list
    print "\nPrinting list[3]:"
    print list[3]
    print "\nPrinting list[6]: "
    print list[6]
except IndexError:
    print "IndexError! \n"

dict = {"A":1,"B":2}
try:
    print "Printing a test dictionary: "
    print "dict = %s " % dict
    print "\nPrinting dict[B]: "
    print dict["B"]
    print "\nPrinting dict[C]: "
    print dict["C"]
except KeyError:
    print "KeyError!"
