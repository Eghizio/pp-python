from random import randint

def sprawdz_zakres(ile_liczb, min_max):
    min, max = min_max
    if min > max:
        raise Exception("Zakres dolny nie moze byc wiekszy od zakresu gornego.")
    if ile_liczb > len(range(min, max)):
        raise Exception("Ilosc liczb nie moze byc wieksza od calego dostepnego zakresu.")

def wytypuj_liczby(ile_liczb, min_max = (1, 10)):
    min, max = min_max
    wytypowane__liczby = set()
    while len(wytypowane__liczby) < ile_liczb:
        try:
            typ = int(input(f"Wytypuj liczbe od {min} do {max}: "))
            if typ < min or typ > max:
                raise Exception("Liczba poza zakresem.")
            if typ in wytypowane__liczby:
                raise Exception("Liczba juz wybrana.")
            wytypowane__liczby.add(typ)
        except:
            print(f"Prosze podaj liczbe z zakresu od {min} do {max}.")
    return wytypowane__liczby

def wylosuj_liczby(ile_liczb, min_max = (1, 10)):
    min, max = min_max
    wylosowane_liczby = set()
    while len(wylosowane_liczby) < ile_liczb:
        wylosowana = randint(min, max)
        if wylosowana in wylosowane_liczby: continue
        wylosowane_liczby.add(wylosowana)
    return wylosowane_liczby

def trafione(wylosowane, typy): return wylosowane & typy

if __name__ == "__main__":
    # print(wytypuj_liczby(3, (1, 10)))
    # print(wylosuj_liczby(5, (1, 5)))
    pass
