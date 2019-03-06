import socket
import toiminnallisuus

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost"), 8888)
sock.listen(5)

client_toiminnallisuus, addr = sock.accept()
viesti = toiminnallisuus.lue_viesti(client_toiminnallisuus)
print viesti

toiminnallisuus.laheta_viesti(client_toiminnallisuus, "sain t: Serveri")
client_toiminnallisuus.close()
sock.close()
