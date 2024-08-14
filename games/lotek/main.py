import os
from time import sleep
from lotek import sprawdz_zakres, wylosuj_liczby, wytypuj_liczby, trafione

def clear(): os.system("cls" if os.name == "nt" else "clear")

def lotto(ile_liczb, min_max):
    try:
        sprawdz_zakres(ile_liczb, min_max)
    except Exception as exception:
        print(repr(exception))

    try:
        typy = wytypuj_liczby(ile_liczb, min_max)
        wylosowane = wylosuj_liczby(ile_liczb, min_max)
        wyniki = trafione(wylosowane, typy)

        print(f"\nWylosowane liczby: {wylosowane}")
        print(f"Wytypowane liczby: {typy}")
        print(f"Trafione liczby: {wyniki}")
        print(f"\nTrafiono {len(wyniki)} / {ile_liczb}\n")
    except:
        print("Wystapil jakis blad.")

def maly_lotek(): lotto(1, (1, 10))

def duzy_lotek(): lotto(6, (1, 49))

def extra_lotek(): lotto(10, (1, 100))


def main():
    clear()
    print("Wybierz Lotto:")
    print("A - Maly Lotek")
    print("B - Duzy Lotek")
    print("C - Extra Lotek")
    
    wybor = input("Twoj wybor: ").upper()

    if wybor == "A":
        maly_lotek()
    elif wybor == "B":
        duzy_lotek()
    elif wybor == "C":
        extra_lotek()
    else:
        print("Wybrano zla opcje. Wybierz A, B, C.")
        sleep(3)
        return main()

    # match wybor:
    #     case "A":
    #         maly_lotek()
    #     case "B":
    #         duzy_lotek()
    #     case "C":
    #         extra_lotek()
    #     case _:
    #         print("Wybrano zla opcje. Wybierz A, B, C.")
    #         sleep(3)
    #         return main()

    powtorka = input("Czy chcesz zagrac jeszcze raz? T/N\n")
    if powtorka.upper() == "T":
        return main()

if __name__ == "__main__":
    # pass
    main()
