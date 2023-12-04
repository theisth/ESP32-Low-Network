import network

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    #sta.connect('your wifi ssid', 'your wifi password')
    sta.connect('Hudayi','hudayi2019')
    while not sta.isconnected():
        pass

print('network config:', sta.ifconfig())

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((sta.ifconfig()[0],53))

FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = 'DISCONNECTED'

def handle_client(conn, addr):
    print(f'[New connection] {addr} connected')

    connected = True
    
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
        
            if msg == DISCONNECT_MESSAGE:
                connected = False

        
            print(f'[{addr}] {msg}')
            conn.send('Msg received'.encode(FORMAT))
        
    conn.close()


def start():
    print(f'[Listening] Server is {sta.ifconfig()[0]}')
    server.listen(10)
    while True:
        conn, addr = server.accept()
        handle_client(conn,addr)


print('Starting')
start()
