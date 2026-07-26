def wybierz_opcje():
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")
    decyzja = int(input("Wybierz opcję: "))
    return decyzja

def usun_zadanie():
    with open("zadania.txt", "r") as plik:
        zadania = plik.readlines()

    licznik = 1

    for zadanie in zadania:
        print(licznik, zadanie)
        licznik += 1

    wybor = int(input("Które zadanie chcesz usunąć?"))

    zadania.pop(wybor - 1)

    with open("zadania.txt", "w") as plik:
        for zadanie in zadania:
            plik.write(zadanie)
    
def wykonaj_polecenie(decyzja):
    if decyzja == 1:
        with open("zadania.txt", "r") as plik:
            zawartosc = plik.read()
            print(zawartosc)
    elif decyzja == 2:
        zadanie = input("Podaj zadanie: ")

        with open("zadania.txt", "a") as plik:
            plik.write(zadanie + "\n")
    elif decyzja == 3:
        usun_zadanie()

decyzja = wybierz_opcje()

while decyzja != 4:
    wykonaj_polecenie(decyzja)
    decyzja = wybierz_opcje()

wykonaj_polecenie(decyzja)
