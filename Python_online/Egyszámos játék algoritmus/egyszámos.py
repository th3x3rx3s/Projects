import os
lista=[]
while len(lista)<=15:
    user_input=int(input("Kérek egy számot! "))
    if user_input>10 or user_input<-10:
        print("Csak -10 és 10 között lehet!")
    else:
        lista.append(user_input)
halmaz=set()
for x in lista:
    halmaz.add(x)
duplicate=[]
singles=[]
for x in halmaz:
    db=0
    for y in lista:
        if x==y:
            db+=1
    if db>1:
        duplicate.append(x)
    else:
        singles.append(x)
print(duplicate, singles)
if len(singles)==0:
    print("Nincs nyertes, nincs olyan szám ami csak egyszer fordult volna elő.")
else:
    print(f"Nyertes szám: {min(singles)} gép neve: {os.environ['COMPUTERNAME']}")