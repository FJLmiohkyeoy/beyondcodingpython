# server.py
import threading
import socket

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()


def handle_client(conn, addr, username):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr} {username}] {msg}")
            with clients_lock:
                for c in clients:
                    c.sendall(f"[{username}] {msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    print("[SERVER STARTED]!")
    server.listen()
    while True:
        conn, addr = server.accept()
        with clients_lock:
            username = conn.recv(1024).decode(FORMAT)
            clients.add(conn)
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, username), daemon=True
        )
        thread.start()


start()

# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server.bind(("localhost", 9999))

# server.listen()

# client, addr = server.accept()

# done = False

# while not done:
#     msg = client.recv(1024).decode("utf-8")
#     if msg == "quit":
#         done = True
#     else:
#         print(msg)
#     client.send(input("Message: ").encode("utf-8"))
