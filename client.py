import socket
import keyboard

HOST = '127.0.0.1'        # The remote host
PORT = 50005              # The same port as used by the server
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            data = data.decode('ascii')

            if data[0] == '1':
                keyboard.press(data[1:])
            else:
                keyboard.release(data[1:])

            








