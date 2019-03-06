
def writeFile(x,y):
    filename = "newfile.txt"
    f = open(filename,"w")
    z = 0
    while z < y:
        f.write("This is line %d\r\n" % (z))
        z = z + 1
    f.close()

writeFile("newfile.txt",10)
