# echo-client.py

import socket
import ceasar

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 64020  # The port used by the server
data_packet = 50
message = "My test message. A Z."
cipher_key = 4
separator = "/n/t/n/t" #разделяет в сообщении ключ от самого сообщения
message_with_key = str(cipher_key) + separator + message
print(f"Sending message: {message}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    #message_with_key = str(cipher_key) + separator + message
    s.sendall(message_with_key.encode())
    data = s.recv(1024)

print(f"Received encrypted messageЖ {data!r}")
str_message = data.decode('UTF-8')
decode_message = ceasar.cipher_decrypt(str_message, cipher_key)
print(f"Received encrypted message: {decode_message}")