import threading
import socket as Socket
import sys


SERVER_HOST = "localhost"
SERVER_PORT = 5050
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)


name = input("Enter your name: ")

if name == "admin":
    password = input("Enter password for admin: ")


# Trying to created socket
try:
    client = Socket.socket(family=Socket.AF_INET, type=Socket.SOCK_STREAM)
except Exception as e:
    print(e)
    sys.exit()

# Trying to connect with server
try:
    client.connect(SERVER_ADDRESS)
except Exception as e:
    print(e)
    sys.exit()


stopThread = False


def receive():
    while True:
        global stopThread
        if stopThread:
            break
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "Name:> ":
                # name -> message
                client.send(message.encode("utf-8"))
                nextMessage = client.recv(1024).encode("utf-8")
                if nextMessage == "PASS:> ":
                    client.send(password.encode("utf-8"))
                    if client.recv(1024).decode("utf-8") == "REFUSE":
                        print("Connection was refused! Wrong password!")
                        stopThread = True
                elif nextMessage == "BAN":
                    print("Connection refuse because of ban!")
                    client.close()
                    stopThread = True
            else:
                print(message)
        except Exception as e:
            print(e)
            client.close()
            break


def write():
    while True:
        if stopThread:
            break
        message = f"{name}:> {input('')}"
        if message[len(name) + 2:].startswith("/"):
            if name == "admin":
                if message[len(message) + 2:].startswith("/kick"):
                    messageFromAdmin = f"KICK {message[len(message)+2+6:]}"
                    client.send(messageFromAdmin.encode("utf-8"))
                elif message[len(message) + 2:].startswith("/ban"):
                    messageFromAdmin = f"BAN {message[len(message)+2+5:]}"
                    client.send(messageFromAdmin.encode("utf-8"))
            else:
                print("Commands can only be executed by admin!")
        else:
            client.send(message.encode("utf-8"))


receiveThread = threading.Thread(target=receive)
receiveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
