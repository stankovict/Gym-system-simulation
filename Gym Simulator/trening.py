import textwrap

def ucitaj_programe_treninga():

    recnik_programa = {}
    with open("programi treninga.txt", "r", encoding="utf-8") as fajl:
        for red in fajl:
            podaci = red.strip().split("|")
            naziv_treninga = podaci[0]
            recnik_programa[naziv_treninga] = {
                "naziv": podaci[0],
                "vrsta": podaci[1],
                "trajanje": int(podaci[2]),
                "instruktori": podaci[3].split(", "),
                "opis": podaci[4],
                "paket": podaci[5],
                }

    return recnik_programa


def header_trening():

    print("Naziv programa treninga | Vrsta programa treninga | Trajanje | Instruktori               | Skraćeni opis                       | Paket članstva")
    print("------------------------+-------------------------+----------+---------------------------+-------------------------------------+---------------")


def ispis_programa(recnik_programa):

    print("********* Dostupni programi treninga *********")
    header_trening()
    for trening, detalji in recnik_programa.items():
        print("{:<24}| {:<24}| {:<9}| {:<26}| {:<36}| {:<12}".format(
            trening,
            detalji['vrsta'],
            f"{detalji['trajanje']} min",
            ', '.join(detalji['instruktori']),
            detalji['opis'],
            detalji['paket']
        ))


def visekriterijumska_pretraga_programa(programi):

    if not programi:
        print("Nema dostupnih programa za pretragu.")
        return

    print("\nDostupni kriterijumi za pretragu:")
    kriterijumi = {
        "1": "Naziv programa",
        "2": "Vrsta programa",
        "3": "Minimalno trajanje treninga",
        "4": "Maksimalno trajanje treninga",
        "5": "Paket članstva"
    }

    for key, value in kriterijumi.items():
        print(f"{key}. {value}")

    odabrani_kriterijumi = set()
    print("\nUnesite brojeve kriterijuma koje želite da koristite (odvojene razmakom): ")
    izbor = input("Vaš izbor: ").strip().split()

    for broj in izbor:
        if broj in kriterijumi:
            odabrani_kriterijumi.add(broj)
        else:
            print(f"Kriterijum sa brojem {broj} ne postoji.")

    if not odabrani_kriterijumi:
        print("Niste odabrali nijedan kriterijum za pretragu.")
        return

    print("\nUnesite vrednosti za odabrane kriterijume (ostavite prazno da preskočite):")
    naziv = vrsta = paket = None
    min_trajanje = 0
    max_trajanje = None

    if "1" in odabrani_kriterijumi:
        naziv = input("Naziv programa: ").strip().lower()
    if "2" in odabrani_kriterijumi:
        vrsta = input("Vrsta programa: ").strip().lower()
    if "3" in odabrani_kriterijumi:
        try:
            min_trajanje = int(input("Minimalno trajanje treninga (u minutima): ") or 0)
        except ValueError:
            print("Neispravan unos. Postavljena vrednost: 0 minuta.")
            min_trajanje = 0
    if "4" in odabrani_kriterijumi:
        try:
            max_trajanje_input = input("Maksimalno trajanje treninga (u minutima): ")
            max_trajanje = int(max_trajanje_input) if max_trajanje_input else None
        except ValueError:
            print("Neispravan unos. Nema ograničenja za maksimalno trajanje.")
            max_trajanje = None
    if "5" in odabrani_kriterijumi:
        paket = input("Paket članstva (standard/premium): ").strip().lower()

    rezultati = []
    for naziv_programa, detalji in programi.items():
        if naziv and naziv not in naziv_programa.lower():
            continue
        if vrsta and vrsta != detalji['vrsta'].lower():
            continue
        if not (min_trajanje <= detalji['trajanje'] <= (max_trajanje if max_trajanje is not None else float('inf'))):
            continue
        if paket and paket != detalji['paket'].lower():
            continue

        rezultati.append((naziv_programa, detalji))

    if rezultati:
        print("\n********* Rezultati pretrage *********")
        header_trening()
        for naziv, detalji in rezultati:
            print("{:<24}| {:<24}| {:<9}| {:<26}| {:<36}| {:<12}".format(
                naziv,
                detalji['vrsta'],
                f"{detalji['trajanje']} min",
                ', '.join(detalji['instruktori']),
                detalji['opis'],
                detalji['paket']
            ))
    else:
        print("\nNema programa koji ispunjavaju zadate kriterijume.")


def pretraga_programa_treninga(programi):

    if not programi:
        print("Nema dostupnih programa za pretragu.")
        return

    print("\nUnesite kriterijume pretrage (pritisnite Enter da preskočite kriterijum):")
    naziv = input("Naziv programa: ").strip().lower()
    vrsta = input("Vrsta programa: ").strip().lower()

    try:
        min_trajanje = int(input("Minimalno trajanje treninga (u minutima): ") or 0)
    except ValueError:
        print("Neispravan unos. Postavljena vrednost: 0 minuta.")
        min_trajanje = 0

    try:
        max_trajanje_input = input("Maksimalno trajanje treninga (u minutima): ")
        max_trajanje = int(max_trajanje_input) if max_trajanje_input else None
    except ValueError:
        print("Neispravan unos. Nema ograničenja za maksimalno trajanje.")
        max_trajanje = None

    paket = input("Paket članstva (standard/premium): ").strip().lower()

    rezultati = []
    for naziv_programa, detalji in programi.items():
        if naziv and naziv not in naziv_programa.lower():
            continue
        if vrsta and vrsta != detalji['vrsta'].lower():
            continue
        if not (min_trajanje <= detalji['trajanje'] <= (max_trajanje if max_trajanje is not None else float('inf'))):
            continue
        if paket and paket != detalji['paket'].lower():
            continue

        rezultati.append((naziv_programa, detalji))

    if rezultati:
        print("\n********* Rezultati pretrage *********")
        header_trening()
        for naziv, detalji in rezultati:
            print("{:<24}| {:<24}| {:<9}| {:<26}| {:<36}| {:<12}".format(
                naziv,
                detalji['vrsta'],
                f"{detalji['trajanje']} min",
                ', '.join(detalji['instruktori']),
                detalji['opis'],
                detalji['paket']
            ))
    else:
        print("\nNema programa koji ispunjavaju zadate kriterijume.")


def unos_programa_treninga(programi):

    naziv = input("Unesite naziv programa: ").strip().title()
    if naziv in programi:
        print("Program sa ovim nazivom već postoji!")
        return programi

    vrsta = input("Unesite vrstu programa: ").strip().title()

    try:
        trajanje = int(input("Unesite trajanje treninga u minutima: ").strip())
    except ValueError:
        print("Trajanje mora biti broj")
        return programi

    instruktori = input("Unesite imena instruktora (odvojena zarezom): ").strip().title().split(",")
    instruktori = [instr.strip() for instr in instruktori if instr.strip()]

    opis = input("Unesite skraćeni opis programa: ").strip().capitalize()
    paket = input("Unesite potrebni paket članstva (standard/premium): ").strip().lower()
    if paket not in ["standard", "premium"]:
        print("Paket mora biti 'standard' ili 'premium'.")
        return programi

    programi[naziv] = {
        "vrsta": vrsta,
        "trajanje": trajanje,
        "instruktori": instruktori,
        "opis": opis,
        "paket": paket,
    }

    print("Program treninga uspešno dodat!")
    return programi


def izmena_programa_treninga(programi):

    naziv = input("Unesite naziv programa koji želite da izmenite: ").strip().title()
    if naziv not in programi:
        print("Program sa tim nazivom ne postoji!")
        return programi

    print("\nTrenutni podaci o programu:")
    print(programi[naziv])

    print("\nUnesite nove podatke (pritisnite Enter za zadržavanje trenutne vrednosti):")
    vrsta = input(f"Vrsta programa ({programi[naziv]['vrsta']}): ").strip().title() or programi[naziv]['vrsta']
    trajanje = input(f"Trajanje treninga ({programi[naziv]['trajanje']} minuta): ").strip()
    trajanje = int(trajanje) if trajanje else programi[naziv]['trajanje']

    instruktori = input(f"Instruktori ({', '.join(programi[naziv]['instruktori'])}): ").strip().title()
    instruktori = [instr.strip() for instr in instruktori.split(",")] if instruktori else programi[naziv]['instruktori']

    opis = input(f"Opis programa ({programi[naziv]['opis']}): ").strip().capitalize() or programi[naziv]['opis']
    paket = input(f"Paket članstva ({programi[naziv]['paket']}): ").strip().lower() or programi[naziv]['paket']

    if paket not in ["standard", "premium"]:
        print("Paket mora biti 'standard' ili 'premium'.")
        return programi

    programi[naziv] = {
        "vrsta": vrsta,
        "trajanje": trajanje,
        "instruktori": instruktori,
        "opis": opis,
        "paket": paket,
    }

    print("Program treninga uspešno izmenjen!")
    return programi


def brisanje_programa_treninga(programi):

    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()
    naziv = input("Unesite naziv programa koji želite da obrišete: ").strip().title()

    if naziv not in programi:
        print("Program sa tim nazivom ne postoji!")
        return programi

    potvrda = input(f"Da li ste sigurni da želite da obrišete program '{naziv}'? (da/ne): ").strip().lower()
    if potvrda == "da":

        del programi[naziv]
        print(f"Program '{naziv}' je uspešno obrisan!")

        sifre_treninga_za_brisanje = [
            sifra for sifra, trening in treninzi.items() if trening['program'] == naziv
        ]

        for sifra in sifre_treninga_za_brisanje:
            del treninzi[sifra]
        print(f"Svi treninzi povezani sa programom '{naziv}' su obrisani.")

        termini_za_brisanje = [
            sifra for sifra, termin in termini.items() if termin['trening'] in sifre_treninga_za_brisanje
        ]
        for sifra in termini_za_brisanje:
            del termini[sifra]
        print(f"Svi termini povezani sa programom '{naziv}' su obrisani.")

        sacuvaj_programe_treninga(programi)
        sacuvaj_treninge(treninzi)
        sacuvaj_termine_treninga(termini)
    else:
        print("Brisanje programa je otkazano.")

    return programi


def sacuvaj_programe_treninga(programi):

    with open("programi treninga.txt", "w", encoding="utf-8") as fajl:
        for naziv, detalji in programi.items():
            fajl.write(f"{naziv}|{detalji['vrsta']}|{detalji['trajanje']}|{', '.join(detalji['instruktori'])}|{detalji['opis']}|{detalji['paket']}\n")


def ucitaj_termine_treninga():

    recnik_termina = {}
    with open("termini.txt", "r", encoding="utf-8") as fajl:
        for red in fajl:
            podaci = red.strip().split("|")
            sifra_termina = podaci[0]
            recnik_termina[sifra_termina] = {
                "trening": sifra_termina[:4],
                "datum": podaci[1]
                }
    return recnik_termina


def ucitaj_treninge():

    treninzi = {}
    with open("treninzi.txt", "r", encoding="utf-8") as fajl:
        for linija in fajl:
            delovi = linija.strip().split("|")
            sifra, sala, vreme_pocetka, vreme_kraja, dani, program = delovi
            treninzi[sifra] = {
                "sala": sala,
                "vreme_pocetka": vreme_pocetka,
                "vreme_kraja": vreme_kraja,
                "dani": dani,
                "program": program
            }
    return treninzi


def sacuvaj_treninge(treninzi):
    with open("treninzi.txt", "w", encoding="utf-8") as fajl:
        for sifra, detalji in treninzi.items():
            linija = f"{sifra}|{detalji['sala']}|{detalji['vreme_pocetka']}|{detalji['vreme_kraja']}|{"".join(detalji['dani'])}|{detalji['program']}\n"
            fajl.write(linija)


def unos_treninga(treninzi):

    sifra = input("Unesite sifru treninga: ").strip()
    if sifra in treninzi:
        print("Trening sa ovom sifrom vec postoji!")
        return treninzi

    sala = input("Unesite oznaku sale: ").strip()
    vreme_pocetka = input("Unesite vreme pocetka (hh:mm): ").strip()
    vreme_kraja = input("Unesite vreme kraja (hh:mm): ").strip()
    dani = input("Unesite dane odrzavanja (odvojene zarezom): ").strip().split(",")
    dani = [dan.strip() for dan in dani if dan.strip()]
    program = input("Unesite program treninga: ").strip()

    treninzi[sifra] = {
        "sala": sala,
        "vreme_pocetka": vreme_pocetka,
        "vreme_kraja": vreme_kraja,
        "dani": ",".join(dani),
        "program": program
    }

    print("Trening uspešno dodat!")
    return treninzi


def izmena_treninga(treninzi):

    sifra = input("Unesite sifru treninga za izmenu: ").strip()
    if sifra not in treninzi:
        print("Trening sa ovom sifrom ne postoji!")
        return treninzi

    print("\nTrenutni podaci o treningu:")
    print(treninzi[sifra])

    print("\nUnesite nove podatke (pritisnite Enter za zadrzavanje trenutne vrednosti):")
    sala = input("Oznaka sale: ").strip() or treninzi[sifra]['sala']
    vreme_pocetka = input("Vreme pocetka: ").strip() or treninzi[sifra]['vreme_pocetka']
    vreme_kraja = input("Vreme kraja: ").strip() or treninzi[sifra]['vreme_kraja']
    dani = input("Dani (ako ima više dana uneti u formatu dan,dan): ").strip() or treninzi[sifra]['dani']
    program = input(f"Program ({treninzi[sifra]['program']}): ").strip() or treninzi[sifra]['program']

    treninzi[sifra] = {
        "sala": sala,
        "vreme_pocetka": vreme_pocetka,
        "vreme_kraja": vreme_kraja,
        "dani": dani,
        "program": program
    }

    print("Trening uspešno izmenjen!")

    return treninzi


def brisanje_treninga(treninzi):

    sifra = input("Unesite sifru treninga za brisanje: ").strip()
    if sifra not in treninzi:
        print("Trening sa ovom sifrom ne postoji!")
        return treninzi

    potvrda = input(f"Da li ste sigurni da želite da obrišete trening '{sifra}'? (da/ne): ").strip().lower()
    if potvrda == "da":
        del treninzi[sifra]
        print(f"Trening '{sifra}' je uspešno obrisan!")
    else:
        print("Brisanje treninga je otkazano.")

    return treninzi


def header_termin():
    print("Datum       | Vreme         | Program         | Sala    | Paket")
    print("------------+---------------+-----------------+---------+-------")


def ispis_termina(termini, treninzi, sale):

    print("\n********* Dostupni termini treninga *********")
    header_termin()
    for termin, detalji in termini.items():
        trening = treninzi.get(detalji['sifra_treninga'], {"naziv": "Nepoznat"})
        sala = sale.get(detalji['sifra_sale'], {"naziv": "Nepoznata"})
        print("{:<12} | {:<13} | {:<15} | {:<7} | {:<7}".format(
            detalji['datum'],
            f"{detalji['vreme_pocetka']} - {detalji['vreme_kraja']}",
            trening['naziv'],
            sala['naziv'],
            detalji['paket']
        ))


def pretrazi_termine(recnik_termina, recnik_treninga):

    print("Pretraga termina treninga")
    print("1. Pretraga po programu")
    print("2. Pretraga po sali")
    print("3. Pretraga po potrebnom uplaćenom paketu")
    print("4. Pretraga po datumu")
    print("5. Pretraga po vremenu početka i kraja")
    izbor = input("Izaberite opciju (1-5): ")

    rezultati = []

    if izbor == "1":
        program = input("Unesite naziv programa: ").strip()
        for sifra, podaci in recnik_termina.items():
            sifra_treninga = podaci["trening"]
            if recnik_treninga[sifra_treninga]["program"].lower() == program.lower():
                rezultati.append((sifra, podaci, recnik_treninga[sifra_treninga]))

    elif izbor == "2":
        sala = input("Unesite oznaku sale (1, 2, 3, 4): ").strip()
        for sifra, podaci in recnik_termina.items():
            sifra_treninga = podaci["trening"]
            if recnik_treninga[sifra_treninga]["sala"].lower() == sala.lower():
                rezultati.append((sifra, podaci, recnik_treninga[sifra_treninga]))


    elif izbor == "3":
        programi = ucitaj_programe_treninga()
        paket = input("Unesite naziv paketa (premium ili standardni): ").strip()
        for sifra, podaci in recnik_termina.items():
            sifra_treninga = podaci["trening"]
            if sifra_treninga in recnik_treninga:
                naziv_programa = recnik_treninga[sifra_treninga]["program"]
                if naziv_programa in programi:
                    if programi[naziv_programa]["paket"].lower() == paket.lower():
                        rezultati.append((sifra, podaci, recnik_treninga[sifra_treninga]))


    elif izbor == "4":
        datum = input("Unesite datum (npr. 16.12.2024.): ").strip()
        for sifra, podaci in recnik_termina.items():
            if podaci["datum"] == datum:
                sifra_treninga = podaci["trening"]
                rezultati.append((sifra, podaci, recnik_treninga[sifra_treninga]))

    elif izbor == "5":
        vreme_pocetka = input("Unesite vreme početka (npr. 09:00): ").strip()
        vreme_kraja = input("Unesite vreme kraja (npr. 10:00): ").strip()
        for sifra, podaci in recnik_termina.items():
            sifra_treninga = podaci["trening"]
            trening_podaci = recnik_treninga[sifra_treninga]
            if (trening_podaci["vreme_pocetka"] == vreme_pocetka and
                    trening_podaci["vreme_kraja"] == vreme_kraja):
                rezultati.append((sifra, podaci, trening_podaci))

    else:
        print("Pogrešan izbor!")
        return

    if rezultati:
        print("\nPronađeni termini:")
        print("Šifra termina | Datum     | Program     | Sala   | Vreme        ")
        print("--------------+-----------+-------------+--------+--------------")
        for sifra, termin, trening in rezultati:
            print("{:14}|{:10}|{:13}|{:8}|{:10}".format(
                sifra,
                termin['datum'],
                trening['program'],
                trening['sala'],
                trening['vreme_pocetka']
            ))

    else:
        print("Nema termina koji ispunjavaju kriterijume.")


def sacuvaj_termine_treninga(termini):

    with open("termini.txt", "w", encoding="utf-8") as fajl:
        for sifra_termina, detalji in termini.items():
            fajl.write(f"{sifra_termina}|{detalji['datum']}\n")


def detaljno_programi(programi):

    print("\n"+150*"=")
    izbor = input("Da li želite da pročitate više o nekom od ponuđenih programa? (da/ne): ")

    if izbor.lower() == "ne":
        return
    elif izbor.lower() == "da":
        prog = input("Unesite naziv programa treninga: ").strip().title()
        if prog in programi:
            print("Duži opis programa:\n")
            fajl = f"{prog}.txt"
            try:
                with open(fajl, "r", encoding="utf-8") as f:
                    for linija in f:
                        print(linija.strip())
            except FileNotFoundError:
                print("Ovaj program nema opis.")
        else:
            print("Program ne postoji.")



def dodaj_opis_programa(programi):

    prog = input("Unesite naziv programa kojem želite da dodate opis: ").strip().title()

    if prog not in programi:
        print("Program ne postoji.")
        return

    print("Unesite opis programa. Kada završite, unesite samo tačku (.) u novom redu.")

    linije = []
    while True:
        linija = input()
        if linija.strip() == ".":
            break
        linije.append(linija)

    ceo_tekst = " ".join(linije)
    formatiran_tekst = textwrap.fill(ceo_tekst, width=80)

    fajl = f"{prog}.txt"

    with open(fajl, "w", encoding="utf-8") as f:
        f.write(formatiran_tekst)


if __name__ == "__main__":
    programi = ucitaj_programe_treninga()
    dodaj_opis_programa(programi)
