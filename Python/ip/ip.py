import ipinfo
import requests as r
import socket
print("Ip info grabber tool")
print("----------------------")
choice = input("Mit szeretnél?\n1.) Ip info\n2.) Host to Ip\n3.) Ip to hostname\n4.) Publikus ip címem\n")

if choice == "1":
    ip = input("Add meg az ip címet! ")
    ip_data = r.get("https://ipinfo.io/" + ip + "?token=072cf790f1df98")
    data = ip_data.json()

    if ip_data != None:
        print("Ip cím: {ip},\nVáros: {city},\nMegye: {region},\nOrszág: {country},\nKoordináta: {loc},\nSzolgáltató: {org},\nIdőzóna: {timezone}".format(
            ip = data['ip'],
            city = data['city'],
            region = data['region'],
            country = data['country'],
            loc = data['loc'],
            org = data['org'],
            timezone = data['timezone']
        ))
elif choice == "2":
    hostname = input("Írd be a hostname-et! ")
    ip_add = socket.gethostbyname(hostname)
    print(ip_add)
elif choice == "3":
    ip = input("Add meg az ip címet! ")
    response = socket.gethostbyaddr(ip)
    print("Hostname: {}".format(response[0]))
elif choice == "4":
    ip_address = r.get("https://api.ipify.org/").text
    print("Az ip címed: {}".format(ip_address))