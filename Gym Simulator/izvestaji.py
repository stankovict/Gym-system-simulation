from sale import *
from datetime import datetime, timedelta
from collections import defaultdict

def izvestaj_a():

    rezervacije = ucitaj_rezervacije()
    if not rezervacije:
        print("Nema rezervacija u sistemu.")
        return

    odabrani_datum = input("Unesite datum rezervacije (format dd.mm.gggg.): ").strip() #gleda se dan kada je rezervacija napravljena ne kada se trening odrzava

    filtrirane_rezervacije = [rez for rez in rezervacije if rez["datum"] == odabrani_datum] #pravi se lista rezervacija koje odgovaraju datumu

    if not filtrirane_rezervacije:
        print(f"Nema rezervacija za odabrani datum: {odabrani_datum}.")
        return


    print(f"Izveštaj rezervacija za datum: {odabrani_datum}")
    print("-" * 50)
    print(f"{'Korisničko ime':<20}{'Termin':<10}{'Mesto':<10}")
    print("-" * 50)

    for rez in filtrirane_rezervacije:
        print(f"{rez['korisnicko_ime']:<20}{rez['termin']:<10}{rez['mesto']:<10}")

    print("-" * 50)


    sacuvaj = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? (da/ne): ").strip().lower()
    if sacuvaj == "da":
        naziv_fajla = "izvestaj_a.txt"
        with open(naziv_fajla, 'a', encoding='utf-8') as file:
            file.write(f"Izveštaj rezervacija za datum: {odabrani_datum}\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'Korisničko ime':<20}{'Termin':<10}{'Mesto':<10}\n")
            file.write("-" * 50 + "\n")
            for rez in filtrirane_rezervacije:
                file.write(f"{rez['korisnicko_ime']:<20}{rez['termin']:<10}{rez['mesto']:<10}\n")
            file.write("-" * 50 + "\n")
        print(f"Izveštaj je uspešno sačuvan u fajlu: {naziv_fajla}")


def izvestaj_b():

    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    if not rezervacije:
        print("Nema rezervacija u sistemu.")
        return

    odabrani_datum = input("Unesite datum termina (format dd.mm.gggg.): ").strip() #datum kada se odrzava termin ne kada je napravljena rez


    filtrirane_rezervacije = [] #drugaciji nacin
    for rez in rezervacije:
        sifra_termina = rez["termin"]
        if sifra_termina in termini and termini[sifra_termina]["datum"] == odabrani_datum:
            filtrirane_rezervacije.append(rez)

    if not filtrirane_rezervacije:
        print(f"Nema rezervacija za termine sa datumom: {odabrani_datum}.")
        return


    print(f"Izveštaj rezervacija za datum termina: {odabrani_datum}")
    print("-" * 50)
    print(f"{'Korisničko ime':<20}{'Termin':<10}{'Mesto':<10}")
    print("-" * 50)

    for rez in filtrirane_rezervacije:
        print(f"{rez['korisnicko_ime']:<20}{rez['termin']:<10}{rez['mesto']:<10}")

    print("-" * 50)


    sacuvaj = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? (da/ne): ").strip().lower()
    if sacuvaj == "da":
        naziv_fajla = "izvestaj_b.txt"
        with open(naziv_fajla, 'a', encoding='utf-8') as file:
            file.write(f"Izveštaj rezervacija za datum termina: {odabrani_datum}\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'Korisničko ime':<20}{'Termin':<10}{'Mesto':<10}\n")
            file.write("-" * 50 + "\n")
            for rez in filtrirane_rezervacije:
                file.write(f"{rez['korisnicko_ime']:<20}{rez['termin']:<10}{rez['mesto']:<10}\n")
            file.write("-" * 50 + "\n")
        print(f"Izveštaj je uspešno sačuvan u fajlu: {naziv_fajla}")


def izvestaj_c():

    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()
    programi = ucitaj_programe_treninga()

    if not rezervacije:
        print("Nema rezervacija u sistemu.")
        return

    odabrani_datum = input("Unesite datum rezervacije (format dd.mm.gggg.): ").strip()
    ime_instruktora = input("Unesite ime instruktora: ").strip().title()

    filtrirane_rezervacije = []

    for rez in rezervacije:
        if rez["datum"] != odabrani_datum:
            continue

        sifra_termina = rez["termin"]
        if sifra_termina not in termini:
            continue


        sifra_treninga = sifra_termina[:4]

        if sifra_treninga not in treninzi:
            continue

        naziv_treninga = treninzi[sifra_treninga]["program"]

        if naziv_treninga not in programi:
            continue

        instruktor = programi[naziv_treninga]["instruktori"]
        if ime_instruktora not in instruktor:
            continue

        filtrirane_rezervacije.append(rez)

    if not filtrirane_rezervacije:
        print(f"Nema rezervacija za datum {odabrani_datum} i instruktora {ime_instruktora}.")
        return


    print(f"Izveštaj rezervacija za datum {odabrani_datum} i instruktora {ime_instruktora}")
    print("-" * 60)
    print(f"{'Korisničko ime':<20}{'Termin':<10}{'Mesto':<10}")
    print("-" * 60)

    for rez in filtrirane_rezervacije:
        print(f"{rez['korisnicko_ime']:<20}{rez['termin']:<10}{rez['mesto']:<10}")

    print("-" * 60)

    sacuvaj = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? (da/ne): ").strip().lower()
    if sacuvaj == "da":
        naziv_fajla = "izvestaj_c.txt"
        with open(naziv_fajla, 'a', encoding='utf-8') as file:
            file.write(f"Izveštaj rezervacija za datum {odabrani_datum} i instruktora {ime_instruktora}\n")
            file.write("-" * 60 + "\n")
            file.write(f"{'Korisničko ime':<20}{'Termin':<10}{'Mesto':<10}\n")
            file.write("-" * 60 + "\n")
            for rez in filtrirane_rezervacije:
                file.write(f"{rez['korisnicko_ime']:<20}{rez['termin']:<10}{rez['mesto']:<10}\n")
            file.write("-" * 60 + "\n")
        print(f"Izveštaj je uspešno sačuvan u fajlu: {naziv_fajla}")


def izvestaj_d():

    recnik_termina = ucitaj_termine_treninga()
    recnik_treninga = ucitaj_treninge()
    rezervacije = ucitaj_rezervacije()

    dan_u_nedelji = input("Unesite dan u nedelji (ponedeljak, utorak, sreda, četvrtak, petak, subota, nedelja): ").strip().lower()

    validni_dani = ["ponedeljak", "utorak", "sreda", "četvrtak", "petak", "subota", "nedelja"]
    if dan_u_nedelji not in validni_dani:
        print("Pogrešan unos dana!")
        return

    ukupan_broj_rezervacija = 0
    rezervacije_za_dan = []

    for rez in rezervacije:
        sifra_termina = rez["termin"]
        if sifra_termina not in recnik_termina:
            continue

        sifra_treninga = sifra_termina[:4]

        if sifra_treninga not in recnik_treninga:
            continue

        dani_odrzavanja = [d.strip().lower() for d in recnik_treninga[sifra_treninga]["dani"].split(",")]

        if dan_u_nedelji in dani_odrzavanja:
            ukupan_broj_rezervacija += 1
            rezervacije_za_dan.append(rez)

    print(f"\nUkupan broj rezervacija za treninge koji se održavaju {dan_u_nedelji}: {ukupan_broj_rezervacija}\n")

    if rezervacije_za_dan:
        print(f"{'Termin':<12} | {'Korisnik':<15} | {'Mesto':<6} | {'Datum':<12}")
        print("-" * 55)
        for rez in rezervacije_za_dan:
            print(f"{rez['termin']:<12} | {rez['korisnicko_ime']:<15} | {rez['mesto']:<6} | {rez['datum']:<12}")
        print("-" * 55)
    else:
        print("Nema rezervacija za izabrani dan.")

    opcija_snimanja = input("\nDa li želite da sačuvate izveštaj u fajl? (da/ne): ").strip().lower()
    if opcija_snimanja == "da":
        naziv_fajla = "izvestaj_d.txt"
        with open(naziv_fajla, "a", encoding="utf-8") as fajl:
            fajl.write(f"Izveštaj za dan {dan_u_nedelji}:\n")
            fajl.write(f"Ukupan broj rezervacija: {ukupan_broj_rezervacija}\n\n")
            fajl.write(f"{'Termin':<12} | {'Korisnik':<15} | {'Mesto':<6} | {'Datum':<12}\n")
            fajl.write("-" * 55 + "\n")

            for rez in rezervacije_za_dan:
                fajl.write(f"{rez['termin']:<12} | {rez['korisnicko_ime']:<15} | {rez['mesto']:<6} | {rez['datum']:<12}\n")

        print("Izveštaj je sačuvan u 'izvestaj_d.txt'.")


def izvestaj_e():

    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()
    programi = ucitaj_programe_treninga()

    if not rezervacije:
        print("Nema rezervacija u sistemu.")
        return


    danas = datetime.now()
    granica = danas - timedelta(days=30)


    statistika_instruktora = {}

    for rez in rezervacije:

        datum_rezervacije = datetime.strptime(rez["datum"], "%d.%m.%Y.")
        if datum_rezervacije < granica:
            continue

        sifra_termina = rez["termin"]
        if sifra_termina not in termini:
            continue


        sifra_treninga = sifra_termina[:4]
        if sifra_treninga not in treninzi:
            continue

        naziv_treninga = treninzi[sifra_treninga]["program"]
        if naziv_treninga not in programi:
            continue


        instruktori = programi[naziv_treninga]["instruktori"]


        for instruktor in instruktori:
            if instruktor not in statistika_instruktora:
                statistika_instruktora[instruktor] = 0
            statistika_instruktora[instruktor] += 1


    sortirana_statistika = sorted(statistika_instruktora.items(), key=lambda x: x[1], reverse=True) #uzima broj rezervacija i obrce ih od najvece do najmanje


    print("Ukupan broj rezervacija po instruktorima u poslednjih 30 dana")
    print("-" * 60)
    print(f"{'Instruktor':<30}{'Broj rezervacija':<20}")
    print("-" * 60)

    for instruktor, broj_rezervacija in sortirana_statistika:
        print(f"{instruktor:<30}{broj_rezervacija:<20}")

    print("-" * 60)

    sacuvaj = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? (da/ne): ").strip().lower()
    if sacuvaj == "da":
        naziv_fajla = "izvestaj_e.txt"
        with open(naziv_fajla, 'a', encoding='utf-8') as file:
            file.write("Ukupan broj rezervacija po instruktorima u poslednjih 30 dana\n")
            file.write("-" * 60 + "\n")
            file.write(f"{'Instruktor':<30}{'Broj rezervacija':<20}\n")
            file.write("-" * 60 + "\n")
            for instruktor, broj_rezervacija in sortirana_statistika:
                file.write(f"{instruktor:<30}{broj_rezervacija:<20}\n")
            file.write("-" * 60 + "\n")
        print(f"Izveštaj je uspešno sačuvan u fajlu: {naziv_fajla}")


def izvestaj_f():

    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()
    programi = ucitaj_programe_treninga()

    danas = datetime.now()
    granica = danas - timedelta(days=30)


    premium_rezervacije = 0
    standard_rezervacije = 0

    for rez in rezervacije:

        datum_rezervacije = datetime.strptime(rez["datum"].strip("."), "%d.%m.%Y")

        if datum_rezervacije < granica:
            continue

        sifra_termina = rez["termin"]
        if sifra_termina not in termini:
            continue

        sifra_treninga = sifra_termina[:4]
        if sifra_treninga not in treninzi:
            continue

        naziv_treninga = treninzi[sifra_treninga]["program"]
        if naziv_treninga not in programi:
            continue


        paket = programi[naziv_treninga]["paket"].lower()
        if paket == "premium":
            premium_rezervacije += 1
        elif paket == "standard":
            standard_rezervacije += 1


    print("Izveštaj o broju rezervacija po paketima članstva u poslednjih 30 dana")
    print("-" * 60)
    print(f"{'Tip paketa':<30}{'Broj rezervacija':<30}")
    print("-" * 60)
    print(f"{'Premium':<30}{premium_rezervacije:<30}")
    print(f"{'Standardni':<30}{standard_rezervacije:<30}")
    print("-" * 60)


    sacuvaj = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? (da/ne): ").strip().lower()
    if sacuvaj == "da":
        naziv_fajla = "izvestaj_f.txt"
        with open(naziv_fajla, 'a', encoding='utf-8') as file:
            file.write(f"{'Tip paketa':<30}{'Broj rezervacija':<30}\n")
            file.write("-" * 60 + "\n")
            file.write(f"{'Premium':<30}{premium_rezervacije:<30}\n")
            file.write(f"{'Standardni':<30}{standard_rezervacije:<30}\n")
            file.write("-" * 60 + "\n")
        print(f"Izveštaj je uspešno sačuvan u fajlu: {naziv_fajla}")


def izvestaj_g():

    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()
    programi = ucitaj_programe_treninga()

    if not rezervacije:
        print("Nema rezervacija u sistemu.")
        return

    danas = datetime.now()
    granica = danas - timedelta(days=365)

    brojac_rezervacija_po_programu = defaultdict(int) #inicijalizuj prvu vrednost na 0, default

    for rez in rezervacije:
        datum_rezervacije = datetime.strptime(rez["datum"].strip("."), "%d.%m.%Y")

        if datum_rezervacije < granica:
            continue

        sifra_termina = rez["termin"]
        if sifra_termina not in termini:
            continue


        sifra_treninga = sifra_termina[:4]
        if sifra_treninga not in treninzi:
            continue

        naziv_treninga = treninzi[sifra_treninga]["program"]
        if naziv_treninga not in programi:
            continue


        brojac_rezervacija_po_programu[naziv_treninga] += 1


    sortirani_programi = sorted(brojac_rezervacija_po_programu.items())


    print("Najpopularniji programi treninga u poslednjih godinu dana")
    print("-" * 60)
    print(f"{'Program':<40}{'Broj rezervacija':<20}")
    print("-" * 60)

    for program, broj in sortirani_programi[:3]: #uzima prva tri
        print(f"{program:<40}{broj:<20}")

    print("-" * 60)


    sacuvaj = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? (da/ne): ").strip().lower()
    if sacuvaj == "da":
        naziv_fajla = "izvestaj_g.txt"
        with open(naziv_fajla, 'a', encoding='utf-8') as file:
            file.write("Najpopularniji programi treninga u poslednjih godinu dana\n")
            file.write("-" * 60 + "\n")
            file.write(f"{'Program':<40}{'Broj rezervacija':<20}\n")
            file.write("-" * 60 + "\n")
            for program, broj in sortirani_programi[:3]:
                file.write(f"{program:<40}{broj:<20}\n")
            file.write("-" * 60 + "\n")


def izvestaj_h():

    rezervacije = ucitaj_rezervacije()
    recnik_termina = ucitaj_termine_treninga()
    recnik_treninga = ucitaj_treninge()

    dani_na_srpskom = {
        "monday": "ponedeljak",
        "tuesday": "utorak",
        "wednesday": "sreda",
        "thursday": "četvrtak",
        "friday": "petak",
        "saturday": "subota",
        "sunday": "nedelja"
    }

    broj_rezervacija_po_danima = {}

    for rez in rezervacije:
        sifra_termina = rez["termin"]
        if sifra_termina not in recnik_termina:
            continue

        sifra_treninga = sifra_termina[:4]
        if sifra_treninga not in recnik_treninga:
            continue

        datum_str = recnik_termina[sifra_termina].get("datum")
        if not datum_str:
            continue

        try:
            datum = datetime.strptime(datum_str, "%d.%m.%Y.")
        except ValueError:
            continue

        dan_eng = datum.strftime("%A").lower() #odredi koji je dan
        dan_srpski = dani_na_srpskom.get(dan_eng) #iz recnika uzmi srpski dan

        broj_rezervacija_po_danima[dan_srpski] = broj_rezervacija_po_danima.get(dan_srpski, 0) + 1

    if not broj_rezervacija_po_danima:
        print("Nema rezervacija za prikaz.")
        return

    print("\n********* BROJ REZERVACIJA PO DANIMA *********")
    print("{:<12} | {:<20}".format("Dan", "Broj rezervacija"))
    print("-" * 35)
    for dan, broj in broj_rezervacija_po_danima.items():
        print("{:<12} | {:<20}".format(dan.capitalize(), broj))
    print("-" * 35)

    max_broj = max(broj_rezervacija_po_danima.values())
    najpopularniji_dani = [dan for dan, broj in broj_rezervacija_po_danima.items() if broj == max_broj]

    if len(najpopularniji_dani) == 1:
        print(f"Najpopularniji dan u nedelji je: {najpopularniji_dani[0].capitalize()} ({max_broj} rezervacija)")
    else:
        dani_str = ", ".join(d.capitalize() for d in najpopularniji_dani)
        print(f"Najpopularniji dani u nedelji su: {dani_str} ({max_broj} rezervacija svaki)")

    opcija = input("Da li želite da sačuvate izveštaj u fajl? (da/ne): ").strip().lower()
    if opcija == "da":
        naziv_fajla = "izvestaj_h.txt"
        with open(naziv_fajla, "a", encoding="utf-8") as fajl:
            fajl.write("Najpopularniji dan u nedelji - izveštaj\n")
            fajl.write("-" * 35 + "\n")
            for dan, broj in broj_rezervacija_po_danima.items():
                fajl.write(f"{dan.capitalize():<12} | {broj}\n")
            fajl.write("-" * 35 + "\n")
            if len(najpopularniji_dani) == 1:
                fajl.write(f"Najpopularniji dan: {najpopularniji_dani[0].capitalize()} "
                           f"({max_broj} rezervacija)\n")
            else:
                dani_str = ", ".join(d.capitalize() for d in najpopularniji_dani)
                fajl.write(f"Najpopularniji dani: {dani_str} ({max_broj} rezervacija svaki)\n")
        print("Izveštaj je sačuvan u 'izvestaj_najpopularniji_dan.txt'.")



if __name__ == "__main__":
    print(izvestaj_h())