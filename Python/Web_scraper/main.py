import requests
from bs4 import BeautifulSoup
import sys
import time
import re

if len(sys.argv)<2:
    exit(f"Használat: {sys.argv[0]} http(s)://host.com")



emails=[]
files=[]
file_exts=(".jpg",".png",".pdf",".mp4",".mp3",".webp",".doc",".docx",".xlsx")
subsites=set()
already_visited=set()
header={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
}

def is_valid_email(email): 
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return re.match(pattern, email) is not None

def link_follow(start):
    stack=[start]
    while stack:
        link=stack.pop()
        for z in range(3):
            try:
                r=requests.get(link, headers=header, timeout=10)
                break
            except requests.exceptions.ConnectionError:
                time.sleep(5)

        if r.status_code==200:
            bs4=BeautifulSoup(r.content, "html5lib")
            for x in bs4.find_all('a'):
                href=x.get('href')
                
                if href:
                    if href.startswith("/"):
                        href=sys.argv[1]+href
                    elif href.startswith("mailto:"):
                        if href[7:] not in emails:
                            emails.append(href[7:])
                        continue
                    elif is_valid_email(href):
                        if href not in emails:
                            emails.append(href)
                        continue         
                    if href.endswith(file_exts):
                            if href.startswith("https") or href.startswith("http"):
                                if href not in files:
                                    files.append(href)
                                continue
                            elif href.startswith("./"):
                                current_file=sys.argv[1]+href[1:]
                                if current_file not in files:
                                    files.append(current_file)
                                continue
                            elif href.startswith("/"):
                                current_file=sys.argv[1]+href
                                if current_file not in files:
                                    files.append(current_file)
                                continue
                            else:
                                current_file=sys.argv[1]+"/"+href
                                if current_file not in files:
                                    files.append(current_file)
                                continue

                    if href.split(".")[-1].startswith("html"):
                        if not href.startswith(("https","http")):
                            if not href.startswith("/"):
                                href=sys.argv[1]+"/"+href
                            else:
                                href=sys.argv[1]+href
                    if href.startswith(("#","javascript")):
                        continue
                    
                if not href or href in already_visited:
                    continue
                
                
                parse_href = href.split("/")[2].split(".")[-2] 
                parse = sys.argv[1].split("/")[2].split(".")[-2] 
                if parse_href != parse: 
                    continue

                if not href.startswith(sys.argv[1]):
                    host_href=href.split("/")
                    subsites.add("/".join(host_href[0:3]))
                
                already_visited.add(href)
                stack.append(href)


try:
    link_follow(sys.argv[1])
    
    site_name=sys.argv[1].split("/")[2]
    if len(site_name.split("."))==2:
        file_name=site_name.split(".")[0]
    elif len(site_name.split("."))>=3:
        file_name=site_name.split(".")[1]

    if len(already_visited)==0:
        already_visited.add("Nincs")
    if len(subsites)==0:
        subsites.add("Nincs")
    if len(emails)==0:
        emails.append("Nincs")
    if len(files)==0:
        files.append("Nincs")
    
    already_visited = list(already_visited)
    subsites = list(subsites)
    
    max_len = max(len(already_visited),len(emails),len(subsites),len(files))

    already_visited += " " * (max_len - len(already_visited))
    subsites += " " * (max_len - len(subsites))
    emails += " " * (max_len - len(emails))
    files += " " * (max_len - len(files))
    try:
        with open(f"{file_name}.csv","w") as f:
            f.write("Aloldalak;Suboldalak;Email-ek;Fájlok\n")
            
            for x in range(max_len):
                site = already_visited[x]
                subsite = subsites[x]
                email = emails[x]
                file = files[x]
                f.write(f"{site};{subsite};{email};{file}\n")
    except PermissionError:
        print("Nincs jogosultságom a fájl írásához. Új fájl létrehozása...")
        n=0
        import os
        while True:
            file_name=file_name+str(n)
            if os.path.exists(os.path.join(os.getcwd(),f"{file_name}.csv")):
                n+=1
            else:
                break
        with open(f"{file_name}.csv","w") as f:
            f.write("Aloldalak;Suboldalak;Email-ek;Fájlok\n")
            
            for x in range(max_len):
                site = already_visited[x]
                subsite = subsites[x]
                email = emails[x]
                file = files[x]
                f.write(f"{site};{subsite};{email};{file}\n")
    except UnicodeEncodeError as e:
        print(f"Hiba történt : {e}")
        print(already_visited, subsites, emails, files)
except IndexError as e:
    exit(f"Hiba lépett fel. Az oldal lehet, hogy védve van.({e})")