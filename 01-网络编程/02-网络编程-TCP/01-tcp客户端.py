import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 注意是SOCK_STREAM，跟UDP的SOCK_DGRAM区分
    # 2.连接服务器
    server_ip = input("输入服务器的ip:")
    server_port = int(input("输入服务器的port:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    # 3.发送接收数据
    send_data = input("输入要发送的数据:")
    tcp_socket.send(send_data.encode("utf-8"))
    # 4.关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
