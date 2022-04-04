from scapy.all import  *
def main():
    ip = "192.168.64.129"
    port = 80
    packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
    resp  = sr1(packet,timeout=20)
    if (str(type(resp))=="<type 'NoneType'>"):
        print('port %s is closed'%(port))
    elif(resp.haslayer(TCP)):
        if (resp.getlayer(TCP).flags==0x12):
            send_rst = sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags='AR'),timeout=20)
            print('port %s is down'%(port))
        elif (resp.getlayer(TCP).flags==0x14):
            print("port %s is down"%port)

if __name__ == '__main__':
    main()