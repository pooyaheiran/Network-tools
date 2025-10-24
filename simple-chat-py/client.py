import socket 
import threading
import sys

def main():
    global username 
    username = input("enter a username: ")
    IP = input("enter host IP: ")
    PORT = int(input("enter host PORT: "))
        
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((IP, PORT))
    threading.Thread(target=send_message, args=(client,)).start()
    threading.Thread(target=recive_message, args=(client,)).start()


def send_message(client):
    while True:
        msg = input()
        if msg == ".exit":
            sys.exit()
        send_msg = f"{username}>> {msg}"
        client.send(send_msg.encode())

def recive_message(client):
    while True:
        recv = client.recv(4096)
        print(recv.decode())

main()
