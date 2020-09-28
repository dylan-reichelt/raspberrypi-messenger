
import sys
from server import MyServer

def applicationStart(address, port):
    server = MyServer(address, port)
    server.run()

if __name__ == "__main__":
    applicationStart(sys.argv[1], sys.argv[2])