from datetime import datetime, timedelta
from meni import admin_menu, trener_menu, user_menu
from prijavljeni_korisnik import prijavljeni_korisnik
from trening import *
import prijavljeni_korisnik


def ucitaj_korisnike():

    recnik_korisnika = {}
    with open("korisnici.txt", "r", encoding="utf-8") as fajl:
        for korisnik in fajl:
            podaci = korisnik.strip().split("|")
            korisnicko_ime = podaci[0]
            recnik_korisnika[korisnicko_ime] = {
                "username": podaci[0],
                "password": podaci[1],
                "ime": podaci[2],
                "prezime": podaci[3],
                "uloga": podaci[4],
                "status": podaci[5],
                "paket": podaci[6],
                "datum": podaci[7],
                "isticanje":podaci[8]
            }
    return recnik_korisnika


def registracija():

    korisnici = ucitaj_korisnike()

    while True:
        novo_korisnicko_ime = input("Unesite korisničko ime: ")

        if novo_korisnicko_ime in korisnici:
            print("Korisničko ime već postoji, pokušajte ponovo.")
            continue

        while True:
            lozinka = input("Unesite lozinku: ")
            if len(lozinka) <= 6 or not any(char.isdigit() for char in lozinka):
                print("Lozinka mora biti duža od 6 karaktera i mora sadržati bar jednu cifru.")
            else:
                break
        break

    ime = input("Unesite ime: ").title()
    prezime = input("Unesite prezime: ").title()
    uloga = "registrovan član"
    danas = datetime.now()
    formatiran_dan = danas.strftime("%d.%m.%Y.")
    isticanje_datum = danas + timedelta(days=30)
    formatiran_isticanje = isticanje_datum.strftime("%d.%m.%Y.")

    korisnici[novo_korisnicko_ime] = {
        "username": novo_korisnicko_ime,
        "password": lozinka,
        "ime": ime,
        "prezime": prezime,
        "uloga": uloga,
        "status": "aktivan",
        "paket": "standard",
        "datum": formatiran_dan,
        "isticanje": formatiran_isticanje
        }
    sacuvaj_korisnike(korisnici)


def sacuvaj_korisnike(korisnici):

    with open("korisnici.txt", "w", encoding="utf-8") as fajl:
        for korisnik, podaci in korisnici.items():
            fajl.write("|".join(podaci.values()) + "\n")


    return korisnici


def prijava():

    korisnici = ucitaj_korisnike()

    while True:
        korisnicko_ime = input("Unesite korisničko ime: ")
        if korisnicko_ime not in korisnici:
            print("Korisničko ime ne postoji. Pokušajte ponovo.")
            continue

        lozinka = input("Unesite lozinku: ")
        if korisnici[korisnicko_ime]["password"] != lozinka:
            print("Pogrešna lozinka. Pokušajte ponovo.")
            continue

        break

    if korisnicko_ime in korisnici and korisnici[korisnicko_ime]["password"] == lozinka and korisnici[korisnicko_ime]["status"] == "aktivan":
        korisnik_info = korisnici[korisnicko_ime]
        print(f"Prijava uspešna! Dobrodošli, {korisnik_info['ime']} {korisnik_info['prezime']}.")
        prijavljeni_korisnik.prijavljeni_korisnik = korisnicko_ime

        if korisnik_info['uloga'] == 'administrator':
            admin_menu()
        elif korisnik_info['uloga'] == 'instruktor':
            trener_menu()
        elif korisnik_info['uloga'] == 'registrovan član':
            user_menu()
    elif korisnicko_ime in korisnici and korisnici[korisnicko_ime]["password"] == lozinka and korisnici[korisnicko_ime]["status"] == "neaktivan":
        print("Aktivirajte nalog i pokušajte ponovo.")
    else:
        print("Pogrešno korisničko ime ili lozinka. Pokušajte ponovo.")
        return None


def registracija_instruktor():

    korisnici = ucitaj_korisnike()
    novo_korisnicko_ime = input("Unesite korisničko ime: ")

    if novo_korisnicko_ime in korisnici:
        print("Korisničko ime već postoji, pokušajte ponovo.")
        return None

    lozinka = input("Unesite lozinku: ")

    if len(lozinka) <= 6 or not any(char.isdigit() for char in lozinka):
        print("Lozinka mora biti duža od 6 karaktera i mora sadržavati bar jednu cifru.")
        return None

    ime = input("Unesite ime: ").title()
    prezime = input("Unesite prezime: ").title()
    uloga = input("Unesite ulogu (instruktor/administrator): ")
    danas = datetime.now()
    formatiran_dan = danas.strftime("%d.%m.%Y.")
    isticanje_datum = danas + timedelta(days=30)
    formatiran_isticanje = isticanje_datum.strftime("%d.%m.%Y.")

    korisnici[novo_korisnicko_ime] = {
        "username": novo_korisnicko_ime,
        "password": lozinka,
        "ime": ime,
        "prezime": prezime,
        "uloga": uloga,
        "status": "aktivan",
        "paket": "standard",
        "datum": formatiran_dan,
        "isticanje": formatiran_isticanje
    }
    sacuvaj_korisnike(korisnici)




if __name__ == "__main__":
    pass