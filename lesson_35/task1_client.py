import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 60888  # The port used by the server
data_packet = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    client_message = "Hello USP server"
    s.sendto(client_message.encode(), (HOST, PORT))
    mes_from_server = s.recvfrom(data_packet)
    message = mes_from_server[0]
    address = mes_from_server[1]

print(f"Received {message.decode('utf-8')}, From: {address}")