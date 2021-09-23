import socket as Socket
import threading
from queue import Queue


target = "localhost"
openPorts = []
myQueue = Queue()


def portScan(port):
    try:
        socket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
        socket.connect((target, port))
        return True
    except Exception:
        return False


def fillQueue(portList):
    for port in portList:
        myQueue.put(port)


def worker():
    while not myQueue.empty():
        port = myQueue.get()
        if portScan(port):
            print(f"Port {port} is open!")
            openPorts.append(port)


portList = range(1, 1025)
fillQueue(portList)

threadList = []

for t in range(10 ** 4):
    thread = threading.Thread(target=worker)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

print(f"Open porsts are: {openPorts}")
