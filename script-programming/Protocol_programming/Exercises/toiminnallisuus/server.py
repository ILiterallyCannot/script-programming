import socket
import toiminnallisuus

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8888))
sock.listen(5)

client, addr = sock.accept()
viesti = toiminnallisuus.lue_viesti(client)
print viesti

toiminnallisuus.laheta_viesti(client, "sain t: Serveri")
client.close()
sock.close()
