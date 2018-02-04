from socket import *  # Import socket module
import sys            # In order to terminate the program

# Create a TCP server socket, AF_INET is used for IPv4 protocols,
# 	SOCK_STREAM is used for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 12000

# Bind the socket to server address and server port
serverSocket.bind(('',serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print('The server is ready to receive')

	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	# If an exception occurs during the execution of try clause, /
	# 	the rest of the clause is skipped
	# If the exception type matches the word after except,
	# 	the except clause is executed
	try:
		# Receives the request message from the client
		message = connectionSocket.recv(1024).decode()

		messageSplit = message.split()

		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filepath = messageSplit[1]

		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		filepathName = filepath[1:]

		# Store the entire contenet of the requested file in
		# 	a temporary buffer
		fileBuffer = open(filepathName)
		fileString = fileBuffer.read()


		# Send the HTTP response header line to the connection socket
		connectionSocket.send(("HTTP/1.1 200 OK\n"
								+ "Content-Type: text/html\n"
								+ "\n").encode())

		# Send the content of the requested file to the connection socket
		connectionSocket.send(fileString.encode())

		# Close the client connection socket
		connectionSocket.close()

		# Closes the server socket after a request is processed
		serverSocket.close()

		#Terminate the program after sending the corresponding data
		sys.exit()

	except IOError:
		# Opens and reads custom 404 page HTML file
		fof = open("fof.html")
		fofRead = fof.read()

		# Sends HTTP response message and page for file not found
		connectionSocket.send(("HTTP/1.1 404 Not Found\n"
								+ "Content-Type: text/html\n"
								+ "\n").encode())
		connectionSocket.send(fofRead.encode())

		# Close the client connection socket
		connectionSocket.close()

		# Closes the server socket after a request is processed
		serverSocket.close()

		#Terminate the program after sending the corresponding data
		sys.exit()