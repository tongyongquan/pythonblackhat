# -*- coding:UTF-8 -*-
import sys
import socket
import getopt
import threading
import subprocess
import time

listen = False
command = False
execute = ""
upload_destination = ""
port = 22

# 如果没有定义目标，那么我们监听所有接口
target = "0.0.0.0"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((target, port))

server.listen(5)
print('等待连接')

# 5.accept() 等待客户端的接入
client_socket, ip_port = server.accept()
print(ip_port, "客户端已经连接")
client_socket.send("<TYQ:#>：".encode())

while True:
    # 6.recv() 接收客户端发来的消息
    recv_len =1
    client_data = ''

    while recv_len:
        data = client_socket.recv(1024)
        recv_len = len(data)
        client_data += data.decode("utf-8")

        if recv_len < 1024:
            break

    # 对客户端发来的信息进行判断.如果有内容就解码打印显示,如果为空就退出
    if client_data != 'exit':
        print("收到新消息 : ", ip_port, ":", client_data)
        output = subprocess.check_output(
            client_data, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)  # 命令执行模块
        # 7.反馈消息给客户端,表示已接收到
        client_socket.send(output.encode())
        print(output)

    else:
        # 如果发送内容为空则跳出 while True 循环
        break

# 8.关闭套接字
client_socket.close()