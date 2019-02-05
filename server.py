
import socket

sock = socket.socket()
sock.bind(('',8443))
sock.listen(10)

conn, addr = sock.accept()

while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
