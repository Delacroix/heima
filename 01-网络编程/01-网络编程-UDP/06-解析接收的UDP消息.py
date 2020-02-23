import socket


def main():
    # 1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息  （必须绑定本地的网络）
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)
    # 3.接收数据
    recv_data = udp_socket.recvfrom(1024)
    # recv_data变量存储的是一个元组  （接收的数据，（发送方的ip, port））
    recv_msg = recv_data[0]  #data
    send_addr = recv_data[1]  #addr
    # 4.打印接收的数据
    # print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))   注意windows默认是gbk编码
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))
    # 5.关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
