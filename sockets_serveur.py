import socket, select


server_socket = socket.socket()
server_socket.bind(('localhost', 10000))
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
            connection.setblocking[0]
            inputs.append(conn)

data = server_socket.recv(1024).decode()
server_socket.send('OK')
msg = {}
server_socket.close()