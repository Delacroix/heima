import socket


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("", 7890))

    # 3.将手机设置为响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    # 这个while True循环为多个客户端服务
    while True:
        print("等待一个新的客户端到来...")
        # 4.等待电话（等待客户端连接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已连接: %s" % str(client_addr))

        # 这个while True循环多次为同一个客户端多次服务
        while True:

            # 接收客户端发来的数据，注意收发数据用的新套接字 new_client_socket
            recv_data = new_client_socket.recv(1024)  # 阻塞
            print("客户端发送过来的消息: %s" % recv_data.decode("gbk"))

            # 如果recv解阻塞，有2种情况：
            # 1.客户端发送过来数据
            # 2.客户端调用close，导致recv解阻塞
            if recv_data:
                new_client_socket.send("数据已发送成功----------OK-----------".encode("gbk"))
            else:
                break
        # 关闭套接字
        # 关闭accept返回的套接字，意味着不再为该客户端服务
        new_client_socket.close()
        print("已经服务完毕！")
    # 如果将listen套接字关闭，将会导致无法接受新客户端的连接，即xxx.accept就会失败
    tcp_server_socket.close()

    # listen套接字负责等待新的客户端进行连接
    # accept产生的新的套接字 为客户端服务
    # listen 和 accept 为一对多关系


if __name__ == '__main__':
    main()
