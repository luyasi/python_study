import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 8001))

sends = input(">>>")

sock.send(sends.encode("utf-8"))

recvs = sock.recv(1024)

print(recvs.decode("utf-8"))

sock.close()
