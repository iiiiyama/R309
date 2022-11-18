import socket

def serveur():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1212
    server_socket.bind((host, port))
    server_socket.listen(3)
    conn_client, client_address = server_socket.accept()

    while True:
        data = conn_client.recv(1024).decode()
        if not data:
            break
        print (f"")
    server_socket.send('OK')
    conn_client.close()
    server_socket.close()


if __name__ == '__main__':
    serveur()