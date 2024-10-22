import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import bs4
from googlesearch import search 

def validate():
    phone = input("Adja meg a telefonszámot: ")
    phone_parse = phonenumbers.parse(phone)
    phone_possible = phonenumbers.is_possible_number(phone_parse)
    phone_valid = phonenumbers.is_valid_number(phone_parse)
    if phone_possible == True:
        if phone_valid == True:
            print("A telefonszám valós!")
        elif phone_valid == False:
            print("A telefonszám nem valós!")
    else:
        print("Hamis formátum!")

def basic_information():
    phone = input("Adja meg a telefonszámot: ")
    phone_number = phonenumbers.parse(phone)
    phone_carrier = carrier.name_for_number(phone_number, 'hu')
    phone_region = geocoder.description_for_number(phone_number, 'hu')
    phone_timezone = timezone.time_zones_for_number(phone_number)
    
    #06-al kezdés
    query_a = phone[3::].split()
    query_b = "".join(query_a)
    query_c = "06" + query_b

    query2 = f"intext:{phone}"
    query4 = f"intext:{query_c}"
    print(f"Szolgáltató: {phone_carrier}")
    print("-------------")
    print(f"Területi info: {phone_region}")
    print("-------------")
    print(f"Időzona: {phone_timezone}")
    print("-------------")
    print("INFORMÁCIÓ KERESÉS A TELEFONSZÁMRÓL ONLINE")
    for b in search(query2, num_results=50):
        print(b)
    if phone != query_c:
        for d in search(query4, num_results=50):
            print(d)
print("--- BasicPhone ---")
while True:
    print("\n1.) Valós-e a telefonszám\n2.) Alap telefonszám információk")
    choice = int(input("\nBP > "))
    if choice == 1:
        validate()
    elif choice == 2:
        basic_information()
    else:
        print("Csak 1-et vagy 2-őt írhatsz be!")