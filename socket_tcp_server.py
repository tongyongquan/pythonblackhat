# _*_ coding:utf-8 _*_


'''
    # 还是先讲讲代码思路
    # 1.导入socket模块
    # 2.创建套接字
    # 3.绑定IP地址和端口
    # 4.linsten监听,使套接字由主动变成被动
    # 5.accept() 等待客户端的接入
    # 6.recv() 接收客户端发来的消息
    # 7.反馈消息给客户端,表示已接收到
    # 8.关闭套接字
    # 9.关闭服务器
'''
# 1.导入socket模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.使用bind()绑定IP地址和端口
tcp_server_socket.bind(("127.0.0.1", 8080))

# 4.linsten监听,使套接字由主动变成被动
tcp_server_socket.listen(128)
while True:
    # 5.accept() 等待客户端的接入
    server_socket, ip_port = tcp_server_socket.accept()
    print(ip_port, "客户端已经连接")
    while True:
        # 6.recv() 接收客户端发来的消息
        server_data = server_socket.recv(1024)

        # 对客户端发来的信息进行判断.如果有内容就解码打印显示,如果为空就退出
        if server_data:
            server_data = server_data.decode()
            print("收到新消息 : ", ip_port, ":", server_data)
            # 7.反馈消息给客户端,表示已接收到
            server_socket.send("已收到".encode())
        else:
            # 如果发送内容为空则跳出 while True 循环
            break

    # 8.关闭套接字
    server_socket.close()
    # 9.关闭服务器,因为服务端一直在接收别人的信息,所以可以不用关闭.
# tcp_client_socket.close()

