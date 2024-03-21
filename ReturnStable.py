# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/4 9:26
@Author: huangkai2
@File:config.py
@Software: PyCharm
"""
from scapy.all import IP, bind_layers, Raw


class FixedIP(IP):
    name = "Fixed IP Packet"
    fields_desc = [
        IP.src,
        IP.dst,
        Raw
    ]

    def answer(self, query):
        # 返回一个固定值的IP数据包
        return FixedIP(src="1.2.3.4", dst="5.6.7.8")


# 绑定FixedIP到IP层，以便能够处理和返回固定值的IP包
bind_layers(IP, FixedIP, frag=0, proto=255)

# 使用Scapy的`sr1`函数发送一个IP数据包并接收返回的响应
response = sr1(IP(dst="1.2.3.4"))

print(response.show())