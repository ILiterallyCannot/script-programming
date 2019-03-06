#-*- coding: UTF-8 -*-


def calculator(cmd, num1, num2):

    if cmd =="add":
        return num1+num2
    elif cmd =="sub":
        return num1-num2
    elif cmd == "multiply":
        return num1*num2
    else:
        return ("invalid function")

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
print(calculator("div", 1, 2)) #should print 2
