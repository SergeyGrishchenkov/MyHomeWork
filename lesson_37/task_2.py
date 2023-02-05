# Create a socket echo server which handles each connection in a separate Thread
import socket, time, threading

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
clients = []
def listen_msg(conn):
    with conn:
        while True:
            try:
                data_enc = conn.recv(1024)
                data = data_enc.decode()
            except Exception as s:
                clients.remove(conn)
            for client in clients:
                client.sendall(data.encode())

def listen_msg_echo(conn):
    with conn:
        while True:
            try:
                data_enc = conn.recv(1024)
                data = data_enc.decode()
                conn.sendall(data.encode())
            except Exception as s:
                clients.remove(conn)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Satrt listening as {HOST} {PORT}')
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        t = threading.Thread(name=str(addr[1]), target=listen_msg_echo, args=(conn,), daemon=True)
        print(f"Connected [{addr[0]}] = [{addr[1]}] = [{itsatime}]. the connection was placed in the stream {t.name} ")
        print(f'Now there are {threading.active_count()} alive threads')
        t.start()
