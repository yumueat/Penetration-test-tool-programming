from scapy.all import *

def main():
    ip = '192.168.64.129'
    port = 3306
    s = socket.socket()
    s.connect((ip,port))
    s.send('haha'.encode())
    banner = s.recv(1024)
    s.close()
    print("banner is %s"%(banner))

if __name__ == '__main__':
    main()