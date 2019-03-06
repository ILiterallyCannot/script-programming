import socket

osoite = "localhost"
portti = 8888
tiedosto = "ibis.jpg"
#tiedosto = "sikapossu.txt"
def main():
	soketti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soketti.connect((osoite,portti))

	soketti.send(tiedosto+"\n")

	filu = open(tiedosto, "rb")

	data = filu.read(1024)

	while data:
		soketti.send(data)
		data = filu.read(1024)

	print "The file was sent! "
	filu.close()
	soketti.close()

main()
