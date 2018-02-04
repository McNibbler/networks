###########################################
# Import module
###########################################
from socket import *

###########################################
# Create a TCP socket 
###########################################
clientSocket = socket(AF_INET, SOCK_STREAM)

###########################################
# Establish a TCP Connection
###########################################

# Server socket informaiton
serverName = '129.10.47.106'
serverPort = 12000

# Contact the server using server socket information
clientSocket.connect((serverName,serverPort))

###########################################
# Send a message to the server
###########################################
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())

###########################################
# Receiver feedback from the server
###########################################
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())

###########################################
# Close the socket
###########################################
clientSocket.close()
