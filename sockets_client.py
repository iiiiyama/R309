import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             ######## crée le socket ##########
host = socket.gethostname()
port = 12121
client_socket.connect((host, port))  ######## se connecte à l'host et au port #########
client_socket.send('testest')               ######## envoie les données ########
data = client_socket.recv(1024)    ######## réception des données #########
client_socket.close()                       ######## ferme la communication #########
print(data), 'Reçue'