import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 8001))

sock.listen(10)

con, add = sock.accept()
print("%s已经连接上服务器" % (add[0]))

recvs = con.recv(512)
print(recvs.decode("utf-8"))

sends = input(">>>")
con.send(sends.encode("utf-8"))

sock.close()
