import socket
from threading import Thread

host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

clients = {}
addresses = {}

def handle_clients(conn,addr):
    name = conn.recv(1024).decode()
    welcome = f"welcome {name}. tab #quit to get out of chatroom"
    conn.recv(bytes(welcome,"utf8"))
    msg = name + "has already joined to chatroom"
    broadcast(bytes(msg,"utf8"))
    clients[conn] = name

    while True:
        msg = conn.recv(1024)
        if msg != "#quit":
            broadcast(msg,name,":")
        else:
            conn.send(bytes("#quit","utf8"))
            conn.close()
            del clients[conn]

def accept_clients_connection():
    while True:
        client_conn,conn_address=sock.accept()
        print(conn_address,"Has connected...")
        client_conn.send("Welcome to chatroom. please type your name to continue ".encode("utf8"))
        addresses[client_conn] = conn_address
        Thread(target=handle_clients,args=[client_conn,conn_address])

def broadcast(msg,prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+msg)


if __name__ == "__main__":
    sock.listen(5)
    print("server is listening to requests sent by clients...")
    thread = Thread(target=accept_clients_connection)
    thread.start()
    thread.join()