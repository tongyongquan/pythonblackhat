# encoding: utf-8

'''
    TCP是,面对连接,需要先建立连接,然后传输数据,最后再断开连接.
    TCP的优点:
        1.TCP是一种面向连接,需要先建立连接才可以传输数据.
        2.可靠传输:
               1).发送应答机制:TCP发送的每个报文段,都必须得到接收方的应答才认为这个TCP的报文段发
                  送成功
               2).错误效验:TCP会使用一种效验函数来检查传输的数据是否错误,传输和和接收的时候都会进
                  行检查
               3).超时重发:发送端发送一个报文段就会进入计时,如果再一定时间内没有收到应答就会重发这
                  个报文段
               4).阻塞管理:流量控制,用来防止因为对方发送消息过快,而导致消息接收不完全.
'''

# 1.导入socket模块
import socket

# 2.使用socket模块,调用socket方法,创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.建立和TCP服务器的连接
# 使用connect()方法来建立和服务器的连接
#                              windows IP    端口号
tcp_client_socket.connect(("127.0.0.1", 8080))

# 4.调用send方法,发送消息
tcp_client_socket.send("你好,我叫宇宙无敌天下第一帅".encode())

# 5.接收TCP服务器返回的消息
# TCP使用recv()返回参数,返回的只有二进制的内容,没有IP地址和端口,这一点和UDP的recvfrom()不一样
udp_data = tcp_client_socket.recv(1024)
# 网络调试助手发送消息是默认gbk方式,所以咱们解包操作 gbk
print("收到新的消息 : ", udp_data.decode("utf-8"))

# 6.关闭套接字,释放电脑空间
tcp_client_socket.close()

