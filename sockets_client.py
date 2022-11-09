import socket


client_socket = socket.socket()             ######## crée le socket ##########
client_socket.connect(('localhost', 10000))  ######## se connecte à l'host et au port #########
client_socket.send('testest')               ######## envoie les données ########
data = client_socket.recv(1024).decode()    ######## réception des données #########
client_socket.close()                       ######## ferme la communication #########
print(data), 'Reçue'