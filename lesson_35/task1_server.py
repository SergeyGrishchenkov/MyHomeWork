# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 60888  # Port to listen on (non-privileged ports are > 1023)
data_packet = 1024

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            data_stream = s.recvfrom(data_packet)
            if not data_stream:
                break
            message = data_stream[0]
            address = data_stream[1]
            print(f'Message: {message}, From: {address}')
            s.sendto(message ,address)
    print('server stopped')