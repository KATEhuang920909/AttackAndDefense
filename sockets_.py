# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/4 9:26
@Author: huangkai2
@File:config.py
@Software: PyCharm
"""
import socket

# 创建基于IPv4的TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# 设置socket选项以接收所有的IP头
sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# 绑定到端口8080（可以更改为任何你想监听的端口）
sock.bind(('0.0.0.0', 8080))

# 设置socket为监听模式
sock.listen(5)

while True:
    # 接收数据（在这个例子中，我们假设我们会收到SYN+ACK包）
    data = sock.recvfrom(65535)

    # 解析IP头和TCP头（需要对TCP头进行详细了解）
    ip_header = data[0][:20]
    tcp_header = data[0][20:40]

    # 解析TCP头中的源和目标端口
    src_port = (tcp_header[0] << 8) + tcp_header[1]
    dst_port = (tcp_header[2] << 8) + tcp_header[3]

    # 创建一个新的TCP头，其中包含RST标志
    new_tcp_header = tcp_header[0:2] + b'\x18' + tcp_header[3:]

    # 重新计算IP头中的校验和（通常需要对IP头和TCP头有深入了解）
    # 这里省略了校验和的计算，因为它超出了简短回答的范围

    # 发送RST包
    sock.sendto(ip_header + new_tcp_header, data[1])