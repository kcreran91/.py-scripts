from udp import *
from time import *

def onUDPReceive(ip, port, data):
	print("Reply from " + ip)

socket = UDPSocket()
socket.onReceive(onUDPReceive)
socket.begin(1235)

<<<<<<< Updated upstream
network = "10.28.167."
=======
network = "10.87.169."
>>>>>>> Stashed changes
	
for host in range(255):

	ip = (network + str(host))

	socket.send(ip, 1235, "")
	delay(1)