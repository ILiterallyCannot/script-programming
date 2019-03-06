import socket

osoite = "localhost"
portti = 8888
polku = "/home/student/script-programming/Protocol_programming/Exercises/filu/This/"

def main():
	sukka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sukka.bind((osoite,portti))
	sukka.listen(5)

	while True:
		client, addr = sukka.accept()
		print "uusi yhteys osoitteesta", addr

		tiedosto = client.recv(1)
		while not "\n" in tiedosto:
			tiedosto += client.recv(1)

		tiedosto = tiedosto.strip()
		print len(tiedosto), tiedosto


		filu = open(polku+tiedosto, "wb")


		data = client.recv(1024)

		while data:
			filu.write(data)
			data = client.recv(1024)


		filu.close()
		print "Filu vastaanotettu"


main()
