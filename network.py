import socket
import pickle

host_port = ('', 5321)

def connect_player():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(host_port)
        connected_player = client.recv(4096).decode()
    return connected_player

def send_player(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.send(str.encode(data))
        return pickle.loads(client.recv(4096))

def get_player():
    player = connect_player()
    return player

