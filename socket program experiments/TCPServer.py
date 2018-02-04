###########################################
# Import module
###########################################
from socket import *

###########################################
# Create a TCP listening socket
###########################################
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

###########################################
# Start to listen
###########################################
serverSocket.listen(1)
print('The server is ready to receive')
#print(serverSocket.getsockname())

###########################################
# Accept connections and transmit data
###########################################
while True:
     # Create a communication socket for the cotacting client
     connectionSocket, addr = serverSocket.accept()
     #print(connectionSocket.getsockname())
     
     # Receive at the communication socket
     sentence = connectionSocket.recv(1024).decode()
     print('From Client: {}'.format(sentence))
         
     # Feedback via the communication socket
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence.encode())
     
     # Close the communication socket
     connectionSocket.close()
