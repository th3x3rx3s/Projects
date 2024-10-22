from datetime import datetime as dt
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
#megnézi, hogy az adott nap milyen napra esett
def what_day_it_is(datum):
    return days[(dt.isocalendar(dt.strptime(datum,"%Y %m %d")).weekday)-1]
#megnézi, hogy az adott év szökőév-e
def szokoev(year):
    if year%4==0: return True
    else: return False

def Naptar():
    date=dt.now()
    months_howmanydays=[]
    #megnézi, hogy hány napból áll havonta az év
    if szokoev(date.year):
        months_howmanydays=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months_howmanydays=[31,28,31,30,31,30,31,31,30,31,30,31]

    print(f"\t\t\t{months[date.month-1]}\t\t\t")

    for x in days:
        if x==days[-1]: print(f"{x}", end="")
        else: print(f"{x}\t", end="")
    print()

    #"\t"*(dt.isocalendar(dt.strptime(f"{date.year} {date.month} {y+1}", "%Y %m %d")).weekday-1) -> annyi tabulátort tegyen elé az első futásnál amilyen nappal kezd az a hónap(pl.: péntek -> 4 tabulátor)

    for y in range(months_howmanydays[date.month-1]):
        if y==0 or what_day_it_is(f"{date.year} {date.month} {y+1}")=="Mon":
            print("\t"*(dt.isocalendar(dt.strptime(f"{date.year} {date.month} {y+1}", "%Y %m %d")).weekday-1),y+1,end="")
        elif what_day_it_is(f"{date.year} {date.month} {y+1}")=="Sun":
            print("\t",y+1,end="\n")
        else:
            print("\t",y+1,end="")
    