from client import MySocket
import sys

def applicationStart(host, port, message):
    socket = MySocket(host, port)
    socket.run(message)

if __name__ == "__main__":
    applicationStart(sys.argv[1], sys.argv[2], sys.argv[3])