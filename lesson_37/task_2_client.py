import socket, time
from colorama import Fore, init
import random
import threading

init()

colors = [Fore.GREEN, Fore.YELLOW, Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX]

client_color = random.choice(colors)

# HOST = "165.232.68.171"  # The server's hostname or IP address
HOST = '127.0.0.1'
PORT = 65432        # The port used by the server

def listen_msg(s):
    while True:
        data = s.recv(1024).decode()
        print("\n"+data)



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'[*] Connecting {HOST}:{PORT}')
    print(f'[*] Connected')


    t = threading.Thread(target=listen_msg, args=(s,), daemon=True)
    t.start()
    name = input("Enter your Name: ")
    while True:
        to_send = input("Enter Message: ")
        date_now = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        to_send = f'[{date_now}]  {name}:{to_send}{Fore.GREEN}'
        s.send(to_send.encode())