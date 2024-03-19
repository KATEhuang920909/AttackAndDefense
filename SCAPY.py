# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/6 15:39
@Author: huangkai2
@File:SCAPY.py
@Software: PyCharm
"""

from scapy.all import *
# 添加过滤条件，只获取指定进程的数据包
pid = 1234  # 指定进程的PID
filter_str = 'host 120.26.224.206'
# 定义处理回调函数，打印出抓取到的数据包的信息
def handle_pkt(pkt):
    pkt.show()
# 启动抓包
print("start")
sniff(filter=filter_str,prn=lambda x:x.summary(),count=2)