import scapy.all as scapy
import optparse
print ("\033[31;1mthis tool was coded by Abo Ahmad LB")

def get():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="nothing")
    (xy, yx) = parser.parse_args()
    return xy
def scan(ip):
    a = scapy.ARP(pdst=ip)
    b = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    c = b/a
    x_list = scapy.srp(c, timeout=1, verbose=False)[0]

    g = []
    for element in x_list:
        f = {"ip": element[1].psrc, "mac":element[1].hwsrc}
        g.append(f)
    return g
def printf(results):
    print("IP\t\t\tMAC\n====================")
    for m in results:
        print(m["ip"] + "\t\t" + m["mac"])

xy = get()
p = scan("192.168.1/24")
printf(p)
