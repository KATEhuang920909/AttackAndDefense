# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/4 9:26
@Author: huangkai2
@File:config.py
@Software: PyCharm
"""
from scapy.all import *
from scapy.layers.inet import *


# 定义一个发送ICMP请求的函数
def send_icmp_packet(dst_ip, count=3, timeout=2):
    # 创建ICMP数据包
    icmp_packet = ICMP()
    icmp_packet.dst = dst_ip

    # 发送ICMP数据包
    answered = send(icmp_packet, count=count, timeout=timeout)

    # 打印收到的响应
    for packet in answered:
        print(packet.show())


# 使用函数发送ICMP请求到目标IP
send_icmp_packet('8.8.8.8')  # 假设你要ping的是Google DNS

# 在另一个线程中，开始捕获ICMP响应
sniff(filter='icmp', prn=lambda x: x.show(), count=3)
