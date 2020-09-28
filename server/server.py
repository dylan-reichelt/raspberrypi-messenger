
#socket_echo_server.py

import socket
import sys

class MyServer:
    
    def __init__(self, address, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (address, int(port))
        print('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)

        # Listen for incoming connections
        self.sock.listen(1)

    def run(self):

        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                print('connection from', client_address)

               # Receive the data in small chunks and retransmit it
                while True:
                   data = connection.recv(16)
                   print('received {!r}'.format(data))
                   if data:
                       print('sending data back to the client')
                       connection.sendall(data)
                   else:
                       print('no data from', client_address)
                       break
                   
            finally:
               # Clean up the connection
               connection.close()

