import socket 
import threading


def send_message(client):
    while True:
        msg = input("")

        send_msg = f"{username}>> {msg}"
        client.send(send_msg.encode())

def recive_message(client):
    while True:
        response = client.recv(4096)
        print(response.decode())

def server():
    global username
    username = input("enter a username: ")
    IP = input("enter your IP: ")
    PORT = int(input("enter a free PORT: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((IP,PORT))
    server.listen(3)
    print(f"server is listening on port: {PORT}")

    
    client, addr = server.accept()
    print(addr[0],":",addr[1],"connected")

    threading.Thread(target=send_message, args=(client,)).start()
    threading.Thread(target=recive_message, args=(client,)).start()
   
server()

