import socket
import time


tcp_client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_tcp.bind(("", 7890))

tcp_client_tcp.listen(128)
tcp_client_tcp.setblocking(False)  # 设置套接字为非阻塞

client_socket_list = list()

while True:

    time.sleep(0.5)

    try:
        new_socket, new_addr = tcp_client_tcp.accept()
    except Exception as ret:
        print("---没有新的客户端---")
    else:
        print("---只要没有产生异常，那么意味着来了一个新的客户端---")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print(ret)
            print("---这个客户端没有发送过来数据---")
        else:
            if recv_data:
                # 对方发送过来数据
                print("---客户端发送过来了数据---")
                print(recv_data.decode("utf-8"))
            else:
                # 对方调用close 导致了 recv返回
                client_socket_list.remove(client_socket)
                client_socket.close()
                print("---客户端已经关闭---")
