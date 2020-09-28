from client import MySocket
import sys

def applicationStart(host, port):
    socket = MySocket(host, port)
    socket.run()

if __name__ == "__main__":
    applicationStart(sys.argv[1], sys.argv[2])