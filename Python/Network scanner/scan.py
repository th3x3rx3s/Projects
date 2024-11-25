from scapy.all import Ether, ARP, srp, sr, IP, TCP
import sys

class modok:
    def __init__(self, mode):
        self.mode = mode
    
    def scan(ip_range):
        devices = {}
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp = ARP(pdst=ip_range.strip())
        packet = ether / arp
        rec, _ = srp(packet, timeout=10, verbose=False) 
        for x in range(len(rec)):
            devices[rec[x][1].src] = rec[x][1].psrc # <== rec: lista amiben soronként értékpárok vannak(tuple) : (keres, valasz)
        print("\nARP Szkennelés Eredmények (Aktív Eszközök):")
        for mac, ip in devices.items():
            print(f"\t{mac} : {ip}")

    def port_scan(target, all, showall):
        ports = {}
        ports_to_scan=range(1,65535)
        common_ports=[20,21,22,23,25,53,80,110,119,123,143,443,465,563,989,990,993,995,3306]

        try:
            ip = IP(dst=target)
            if all:
                tcp = TCP(dport=ports_to_scan, flags="S")
            else:
                tcp = TCP(dport=common_ports, flags="S")
            packet = ip / tcp
            ans, _ = sr(packet, verbose=False, timeout=2)
        except Exception as e:
            exit(f"Nem sikerült a címet érvényesíteni {target} : {e}")

        for _, answered in ans:
            if all:
                if (answered[TCP].sport in ports_to_scan) and (answered[TCP].flags == 0x12):
                    ports[str(answered[TCP].sport)] = "nyitott"
                else:
                    if showall:
                        ports[str(answered[TCP].sport)] = "zárt"
                    else:
                        continue

            else:
                if (answered[TCP].sport in common_ports) and (answered[TCP].flags == 0x12):
                    ports[str(answered[TCP].sport)] = "nyitott"
                else:
                    if showall:
                        ports[str(answered[TCP].sport)] = "zárt"
                    else:
                        continue

        vanenyitott=False
        for port, state in ports.items():
            if state == "nyitott":
                vanenyitott=True
        if vanenyitott:
            print(f"\nNyitott portok: {target}\n" if len(target.split("."))>3 else f"\nNyitott portok: {target}({ans[0][1].src})\n")
            for port, state in ports.items():
                print(f"\t{port}\t{state}")
        else:
            print("Nincs nyitott port.")


lehetseges_modok={
    "-h": "Segítség",
    "-s": "Aktív eszközök",
    "-p": "Gyakori portok",
    "-pa": "Összes port",
    "--show-all": "Zárt portok is"
}
exit_text="""
    Módok:
        -h: Kiírja ezt az segítő szöveget.
        -s: Kiírja az aktív eszközöket a hálózaton(csak LAN hálózat! nem párosítható -p -vel!).
        -p: Kiírja az aktív portokat egy adott IP címen(nem párosítható -s -el!).
        -a: Szkennel minden lehetséges portot(nem párosítható -s -el!).
        --show-all: Kiírja a zárt és nyitott portokat is(nem párosítható -s -el!).
    Használat: scan.py <mode> <ip_range>
    Például: scan.py -s 192.168.1.0/24"""


if len(sys.argv)<=2:
    exit(exit_text)
for x in sys.argv[1:-1]:
    if x not in lehetseges_modok.keys():
        exit(exit_text)


for x in sys.argv[1:]:
    if ["-s"] not in sys.argv:
        if x == "-p":
            if "--show-all" in sys.argv:
                modok.port_scan(target=sys.argv[-1], all=False, showall=True)
            else:
                modok.port_scan(target=sys.argv[-1], all=False, showall=False)
        elif x == "-pa":
            if "--show-all" in sys.argv:
                modok.port_scan(target=sys.argv[-1], all=True, showall=True)
            else:
                modok.port_scan(target=sys.argv[-1], all=True, showall=False)
    if ["-p", "-pa", "--show-all"] not in sys.argv:
        if x == "-s":
            modok.scan(ip_range=sys.argv[-1])