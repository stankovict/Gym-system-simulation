from datetime import datetime
import login_logout_signin
from login_logout_signin import *
from trening import *
from prijavljeni_korisnik import prijavljeni_korisnik
import prijavljeni_korisnik

def ucitaj_sale():

    with open("sale.txt", 'r', encoding="utf-8") as fajl:
        recnik_sala = {}
        for line in fajl:
            sala = line.strip().split("|")
            if len(sala) == 4:
                sifra_sale, ime_sale, broj_redova, mesta = sala
                recnik_sala[sifra_sale] = {
                    "sifra_sale": sifra_sale,
                    "ime_sale": ime_sale,
                    "broj_redova": int(broj_redova),
                    "mesta": list(mesta),
                }
        return recnik_sala


def sacuvaj_sale(sale):

    with open("sale.txt", 'w', encoding='utf-8') as file:
        for sala in sale.values():
            mesta_str = "".join(sala['mesta'])
            file.write(
                f"{sala['sifra_sale']}|{sala['ime_sale']}|{sala['broj_redova']}|{mesta_str}\n")


def sacuvaj_rezervacije(rezervacije):

    with open("rezervacije.txt", 'w', encoding='utf-8') as file:
        for rez in rezervacije:
            file.write(f"{rez['korisnicko_ime']}|{rez['termin']}|{rez['mesto']}|{rez['datum']}\n")


def ucitaj_rezervacije():

    with open("rezervacije.txt", 'r', encoding='utf-8') as file:
        rezervacije = []
        for line in file:
            korisnicko_ime, termin, mesto, datum = line.strip().split("|")
            rezervacije.append({
                "korisnicko_ime": korisnicko_ime,
                "termin": termin,
                "mesto": mesto,
                "datum": datum
                })
    return rezervacije


def matricni_prikaz(sifra_sale, sifra_termina):

    recnik_sala = ucitaj_sale()
    recnik_termina = ucitaj_termine_treninga()
    rezervacije = ucitaj_rezervacije()

    if sifra_sale not in recnik_sala:
        print("Sala sa unetom šifrom ne postoji.")
        return

    if sifra_termina not in recnik_termina:
        print("Termin sa unetom šifrom ne postoji.")
        return

    sala = recnik_sala[sifra_sale]
    broj_redova = sala['broj_redova']
    mesta = sala['mesta']

    rezervisana_mesta = {rez['mesto'] for rez in rezervacije if rez['termin'] == sifra_termina}

    print(f"Sala: {sala['ime_sale']} ({sala['sifra_sale']}), Termin: {sifra_termina}")
    for red in range(1, broj_redova + 1): #da bi kretalo od 1
        print(f"Red {red:<4} |", end=" ") #da nastavi isti red
        for mesto in mesta:
            oznaka_mesta = f"{red}{mesto}"
            if oznaka_mesta in rezervisana_mesta:
                print("X", end=" ") #ako je u rezervisanim oznaci ga sa X
            else:
                print(mesto, end=" ")
        print()
    print()


def rezervisi_mesto():

    korisnicko_ime = prijavljeni_korisnik.prijavljeni_korisnik
    recnik_sala = ucitaj_sale()
    recnik_termina = ucitaj_termine_treninga()
    recnik_treninga = ucitaj_treninge()
    recnik_programa = ucitaj_programe_treninga()
    korisnici = login_logout_signin.ucitaj_korisnike()
    rezervacije = ucitaj_rezervacije() or []

    sifra_termina = input("Unesite šifru termina: ").strip()
    if sifra_termina not in recnik_termina:
        print("Termin nije pronađen.")
        return

    termin = recnik_termina[sifra_termina]
    sifra_treninga = termin["trening"]

    if sifra_treninga not in recnik_treninga:
        print("Trening nije pronađen.")
        return

    trening = recnik_treninga[sifra_treninga]
    sifra_sale = trening["sala"]
    sifra_programa = trening["program"]

    if sifra_sale not in recnik_sala:
        print("Sala nije pronađena.")
        return
    if sifra_programa not in recnik_programa:
        print("Program nije pronađen.")
        return

    sala = recnik_sala[sifra_sale]
    program = recnik_programa[sifra_programa]
    potreban_paket = program["paket"].lower()

    korisnik_info = korisnici.get(korisnicko_ime)
    if not korisnik_info:
        print("Korisnik nije pronađen.")
        return
    korisnikov_paket = korisnik_info.get("paket").lower()

    danas = datetime.now()
    danasnji_datum = danas.strftime("%d.%m.%Y.")
    danasnji_dan = danas.strftime("%A").lower()


    if danasnji_dan != "friday":
        if korisnikov_paket == "standard" and potreban_paket != "standard":
            print(f"Ovaj trening zahteva '{potreban_paket}' paket, a vi imate 'standard'.")
            return
        elif korisnikov_paket not in ["standard", "premium"]:
            print("Nemate validan paket.")
            return

    matricni_prikaz(sifra_sale, sifra_termina)

    while True:
        odabrano_mesto = input("Unesite oznaku mesta za rezervaciju (npr. 1A): ").strip()
        red = odabrano_mesto[:-1]
        kolona = odabrano_mesto[-1]

        if not red.isdigit() or int(red) > sala["broj_redova"]:
            print("Uneli ste nepostojeći red.")
            continue

        if kolona not in sala["mesta"]:
            print("Uneli ste nepostojeću kolonu.")
            continue

        if any(
            rez['mesto'] == odabrano_mesto and rez['termin'] == sifra_termina
            for rez in rezervacije
        ):
            print("Odabrano mesto je već rezervisano za ovaj termin.")
            continue

        rezervacije.append({
            "korisnicko_ime": korisnicko_ime,
            "termin": sifra_termina,
            "mesto": odabrano_mesto,
            "datum": danasnji_datum
        })

        sacuvaj_rezervacije(rezervacije)
        print(f"Mesto {odabrano_mesto} je uspešno rezervisano za termin {sifra_termina} ({danasnji_datum}).")
        break

    jos_mesta = input("Da li želite da rezervišete još mesta? (da/ne): ").strip().lower()
    if jos_mesta == "da":
        rezervisi_mesto()


def ponisti_rezervaciju():

    korisnicko_ime = prijavljeni_korisnik.prijavljeni_korisnik
    rezervacije = ucitaj_rezervacije()
    if not rezervacije:
        print("Nema rezervacija za poništavanje.")
        return

    sifra_termina = input("Unesite šifru termina: ").strip()
    mesto = input("Unesite oznaku mesta za poništavanje (npr. 1A): ").strip()

    rezervacija_za_brisanje = None
    for rezervacija in rezervacije:
        if (
            rezervacija["korisnicko_ime"] == korisnicko_ime and
            rezervacija["termin"] == sifra_termina and
            rezervacija["mesto"] == mesto
        ):
            rezervacija_za_brisanje = rezervacija
            break

    if rezervacija_za_brisanje:
        rezervacije.remove(rezervacija_za_brisanje)
        sacuvaj_rezervacije(rezervacije)
        print(f"Rezervacija za mesto {mesto}, termin {sifra_termina} uspešno poništena.")
    else:
        print("Rezervacija sa unetim podacima nije pronađena.")


def pregled_rezervisanih_mesta():

    korisnicko_ime = prijavljeni_korisnik.prijavljeni_korisnik
    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()

    korisnicke_rezervacije = [
        rez for rez in rezervacije if rez["korisnicko_ime"] == korisnicko_ime
    ]

    if not korisnicke_rezervacije:
        print(f"Korisnik {korisnicko_ime} nema rezervisanih mesta.")
        return

    print(f"\nRezervisana mesta za korisnika {korisnicko_ime}:")
    print("{:<12} | {:<8} | {:<12} | {:<10} | {:<10} | {:<5}".format("Termin", "Mesto", "Datum", "Početak", "Kraj","Sala"))
    print("-" *70)
    for rez in korisnicke_rezervacije:
        termin = rez["termin"]
        mesto = rez["mesto"]
        datum = termini.get(termin, {}).get("datum")

        sifra_treninga = termin[:4]
        trening = treninzi.get(sifra_treninga, {})
        vreme_pocetka = trening.get("vreme_pocetka")
        vreme_kraja = trening.get("vreme_kraja")
        sala = trening.get("sala", "")
        print("{:<12} | {:<8} | {:<12} | {:<10} | {:<10} | {:<5}".format(
            termin, mesto, datum, vreme_pocetka, vreme_kraja,sala
        ))

    print("-" * 70)


def izmeni_rezervaciju():

    rezervacije = ucitaj_rezervacije() or []
    recnik_termina = ucitaj_termine_treninga()
    recnik_treninga = ucitaj_treninge()
    recnik_sala = ucitaj_sale()

    sifra_termina = input("Unesite šifru termina: ").strip()
    korisnicko_ime = input("Unesite korisničko ime: ").strip()
    oznaka_mesta = input("Unesite oznaku mesta (npr. 1A): ").strip()

    rezervacija = next(
        (rez for rez in rezervacije if rez["termin"] == sifra_termina and rez["korisnicko_ime"] == korisnicko_ime and rez["mesto"] == oznaka_mesta),
        None
    )

    if not rezervacija:
        print("Rezervacija nije pronađena.")
        return

    print("Pronađena rezervacija:")
    print(f"Korisničko ime: {rezervacija['korisnicko_ime']}, Termin: {rezervacija['termin']}, Mesto: {rezervacija['mesto']}, Datum: {rezervacija['datum']}")

    nova_sifra_termina = input("Unesite novu šifru termina (pritisnite Enter za bez izmene): ").strip() or rezervacija["termin"]
    novi_korisnicko_ime = input("Unesite novo korisničko ime (pritisnite Enter za bez izmene): ").strip() or rezervacija["korisnicko_ime"]
    novo_mesto = input("Unesite novu oznaku mesta (pritisnite Enter za bez izmene): ").strip() or rezervacija["mesto"]

    if nova_sifra_termina != rezervacija["termin"]:
        if nova_sifra_termina not in recnik_termina:
            print("Uneli ste nepostojeću šifru termina.")
            return

    sifra_treninga = recnik_termina[nova_sifra_termina]["trening"]

    if sifra_treninga not in recnik_treninga:
        print("Trening povezan s terminom nije pronađen.")
        return

    sifra_sale = recnik_treninga[sifra_treninga]["sala"]

    if novo_mesto != rezervacija["mesto"]:
        if sifra_sale not in recnik_sala:
            print("Sala za novi termin nije pronađena.")
            return

        sala = recnik_sala[sifra_sale]

        red = novo_mesto[:-1]
        kolona = novo_mesto[-1]

        if not red.isdigit() or int(red) > sala["broj_redova"]:
            print("Uneli ste nepostojeći red.")
            return

        if kolona not in sala["mesta"]:
            print("Uneli ste nepostojeću kolonu.")
            return


        if any(
            rez["termin"] == nova_sifra_termina and rez["mesto"] == novo_mesto
            for rez in rezervacije
        ):
            print("Novo mesto je već rezervisano za taj termin.")
            return

    rezervacija["termin"] = nova_sifra_termina
    rezervacija["korisnicko_ime"] = novi_korisnicko_ime
    rezervacija["mesto"] = novo_mesto

    sacuvaj_rezervacije(rezervacije)
    print("Rezervacija je uspešno izmenjena!")


def pregled_instruktorovih_rezervacija():

    korisnici = login_logout_signin.ucitaj_korisnike()
    treninzi = ucitaj_treninge()
    programi = ucitaj_programe_treninga()
    termini = ucitaj_termine_treninga()
    rezervacije = ucitaj_rezervacije()

    ulogovani = prijavljeni_korisnik.prijavljeni_korisnik
    if ulogovani not in korisnici:
        print("Greška: ulogovani korisnik nije pronađen.")
        return

    ime_instruktora = korisnici[ulogovani]["ime"]
    prezime_instruktora = korisnici[ulogovani]["prezime"]
    puno_ime = f"{ime_instruktora} {prezime_instruktora}" #odavde treba proveriti instruktora, moglo je i preko korisnickog imena ali nisam menjala

    relevantne_rezervacije = []

    for rez in rezervacije:
        sifra_termina = rez["termin"]
        sifra_treninga = sifra_termina[:4]

        if sifra_treninga not in treninzi:
            continue

        trening = treninzi[sifra_treninga]
        naziv_programa = trening["program"]

        if naziv_programa not in programi:
            continue

        instruktori_programa = programi[naziv_programa]["instruktori"]
        lista_instruktora = [i.strip() for i in instruktori_programa]

        if puno_ime not in lista_instruktora:
            continue

        if sifra_termina not in termini:
            continue

        termin = termini[sifra_termina]
        vreme_pocetka = trening["vreme_pocetka"]
        vreme_kraja = trening["vreme_kraja"]

        korisnicko_ime_clana = rez["korisnicko_ime"]
        if korisnicko_ime_clana not in korisnici:
            continue

        ime_clana = korisnici[korisnicko_ime_clana]["ime"]
        prezime_clana = korisnici[korisnicko_ime_clana]["prezime"]
        datum = rez["datum"]
        mesto = rez["mesto"]

        relevantne_rezervacije.append({
            "termin": sifra_termina,
            "ime": ime_clana,
            "prezime": prezime_clana,
            "korisnicko_ime": korisnicko_ime_clana,
            "program": naziv_programa,
            "datum": datum,
            "vreme_pocetka": vreme_pocetka,
            "vreme_kraja": vreme_kraja,
            "mesto": mesto
        })

    if not relevantne_rezervacije:
        print("Nemate nijednu rezervaciju za svoje termine.")
        return

    print(f"\nRezervacije termina koje vodi instruktor {puno_ime}:")
    print("-" * 90)
    print("{:<10} {:<12} {:<12} {:<15} {:<10} {:<10} {:<10} {:<6}".format(
        "Termin", "Ime", "Prezime", "Korisničko ime", "Program", "Datum", "Početak", "Mesto"
    ))
    print("-" * 90)

    for r in relevantne_rezervacije:
        print("{:<10} {:<12} {:<12} {:<15} {:<10} {:<10} {:<10} {:<6}".format(
            r["termin"], r["ime"], r["prezime"], r["korisnicko_ime"],
            r["program"], r["datum"], r["vreme_pocetka"], r["mesto"]
        ))
    print("-" * 90)


def ponisti_rezervaciju_instruktor():

    korisnicko_ime_instruktora = prijavljeni_korisnik.prijavljeni_korisnik
    korisnici = login_logout_signin.ucitaj_korisnike()
    rezervacije = ucitaj_rezervacije()
    termini = ucitaj_termine_treninga()
    treninzi = ucitaj_treninge()
    programi = ucitaj_programe_treninga()

    if korisnicko_ime_instruktora not in korisnici:
        print("Greška: Instruktor nije pronađen.")
        return

    ime_instruktora = korisnici[korisnicko_ime_instruktora]["ime"].lower()
    prezime_instruktora = korisnici[korisnicko_ime_instruktora]["prezime"].lower()

    while True:
        korisnicko_ime_clana = input("Unesite korisničko ime člana čiju rezervaciju brišete: ").strip()
        sifra_termina = input("Unesite šifru termina: ").strip()
        mesto = input("Unesite oznaku mesta (npr. 1A): ").strip()

        rezervacija_za_brisanje = None

        for rez in rezervacije:
            if (
                rez["korisnicko_ime"] == korisnicko_ime_clana and
                rez["termin"] == sifra_termina and
                rez["mesto"] == mesto
            ):
                sifra_treninga = sifra_termina[:4]
                trening = treninzi.get(sifra_treninga)
                if trening:
                    program_naziv = trening["program"]
                    program = programi.get(program_naziv)
                    if program:
                        instruktori = [i.strip().lower() for i in program["instruktori"]]
                        if f"{ime_instruktora} {prezime_instruktora}" in instruktori:
                            rezervacija_za_brisanje = rez
                            break

        if rezervacija_za_brisanje:
            rezervacije.remove(rezervacija_za_brisanje)
            sacuvaj_rezervacije(rezervacije)
            print("Rezervacija je uspešno poništena.")
        else:
            print("Nije pronađena rezervacija koju imate pravo da obrišete.")

        jos = input("Da li želite da obrišete još neku rezervaciju? (da/ne): ").strip().lower()
        if jos != "da":
            break


def rezervisi_mesto_instruktor():

    korisnicko_ime_instruktora = prijavljeni_korisnik.prijavljeni_korisnik
    korisnici = login_logout_signin.ucitaj_korisnike()
    recnik_sala = ucitaj_sale()
    recnik_termina = ucitaj_termine_treninga()
    recnik_treninga = ucitaj_treninge()
    recnik_programa = ucitaj_programe_treninga()
    rezervacije = ucitaj_rezervacije() or []

    if korisnicko_ime_instruktora not in korisnici:
        print("Greška: Instruktor nije pronađen.")
        return

    ime_instruktora = korisnici[korisnicko_ime_instruktora]["ime"].strip().lower()
    prezime_instruktora = korisnici[korisnicko_ime_instruktora]["prezime"].strip().lower()
    puno_ime_instruktora = f"{ime_instruktora} {prezime_instruktora}"

    korisnicko_ime_clana = input("Unesite korisničko ime člana za kog pravite rezervaciju: ").strip()
    if korisnicko_ime_clana not in korisnici:
        print("Član sa datim korisničkim imenom ne postoji.")
        return

    clan_info = korisnici[korisnicko_ime_clana]
    status_clana = clan_info.get("status", "").lower()
    paket_clana = clan_info.get("paket", "").lower()

    if status_clana != "aktivan":
        print("Rezervacija nije moguća. Član nije aktivan.")
        return

    sifra_termina = input("Unesite šifru termina: ").strip()
    if sifra_termina not in recnik_termina:
        print("Termin nije pronađen.")
        return

    sifra_treninga = sifra_termina[:4]
    trening = recnik_treninga.get(sifra_treninga)
    if not trening:
        print("Trening nije pronađen.")
        return

    naziv_programa = trening["program"]
    program = recnik_programa.get(naziv_programa)
    if not program:
        print("Program treninga nije pronađen.")
        return

    instruktori_programa = [i.strip().lower() for i in program["instruktori"]]
    if puno_ime_instruktora not in instruktori_programa:
        print("Nemate dozvolu da pravite rezervaciju za ovaj termin.")
        return

    potrebni_paket = program.get("paket", "standard").lower()
    if paket_clana == "standard" and potrebni_paket == "premium":
        print("Rezervacija nije moguća. Član sa 'standard' paketom ne može pristupiti 'premium' programu.")
        return

    sifra_sale = trening["sala"]
    sala = recnik_sala.get(sifra_sale)
    if not sala:
        print("Sala nije pronađena.")
        return

    danasnji_datum = datetime.now().strftime("%d.%m.%Y.")
    matricni_prikaz(sifra_sale, sifra_termina)

    while True:
        odabrano_mesto = input("Unesite oznaku mesta za rezervaciju (npr. 1A): ").strip()
        red = odabrano_mesto[:-1]
        kolona = odabrano_mesto[-1]

        if not red.isdigit() or int(red) > sala["broj_redova"]:
            print("Uneli ste nepostojeći red.")
            continue

        if kolona not in sala["mesta"]:
            print("Uneli ste nepostojeću kolonu.")
            continue

        if any(
            rez['mesto'] == odabrano_mesto and rez['termin'] == sifra_termina
            for rez in rezervacije
        ):
            print("Odabrano mesto je već rezervisano za ovaj termin.")
            continue

        rezervacije.append({
            "korisnicko_ime": korisnicko_ime_clana,
            "termin": sifra_termina,
            "mesto": odabrano_mesto,
            "datum": danasnji_datum
        })

        sacuvaj_rezervacije(rezervacije)
        print(f"Mesto {odabrano_mesto} je uspešno rezervisano za {korisnicko_ime_clana} u terminu {sifra_termina} ({danasnji_datum}).")
        break

    jos_mesta = input("Da li želite da rezervišete još mesta za ovog ili drugog člana? (da/ne): ").strip().lower()
    if jos_mesta == "da":
        rezervisi_mesto_instruktor()


def pretraga_instruktorskih_rezervacija():

    rezervacije = ucitaj_rezervacije()
    korisnici = login_logout_signin.ucitaj_korisnike()
    treninzi = ucitaj_treninge()
    termini = ucitaj_termine_treninga()

    if not rezervacije:
        print("Nema rezervacija za pretragu.")
        return

    kriterijumi = {
        "1": "Šifra treninga",
        "2": "Ime člana",
        "3": "Prezime člana",
        "4": "Datum"
    }

    print("\nDostupni kriterijumi za pretragu:")
    for key, value in kriterijumi.items():
        print(f"{key}. {value}")

    izbor = input("\nUnesite brojeve kriterijuma koje želite da koristite (odvojene razmakom): ").split()
    odabrani = set(k for k in izbor if k in kriterijumi)

    if not odabrani:
        print("Niste odabrali nijedan validan kriterijum.")
        return

    print("\nUnesite vrednosti za izabrane kriterijume:")
    sifra_treninga = ime = prezime = datum = None

    if "1" in odabrani:
        sifra_treninga = input("Šifra treninga: ").strip().lower()
    if "2" in odabrani:
        ime = input("Ime člana: ").strip().lower()
    if "3" in odabrani:
        prezime = input("Prezime člana: ").strip().lower()
    if "4" in odabrani:
        datum = input("Datum (dd.mm.gggg.): ").strip()

    rezultati = []

    for rez in rezervacije:
        termin_sifra = rez["termin"]
        korisnicko_ime = rez["korisnicko_ime"]
        clan = korisnici.get(korisnicko_ime, {})
        datum_r = rez["datum"]

        sifra_tr = termin_sifra[:4]

        if (
            (sifra_treninga and sifra_treninga != sifra_tr.lower()) or
            (ime and clan.get("ime", "").lower() != ime) or
            (prezime and clan.get("prezime", "").lower() != prezime) or
            (datum and datum != datum_r)
        ):
            continue

        rezultati.append({
            "termin": termin_sifra,
            "korisnicko_ime": korisnicko_ime,
            "ime": clan.get("ime", "Nepoznato"),
            "prezime": clan.get("prezime", "Nepoznato"),
            "datum": datum_r,
            "mesto": rez["mesto"]
        })

    if not rezultati:
        print("\nNema rezultata za zadate kriterijume.")
        return

    print("\nRezultati pretrage rezervacija:")
    print("{:<10} | {:<10} | {:<10} | {:<15} | {:<12} | {:<5}".format(
        "Termin", "Ime", "Prezime", "Korisničko ime", "Datum", "Mesto"
    ))
    print("-" * 70)

    for r in rezultati:
        print("{:<10} | {:<10} | {:<10} | {:<15} | {:<12} | {:<5}".format(
            r["termin"], r["ime"], r["prezime"], r["korisnicko_ime"],
            r["datum"], r["mesto"]
        ))

if __name__ == "__main__":
    rezervisi_mesto()
