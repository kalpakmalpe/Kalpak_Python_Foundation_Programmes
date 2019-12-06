import socket

#1. create a  new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
print("Server Socket Created...")

#2. Reserver Port
port = 9999
#3. Get Host of a local machine
host = socket.gethostname()

#4. Bind socket with host and ip
s.bind((host,port))
print("servrsocket binded with", host)

#5. Put socket in listen mode
s.listen(5)
print("Server socket is listening on port", port)

while(True):

    #6. Accpet if anyt lcient connects to serversocket
    clientsocket, clienthost =  s.accept()
    print("client Socket connected to server : ", clienthost)

    #7. If connected send some data to client socket
    message = "Hello"
    clientsocket.send(message.encode())
    print("Response Sent to Client")

    #8. close the connection with current client socket
    clientsocket.close()
    print("Client Connection closed!")




