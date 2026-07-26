def podaj_imie():
    imie = input("Podaj imię: ")
    return imie

imie = podaj_imie()

def podaj_email():
    email = input("Podaj email: ")
    return email

email = podaj_email()

def wartosc_zamowienia():
    wartosc = float(input("Podaj wartość zamówienia: "))
    return wartosc

wartosc = wartosc_zamowienia()

plik = open("baza_klientow.txt", "a")

plik.write(imie + "|" + email + "|" + str(wartosc) + "\n")

plik.close()
