digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convert_to_decimal(number, base):
    n=len(str(number))-1
    decimal=0
    for x in str(number):
        decimal+=digits.index(x)*(base**n)
        n=n-1
    return decimal

def is_base_correct(base):
    if 2<=base<=36:
        return True
    else:
        return False

def is_number_correct(num,base):
    for x in str(num):
        if digits.index(x)>=base:
            return False
    return True
    
def base_converter(num,ogbase,tgbase):
    #megvizsgálja, hogy a bevitt számrendszerek 2 és 36 között vannak-e
    if is_base_correct(ogbase)==False or is_base_correct(tgbase)==False:
        return "Hiba: Az eredeti és cél számrendszerek csak 2 és 36 között lehetnek."
    
    #megvizsgálja, hogy a bevitt szám lehetséges-e az adott számrendszerben
    if is_number_correct(num,ogbase)==False:
        return f"Hiba: {ogbase} alapú számrendszerben nem szerepelhet ilyen szám[0-{ogbase-1}]."
    
    if int(ogbase)<=10 and int(num)<0:
        return "Hiba: A szám nem lehet negatív."
    
    result=""
    if ogbase!=10 and tgbase!=10:
        #decimális számrendszerbe váltás
        dec=convert_to_decimal(num,ogbase)
        #decimálisból cél számrendszerbe váltás
        while dec>0:
            result+=digits[dec%tgbase]
            dec=dec//tgbase
        return result[::-1]
    elif ogbase==10:
        #decimálisból cél számrendszerbe váltás
        while num>0:
            result+=digits[num%tgbase]
            num=num//tgbase
        return result[::-1]
    elif tgbase==10:
        #eredeti számrendszerből decimálisba váltás
        dec=convert_to_decimal(num,ogbase)
        return dec
    elif ogbase==tgbase:
        return num
print(base_converter("AC4571B",15,16))