import random as r
abc="aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz0123456789(*@&#<>^)!.,:-_?/%=+' "
reverse_abc=sorted(abc, reverse=True)
reverse_abc="".join(reverse_abc)
key="<kulcsod>"

while True:
    print("\t0: kilépés\n\t1: encode\n\t2: decode")
    command=input("Mit szeretnél tenni?")
    if command=="0": break
    elif command=="1":
        text=input("Add meg a szöveget xd ")
        encoded=""
        for x in range(len(text)):
            if text[x]!=" ":
                for z in range(len(abc)):
                    if abc[z]==text[x]:
                        encoded+=reverse_abc[z]
            else:
                encoded+=" "
        print(encoded)
    elif command=="2":
        encoded=input("Add meg az encoded szöveget xd ")
        text=""
        ask_for_key=input("Mi a kulcs? ")
        if ask_for_key==key:
            for x in range(len(encoded)):
               for y in range(len(reverse_abc)):
                   if reverse_abc[y]==encoded[x]:
                       text+=abc[y]
            print(f"Dekódolt szöveg: {text}")
        else:
            print("Hibás kulcs.")
    else:
        print("Nincs ilyen lehetőség.")
