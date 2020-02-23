import socket


def main():
    # 1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息
    udp_socket.bind(("", 7890))
    while True:
    # 3.要发送的数据
        send_data = input("输入要发送的数据：")

        # 4.如果输入 exit，就推出
        if send_data == "exit":
            break
        # 5.发送数据
        # udp_socket.sendto("hahaha", 对方的IP以及PORT)
        # udp_socket.sendto(b"hahaha", ("192.168.2.217", 8080))
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.2.217", 8080))
        # 6.关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
