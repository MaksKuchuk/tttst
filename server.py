import socket
import keyboard
from keyboard._keyboard_event import KEY_DOWN, KEY_UP

def on_action(key, conn):
    if key.name == 'unknown':
        return

    if key.event_type == KEY_DOWN:
        conn.sendall(('1' + key.name).encode('ascii'))

    elif key.event_type == KEY_UP:
        conn.sendall(('0' + key.name).encode('ascii'))


HOST = '127.0.0.1'         # Symbolic name meaning all available interfaces
PORT = 50005                        # Arbitrary non-privileged port
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            keyboard.hook(lambda k: on_action(k, conn))

            keyboard.wait()
    








