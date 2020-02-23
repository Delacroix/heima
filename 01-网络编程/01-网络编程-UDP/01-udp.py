import socket


def main():
    #创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 要发送的数据
    send_data = input("输入要发送的数据：")

    # 发送数据
    # udp_socket.sendto("hahaha", 对方的IP以及PORT)
    # udp_socket.sendto(b"hahaha", ("192.168.2.217", 8080))
    udp_socket.sendto(send_data.encode("utf-8"), ("192.168.2.217", 8080))
    # 关闭套接字
    udp_socket.close()

    print("-----run-----")


if __name__ == '__main__':
    main()
