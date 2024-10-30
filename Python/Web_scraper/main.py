import requests
from bs4 import BeautifulSoup
import sys

emails=[]
sites=[]
already_visited=set()
header={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
}

def link_follow(start):
    stack=[start]
    while stack:
        link=stack.pop()
        for z in range(3):
            try:
                r=requests.get(link, headers=header, timeout=10)
                break
            except requests.exceptions.ConnectionError:
                continue

        if r.status_code==200:
            bs4=BeautifulSoup(r.content, "html5lib")
            for x in bs4.find_all('a'):
                href=x.get('href')
                if href:
                    sites.append(href)
                    if href.startswith("/"):
                        href=f"{sys.argv[1]+href}"
                    elif href.startswith("mailto:"):
                        if href[7:] not in emails:
                            emails.append(href[7:])
                            continue

                if not href or not href.startswith(sys.argv[1]) or href in already_visited:
                    continue

                already_visited.add(href)
                stack.append(href)

try:
    link_follow(sys.argv[1])
    print(already_visited)
    site_name=sys.argv[1].split("/")[2]

    if len(site_name.split("."))==2:
        file_name=site_name.split(".")[0]
    elif len(site_name.split("."))>=3:
        file_name=site_name.split(".")[1]

    with open(f"{file_name}.csv","w") as f:
        already_visited = list(already_visited)
        max_len = max(len(already_visited),len(emails))
        f.write("Aloldalak;Email-ek\n")
        for x in range(max_len):
            site = already_visited[x] if x < len(already_visited) else " "
            email = emails[x] if x < len(emails) else " "
            f.write(f"{site};{email}\n")

except IndexError:
    exit(f"Használat: {sys.argv[0]} http(s)://host.com")
