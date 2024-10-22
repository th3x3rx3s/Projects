import os

def file_organizer(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        return print("A megadott elérési útvonal nem létezik.")
    directory=os.getcwd()

    for x in os.listdir():
        if x[0]=="." or x==os.path.basename(__file__) or not os.path.isfile(x):
            continue
        name,ext=os.path.splitext(x)
        ext=ext.replace(ext[0],"")
        ext_dir=os.path.join(directory,ext)
        if not os.path.exists(ext_dir):
            try:
                os.mkdir(ext_dir)
            except PermissionError:
                print("Nincs jogom a mappa létrehozásához, átugrás...")
                continue
        
        try:
            os.rename(os.path.join(directory,x), os.path.join(ext_dir,x))
        except FileExistsError:
            n=2
            while os.path.exists(os.path.join(ext_dir,x)):
                x=f"{name}+_{n}.{ext}"
                n+=1
            os.rename(os.path.join(directory,x), os.path.join(ext_dir,x))
        

pathway=input("Mi a mappa elérési útvonala?[jelenlegi mappa] ").strip() or os.getcwd()
file_organizer(pathway)