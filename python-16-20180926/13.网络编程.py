""""""
"""
网络编程：是如何在程序中实现两台计算机的通讯

socket
socketserver

服务端：被动相应的叫服务端
客户端：主动发起呼叫的叫客户端

单工：通讯通道只有一条，通讯双方不可逆。
半双工：通讯通道只有一条，通讯双方可逆。
全双工：通讯通道有多条。

服务端
1、导入socket模块
import socket

2、创建socket对象，socket是一个类
    sock = socket.socket(socket_family,socket_type)
        socket_family
            socket.AF_INET   ipv4
            socket.AF_INET6  ipv6
            socket.AF_UNIX   使用unix内部传输
        socket_type
            socket.SOCK_STREAM   TCP协议
            socket.SOCK_DGRAM    UDP协议
3、绑定ip和端口
    sock.bind(("ip",端口号))
4.设置最大监听数量
    sock.listen(100)
5.接受信息
    con,add = scok.accept()
    con:接受sock对象
    add:接受ip和端口号 组成双元素元组
    print(con.recv(1024))
    con.send("要发送的消息")
6.关闭socket
    socket.close()
    
客户端
1、导入模块
2、创建socket对象
3、连接服务器
    sock.connent(("服务器的ip",端口))
4、接受信息
    sock.send("要发送的信息")
    print(sock.recv(1024))
5、关闭socket
    sock.close()

"""
