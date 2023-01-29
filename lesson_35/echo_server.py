import socket
import ceasar

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 64020  # Port to listen on (non-privileged ports are > 1023)
data_packet = 50

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(data_packet)
                if not data:
                    break
                data_str = data.decode('UTF-8')
                key, main_data = data_str.split(sep="/n/t/n/t")
                encode_data = ceasar.cipher_encrypt(main_data, int(key))
                print(encode_data)
                conn.sendall(encode_data.encode())
    print('server stopped')