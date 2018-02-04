###########################################
# Import Modules
###########################################
from socket import *

###########################################
# Create a UDP socket
###########################################
clientSocket = socket(AF_INET,SOCK_DGRAM)

# Server address and port
serverName = '10.110.20.169'
serverPort = 12000

# Send a message
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
#print(clientSocket.getsockname())

###########################################
# Receive the response message
###########################################
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('From Server: {}'.format(modifiedMessage.decode()))
#print(serverAddress)

# Close the socket
clientSocket.close()
