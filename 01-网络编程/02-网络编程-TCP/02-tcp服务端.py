import socket


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("", 7890))

    # 3.将手机设置为响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    print("----------1------------")
    # 4.等待电话（等待客户端连接 accept）
    new_client_socket, client_addr = tcp_server_socket.accept()
    print("---------2----------")
    print(client_addr)

    # 接收客户端发来的数据，注意收发数据用的新套接字 new_client_socket
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    new_client_socket.send("hahaha----------OK-----------".encode("utf-8"))

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()

    # listen套接字负责等待新的客户端进行连接
    # accept产生的新的套接字 为客户端服务
    # listen 和 accept 为一对多关系


if __name__ == '__main__':
    main()