# listener.py
import socket
import threading

def receive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 3333))
    s.listen(1)
    print("Waiting for connection...")
    c, addr = s.accept()
    print("Connected to", addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("Received:", data.decode())

def send():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.X", 3333))
    while True:
        message = input("Enter message: ")
        if message == "q":
            break
        s.send(message.encode())
    s.close()

t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=send)
t1.start()
t2.start()
t1.join()
t2.join()
