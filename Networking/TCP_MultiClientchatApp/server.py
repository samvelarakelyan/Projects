import threading
import socket as Socket
import sys


HOST = "localhost"
PORT = 5050
CLIENTS = []  # Sockets of all active clients
NICNAMES = []  # Nicknames of all active clients


try:
    server = Socket.socket(family=Socket.AF_INET, type=Socket.SOCK_STREAM)
    print("Server Created...")
except Exception as e:
    print(e)
    sys.exit()

try:
    server.bind((HOST, PORT))
except Exception as e:
    print(e)
    server.close()
    sys.exit()

try:
    server.listen()
    print(f"Server listen at {HOST}:{PORT}")
except Exception as e:
    print(e)
    server.close()
    sys.exit()


def broadcast(message):
    """
    Function to send message all the clients
    """
    for client in CLIENTS:
        client.send(message)


def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            if msg.decode("utf-8").startswith("KICK"):
                if NICNAMES[CLIENTS.index(client)] == "admin":
                    nameToKick = msg.decode("utf-8")[5:]
                    kickUser(nameToKick)
                else:
                    client.send("Command was refused!".encode("utf-8"))
            elif msg.decode("utf-8").startswith("BAN"):
                if NICNAMES[CLIENTS.index(client)] == "admin":
                    nameToBan = msg.decode("utf-8")[4:]
                    with open("bans.txt", 'a') as f:
                        f.write(f"{nameToBan}\n")
                    print(f"{nameToBan} was banned!")
                else:
                    client.send("Command was refused!".encode("utf-8"))
            else:
                broadcast(message)
        except Exception as e:
            if client in CLIENTS:
                print(e)
                index = CLIENTS.index(client)
                CLIENTS.remove(client)
                client.close()
                nickname = NICNAMES[index]
                NICNAMES.remove(nickname)
                broadcast(f"{nickname} left the chat!".encode("utf-8"))
                break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address[0]}:{address[1]}")

        client.send("Name:> ".encode("utf-8"))
        name = client.recv(1024).decode("utf-8")

        with open("bans.txt", 'r') as f:
            bans = f.readlines()

        if f"{name}\n" in bans:
            client.send("BAN".encode("utf-8"))
            client.close()
            continue

        if name == "admin":
            client.send("PASS:> ".encode("utf-8"))
            password = client.recv(1024).decode("utf-8")

            if password != "adminpass":
                client.send("REFUSE".encode("utf-8"))
                client.close()
                continue

        NICNAMES.append(name)
        CLIENTS.append(client)

        print(f"Name of the client is {name}!")
        broadcast(f"{name} joined the chat!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kickUser(nameToKick):
    if nameToKick in NICNAMES:
        nameIndex = NICNAMES.index(nameToKick)
        clientToKick = CLIENTS[nameIndex]
        CLIENTS.remove(clientToKick)
        NICNAMES.remove(nameToKick)
        clientToKick.send("You were kicked by an admin!".encode("utf-8"))
        clientToKick.close()
        broadcast(f"{nameToKick} was kicked by an admin!".encode("utf-8"))


receive()
