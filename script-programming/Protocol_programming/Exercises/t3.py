import sys

def sum2(numero):
	sum=0	
	#while y <= x:
	 #y += 1
	for x in range(0, numero+1):
	 sum += x
 	return sum
	 # y += 1

numero= int(sys.argv[1])

 	if len(sys.argv) != 1:
		print "väärä määrä parametreja"
 	else:
  		print sum2(x)
