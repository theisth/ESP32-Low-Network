import socket 

HEADER = 64
PORT = 53
SERVER = '172.16.2.160'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECTED'
ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send('ahmet')
