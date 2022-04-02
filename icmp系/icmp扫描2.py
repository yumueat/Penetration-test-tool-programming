from scapy.all import *

def main():
    ans,uans  = sr(IP(dst="192.168.64.1")/ICMP())

    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is alive now"))
if __name__ == '__main__':
    main()