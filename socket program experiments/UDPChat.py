###########################################
# Import modules
###########################################
from socket import *
from threading import Thread

global clientSocket 

###########################################
# Define receiving thread
###########################################
def receive():
    global clientSocket
    while True:
        # Receive the response message
        modifiedMessage, friendAddress = clientSocket.recvfrom(2048)
        print('From my friend: {}'.format(modifiedMessage.decode()))
       
###########################################
# Create a socket
###########################################              
#myName = gethostbyname(gethostname()) 	# for UNIX systems (Mac and Linux)
#myName = '129.10.47.106'
myPort = 12000                          # Server address and port

# Create a UDP socket
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('', myPort))

# Start receiving
rcvthread = Thread(target=receive, args = ())
rcvthread.start()

###########################################
# Start sending
###########################################
friendName = '10.110.20.169'
friendPort = 12000
while True:
    message = input('Send your friend a message:')
    clientSocket.sendto(message.encode(), (friendName, friendPort))

###########################################
# Close the socket
###########################################
clientSocket.close()




