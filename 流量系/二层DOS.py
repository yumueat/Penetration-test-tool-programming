from scapy.all import  *
import time
# ���㹥��
# MAC��ַ���鹥��
def main():
    while 1:
        packet = Ether(src=RandMAC(),dst=RandMAC())/IP(src=RandIP(),dst=RandIP())/ICMP()
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    # ��������д��ֱ�Ӳ�����Ether
    '''
        while 1:
        packet = IP(src=RandIP(), dst=RandIP()) / ICMP()
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    '''
    # ��ȻҲ����ֻ����Ether
    '''
    while 1:
        packet = Ether(src=RandMAC(),dst=RandMAC())
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    '''
if __name__ == '__main__':
    main()