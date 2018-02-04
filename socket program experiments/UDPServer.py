###########################################
# Import Modules
###########################################
from socket import *

###########################################
# Create a UDP socket
###########################################
serverSocket = socket(AF_INET, SOCK_DGRAM)    
#print(dir(serverSocket))
serverPort = 12000
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
#print(serverSocket.getsockname())

###########################################
# Receive and send using the created UDP socket
###########################################
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('From Client: {}'.format(message.decode()))
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
