# -*- coding:UTF-8 -*-
import sys
import socket
import getopt
import threading
import subprocess
import time

# 1.导入socket模块
import socket

# 2.使用socket模块,调用socket方法,创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.建立和TCP服务器的连接
# 使用connect()方法来建立和服务器的连接
#                              windows IP    端口号
tcp_client_socket.connect(("127.0.0.1", 22))

first_data = tcp_client_socket.recv(1024)
# 网络调试助手发送消息是默认gbk方式,所以咱们解包操作 gbk

while(True):
    print(first_data.decode("utf-8"),end='')
    command = input()
    if command == 'exit':

        # 4.调用send方法,发送消息
        tcp_client_socket.send(command.encode())
        break
    tcp_client_socket.send(command.encode())

    # 5.接收TCP服务器返回的消息
    # TCP使用recv()返回参数,返回的只有二进制的内容,没有IP地址和端口,这一点和UDP的recvfrom()不一样
    recv_len = 1
    recv_data = ''

    while recv_len:
        data = tcp_client_socket.recv(1024)
        recv_len = len(data)
        recv_data += data.decode("utf-8")
        if recv_len < 1024:
            break

    # 网络调试助手发送消息是默认gbk方式,所以咱们解包操作 gbk
    print(recv_data)

# 6.关闭套接字,释放电脑空间
tcp_client_socket.close()