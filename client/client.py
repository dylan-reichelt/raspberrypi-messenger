import socket

class MySocket:

    def __init__(self, address, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.server_address = (address, int(port))
        print('connecting to {} port {}'.format(*self.server_address))
        self.sock.connect(self.server_address)
    
    def run(self):
        try:

            # Send data
            message = b'This is the message.  It will be repeated.'
            print('sending {!r}'.format(message))
            self.sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('closing socket')
            self.sock.close()

