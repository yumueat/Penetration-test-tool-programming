from scapy.all import *

def main():
    ip = '192.168.64.129'
    ans,uans = sr(IP(dst=ip)/UDP(dport=80))
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is up"))

if __name__ == '__main__':
    main()