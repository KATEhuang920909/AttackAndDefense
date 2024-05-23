# -*- coding =  utf-8 -*-
"""
@Time : 2024/3/6 14:43
@Author: huangkai2
@File:NMAP.py
@Software: PyCharm
"""
import nmap
import prettytable as pt2
class nmapApply:
   target_host = ""        #主机ip地址
   target_ports = ""       #扫描端口号
   arguments = "-p"        #扫描参数
   up_hosts = []
   nmps = nmap.PortScanner()

   def useage(self):
       print("nmap IP:", "无任何参数扫描，相当于sS 参数扫描")
       print("nmap -vv IP:", "冗余扫描，将侦测过程原原本本的打印输出出来")
       print("nmap -p22 IP:", "指定端口号扫描,p和端口号可以不加空格")
       print("nmap -O IP:", "操作系统侦测扫描")
       print("nmap -A IP:", "操作系统侦测扫描,使用 A 参数，可以得到更多的信息")
       print("nmap -sn IP:", "只进行主机发现扫描,最常用的扫描方式，使用ping 扫描来侦测存活的主机，而不进行端口扫描")
       print("nmap -Pn IP:", "跳过主机发现扫描,假设所有的目标 IP 均为存活，以这种方式一个一个主机的进行端口扫描。(逃脱策略)")
       print("nmap -sV IP:", "扫描和版本号侦测扫描,侦测开放的端口来判断开放的服务，并试图检测它的版本")
       print("nmap --script=vuln  IP:", "常见漏洞扫描")
       print("nmap -sU IP:", "UDP 扫描,用于NTP（123端口）、SNMP（161端口）之类的UDP服务扫描")
       print("nmap -D IP1,IP2 IP3:", "绕过防火墙利用掩体扫描,用掩体IP混入其中")
       print("nmap -P0 IP1,IP2 IP3:", "禁用 ping扫描")
       print("nmap -sI 僵尸IP地址[:开放的僵尸端口] IP:", "空闲扫描，sI 根本不使用你自己的 IP 地址，而是使用空闲的网络资源用于提高隐蔽性")
       print("nmap -e 网卡 IP:", "指定网卡扫描")
       print("nmap --host-timeout 时间 IP:", "限制每个 IP 地址的扫描时间（单位为秒），当要扫描大量的主机 IP 时这很有用")
       print("nmap -S 源IP IP:", "指定源IP扫描，冒充的 IP 地址(可以是下线状态的主机地址)进行扫描以增强隐蔽性")
       print("nmap -g 53 IP:", "指定源主机端口扫描，g/source-port 参数手动设定用来扫描的端口")
       print("nmap -f IP:", "数据包分片技术扫描，用于逃脱防火墙或闯入检测系统的检测")
       print("nmap --mtu mtu单元大小  IP:", "数据包分片技术扫描，mtu 的值必须是 8 的倍数（如 8、16、24、32 等）")
       print("nmap --data-length 垃圾数据长度 IP:", "添加垃圾数据扫描，在发送的数据包末尾添加随机的垃圾数据，以达到混淆视听的作效果")
       print("nmap --randomize-hosts IP:","随机选择扫描对象，如果你要扫描大量的，比如成百上千的主机 IP，这很有效。它会打乱扫描顺序，以规避检测系统的检测")
       print("nmap --spoof-mac 伪造MAC IP:","伪装 MAC 地址扫描，通过指定供应商的名字来伪装 MAC 地址。可选的名字有 Dell、Apple、3Com。"
        "当然也可以手动指定 MAC 地址的值。或者为了简单起见，可以在上面 “伪造IP” 的地方填写数字 0，这将生成一个随机的 MAC 地址")
       print("nmap --badsum IP:", "伪造检验值扫描，使用伪造的 TCP / UDP / SCTP 校验和发送数据")
       print("nmap -T0 IP:", "扫描速度，T后面跟的数字代表扫描速度，数字越大则速度越快。"
                             "0～5分别表示：妄想症、鬼鬼祟祟、彬彬有礼、正常、好斗、精神病")
   #判断主机是否存活
   def isalive(self):
       self.nmps.scan(hosts=self.target_host, arguments='-n -sP -PE')
       self.up_hosts = self.nmps.all_hosts()  # 获取存活主机列表
       print("存活主机:",self.up_hosts)
   def oneIPscan(self):
       L = []
       if "/" in self.target_host:
           L = self.nmps.all_hosts()
       else:
           L.append(self.target_host)
       for ip in L:
           self.nmps.scan(hosts=ip)#,arguments=self.arguments)  # 扫描主机 127.0.0.1 端口号 22-443
           print(self.nmps.command_line())  # 获取用于扫描的命令行：nmap -oX - -p 22-443 127.0.0.1
           tableA = pt2.PrettyTable()
           # print('values:%s' % self.nmps[ip].values())
           col = 3
           if "-sV" in self.arguments:
               col = 4
               tableA.field_names = ["port", "state", "name", "product"]
           else:
               tableA.field_names = ["port", "state", "name"]
           for i in self.nmps[ip].values():
               if type(i) == dict:
                   for j in i:
                       li = [j, i[j]]
                       if type(li[1]) == dict:
                           ll = []
                           str1 = str(j)
                           if j in self.nmps[ip].all_tcp():
                               str1 += "/tcp"
                           elif j in self.nmps[ip].all_udp():
                               str1 += "/udp"
                           elif j in self.nmps[ip].all_ip():
                               str1 += "/ip"
                           elif j in self.nmps[ip].all_sctp():
                               str1 += "/sctp"
                           ll.append(str1)
                           ll.append(li[1]['state'])
                           ll.append(li[1]['name'])
                           if "-sV" in self.arguments:
                               ll.append(li[1]['product'])
                           li = ll
                       while True:
                           if len(li) < col:
                               li.append(" ")
                           else:
                               break
                       tableA.add_row(li)
           print(tableA)

           tableB = pt2.PrettyTable()
           c = 0
           for i in self.nmps[ip].values():
               if type(i) != dict:
                   for J in i:
                       for k in J:
                           if k != 'osclass' and k != 'id' and k != 'output':
                               li = [k, J[k]]
                               tableB.add_row(li)
                           elif k == 'id':
                               li = [J[k], J['output']]        #漏洞检测输出
                               tableB.add_row(li)
                               c += 1
           if c > 0:
               tableB.field_names = ["id", "output"]
               print(tableB)
           tableC = pt2.PrettyTable()
           for i in self.nmps[ip].values():
               if type(i) != dict and len(i) > 0:
                   if 'osclass' in i[0].keys():
                       tableC.field_names = ["os", "vendor", "osfamily", "accuracy", "cpe"]
                       for j in i[0]:
                           li = [j, i[0][j]]
                           if len(i[0][j]) > 0 and type(i[0][j][0]) == dict:
                               ll = []
                               ll.append(j)
                               ll.append(i[0][j][0]["vendor"])
                               ll.append(i[0][j][0]["osfamily"])
                               ll.append(i[0][j][0]["accuracy"])
                               ll.append(i[0][j][0]["cpe"])
                               li = ll
                           if len(li) > 2:
                               tableC.add_row(li)  # 系统检测输出
                               print(tableC)
           print("在线状态:", self.nmps[ip].state())  # 获取主机 127.0.0.1 的状态 (up|down|unknown|skipped)
           print("22端口检测:", self.nmps[ip].has_tcp(22))  # 是否含有主机 127.0.0.1 的 22 端口的信息
if __name__ == '__main__':
   nma = nmapApply()
   # 获取需要扫描的主机IP地址和端口
   # nma.target_host = input("输入help可以查看帮助:")
   if nma.target_host == "help" or nma.target_host == "HELP":
       nma.useage()
   nma.target_host = "192.168.12.137"#input("请输入需要扫描的主机ip地址:")

   # nma.target_ports = "8888"#input("请输入需要扫描的主机 port:")
   #获取存活主机列表
   nma.isalive()
   #单IP扫描
   if len(nma.up_hosts) > 0:
       nma.oneIPscan()
