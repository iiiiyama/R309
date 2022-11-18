import socket


def client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1212
    client_socket.connect((host, port))
    data = client_socket.recv(1024)    ######## réception des données #########
    message = input("->")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('received from server: ' + data)
        message = input("->")

    client_socket.close()                       ######## ferme la communication #########
    print(data), 'Reçue'


if __name__ == '__main__':
    client()