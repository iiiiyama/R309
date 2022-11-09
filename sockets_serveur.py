import socket, select


server_socket = socket.socket()
host = socket.gethostname()
port = 12121
server_socket.bind((host, port))
######### écoute les connexions entrantes #########
server_socket.listen(3)
####################################

inputs= [server_socket]
outputs = []

while inputs :
    readable, writeable, exceptionnal = select.select(inputs, outputs, inputs)
    for client_socket in readable:
        if client_socket is server_socket :

            conn, client_address = server_socket.accept()
            inputs.append(conn)

data = server_socket.recv(1024).decode()
server_socket.send('OK')
msg = {}
server_socket.close()