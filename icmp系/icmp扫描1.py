from whois import whois
import socket
from scapy.all import *
from random import randint

def main():
    # ������Ϣ�ռ�
    # data = whois('www.baidu.com')
    # print(data)

    # ����ʹ��ping���ֱ����python��ѯ������Ϣ
    # baidu_ip = socket.gethostbyname('www.baidu.com')
    # print(baidu_ip)

    # ɨ��������
    ip_id = randint(1,65535)
    icmp_id = randint(1,65535)
    icmp_seq = randint(1,65535)
    packet = IP(dst="192.168.64.1",ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'rootkit'
    '''
    sr() �����������������ݰ��ͽ���Ӧ��.�ú�������һ�����ݰ�����Ӧ��,������Ӧ������ݰ�
    sr1() ������һ�ֱ��壬��������һ��Ӧ�����ݰ�,���͵����ݰ������ǵ�3�㱨�ģ�IP��ARP�ȣ�
    srp() ����ʹ�õ�2�㱨�ģ���̫����802.3�ȣ�
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