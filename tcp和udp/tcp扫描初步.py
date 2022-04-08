from scapy.all import *
import time
from random import randint

def main():
    ip = '192.168.64.129'
    dport = 80
    packet = IP(dst=ip)/TCP(flags="A",dport=dport)

    resp = sr1(packet,timeout=1.0,verbose=0)

    if resp:
        #RST
        if int(resp[TCP].flags) == 4:
            time.sleep(0.5)
            print(ip + 'is up')
        else:
            print((ip + 'is down'))
    else:
        print((ip + 'is down'))

if __name__ == '__main__':
    main()