# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/6 15:39
@Author: huangkai2
@File:SCAPY.py
@Software: PyCharm
"""
from scapy.all import *
from scapy.layers.inet import TCP, IP, ICMP, Ether


def handle_packet(packet):
    # 检查是否为TCP SYN包
    if packet.haslayer(TCP) and packet[TCP].flags == 0x02:  # 0x02代表TCP的SYN标志
        # 创建一个TCP RST包来响应这个SYN包
        tcp_packet = TCP(sport=packet[TCP].dport, dport=packet[TCP].sport, flags="R", seq=1, ack=1)

        rst_packet = Ether() / IP(dst=packet[IP].src, src=packet[IP].dst) / tcp_packet
        sendp(rst_packet)  # 发


#
def target_2(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == 0x02:  # 0x02代表TCP的SYN标志
        ip_packet =  IP(dst=packet[IP].src, src=packet[IP].dst)
        tcp_packet = TCP(sport=packet[TCP].dport, dport=packet[TCP].sport, flags="F", seq=1, ack=1)
        packet = ip_packet / tcp_packet
        send(packet)
        print(f"Sent packet ")

sniff(filter="tcp[tcpflags] == tcp-syn and ip dst 192.168.12.234 and ip src 192.168.12.29",
      prn=target_2,
      store=False)
