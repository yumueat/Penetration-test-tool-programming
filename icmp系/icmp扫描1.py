from whois import whois
import socket
from scapy.all import *
from random import randint

def main():
    # 进行信息收集
    # data = whois('www.baidu.com')
    # print(data)

    # 不用使用ping命令，直接用python查询主机信息
    # baidu_ip = socket.gethostbyname('www.baidu.com')
    # print(baidu_ip)

    # 扫描器雏形
    ip_id = randint(1,65535)
    icmp_id = randint(1,65535)
    icmp_seq = randint(1,65535)
    packet = IP(dst="192.168.64.1",ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'rootkit'
    '''
    sr() 函数是用来发送数据包和接受应答.该函数返回一对数据包及其应答,还有无应答的数据包
    sr1() 函数是一种变体，用来返回一个应答数据包,发送的数据包必须是第3层报文（IP，ARP等）
    srp() 则是使用第2层报文（以太网，802.3等）
    '''
    result = sr1(packet,timeout=1,verbose=False)
    if result:
        for rcv in result:
            scan_ip = rcv[IP].src
            print(scan_ip+'is alive')
    else:
        print('is down ')
if __name__ == '__main__':
    main()