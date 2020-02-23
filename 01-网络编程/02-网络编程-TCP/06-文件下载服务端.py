import socket


def send_file_2_client(new_client_socket, client_addr):
    # 1.接收客户端发来的要下载的文件名
    file_name = new_client_socket.recv(1024).decode("gbk")
    print("客户端(%s)需要下载的文件名是：%s" % (str(client_addr), file_name))

    file_content = None
    # 2.打开文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)

    # 3.发送文件给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("", 7890))

    # 3.将手机设置为响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    print("----------1------------")

    while True:
        # 4.等待电话（等待客户端连接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5.调用发送文件函数，完成服务
        send_file_2_client(new_client_socket, client_addr)

        # 6.关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

    # listen套接字负责等待新的客户端进行连接
    # accept产生的新的套接字 为客户端服务
    # listen 和 accept 为一对多关系


if __name__ == '__main__':
    main()