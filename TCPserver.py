import socket

# creating socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 999

# binding socket to host and port
serversocket.bind((host, port))

# starting tcp listeners
serversocket.listen(4)

while True:
    # creating connection
    clientsocket, address = serversocket.accept()

    print("Received connection from %s" % str(address))

    message = 'Hey!, Connected!' +"\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close() 