from scapy.all import Ether, ARP, srp, sr, IP, TCP
import sys

modok=["s","p","a"]
common_ports=[21,22,23,25,53,80,110,443,3306]
exit_text="""
    Módok:
        -s: Kiírja az aktív eszközöket a hálózaton(csak LAN hálózat! nem párosítható -p -vel!).
        -p: Kiírja az aktív portokat egy adott IP címen(nem párosítható -s -el!).
        -a: Kiír minden információt(nem párosítható -s -el!).
    Használat: scan.py <mode> <ip_range>
    Például: scan.py scan 192.168.1.0/24"""



if len(sys.argv)<=2:
    exit(exit_text)
for x in sys.argv[1]:
    if x not in modok and x!="-":
        exit(exit_text)

devices = {}

def scan(ip_range):

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ip_range)
    packet = ether / arp
    rec, _ = srp(packet, timeout=10, verbose=False) 
    for x in range(len(rec)):
        devices[rec[x][1].src] = rec[x][1].psrc # <== rec: lista amiben soronként értékpárok vannak(tuple) : (keres, valasz)
    print("\nARP Szkennelés Eredmények (Aktív Eszközök):")
    for mac, ip in devices.items():
        print(f"\t{mac} : {ip}")

ports={}

def port_scan(ip_range, all):
    try:
        ip = IP(dst=ip_range)
        tcp = TCP(dport=common_ports,flags="S")
        packet = ip / tcp
        ans, unans = sr(packet, verbose=False, timeout=2)
    except Exception as e:
        exit(f"Nem sikerült a címet érvényesíteni {ip_range} : {e}")
    
    ans_len=len(ans)
    unans_len=len(unans)
    n=0
    for x in range(len(common_ports)):
        port=common_ports[x]
        if x+1<=ans_len:
            ports[str(ans[x][1].sport)] = "nyitott"
        elif x+1>ans_len and unans_len!=0:
            ports[str(unans[n][1].dport)] = "zárt"
            n+=1

    if len(ports)!=0:
        print(f"\nNyitott portok: {ip_range}\n" if len(ip_range.split("."))>3 else f"\nNyitott portok: {ip_range}({ans[0][1].src})\n")
        for port, state in ports.items():
            if all:
                print(f"\t{port}\t{state}")
            elif all == False:
                if state == "nyitott":
                    print(f"\t{port}\t{state}")
        
    else:
        print("Nincs nyitott port.")
        
if ("p" in sys.argv[1]) and ("s" not in sys.argv[1]):
    if ("a" in sys.argv[1]):
        port_scan(sys.argv[2], all=True)
    else:
        port_scan(sys.argv[2], all=False)
elif ("s" in sys.argv[1]) and ("p" not in sys.argv[1]):
    scan(sys.argv[2])
else:
    exit("p és s opciót egyszerre nem választhatja!")