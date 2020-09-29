import socket

class MySocket:

    def __init__(self, address, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.server_address = (address, int(port))
        print('connecting to {} port {}'.format(*self.server_address))
        self.sock.connect(self.server_address)
    
    def run(self, message):
        recievedMessage = ""
        try:

            # Send data
            byteMessage = message.encode("utf-8")
            print('sending {!r}'.format(message))
            self.sock.sendall(byteMessage)

            # Look for the response
            amount_received = 0
            amount_expected = len(byteMessage)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                recievedMessage += data.decode("utf-8")

        finally:
            if recievedMessage == message:
                print("Message sent successfully :D")
            print('closing socket')
            self.sock.close()

