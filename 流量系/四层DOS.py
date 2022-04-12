from scapy.all import  *
import time
from random import randint
def main():
    while 1:
        pdst = "%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
        psrc = "%i.%i.%i.%i" % (randint(1, 254), randint(1, 254), randint(1, 254), randint(1, 254))
        # print(pdst)
        packet = IP(dst=pdst,src=psrc)/TCP(dport=80,flags="S")
        send(packet)
        time.sleep(0.5)
        print(packet.summary())
if __name__ == '__main__':
    main()