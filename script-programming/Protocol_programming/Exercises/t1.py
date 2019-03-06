# -*- coding: utf-8 -*-

def compare(x, y):
	if x > y: 
	 print x
	elif y > x:
	 print y
	else:
	 print "luvut ovat yhtasuuret"

x = raw_input("Anna luku 1:")
y = raw_input("Anna luku 2:")

compare(x, y)
