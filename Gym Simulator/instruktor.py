from datetime import datetime, timedelta
from login_logout_signin import *

def deaktivirani_korisnici(korisnici):

    nadjen = False
    print("Korisnici koji su trenutno 'neaktivni':")
    for korisnicko_ime, podaci in korisnici.items():
        if korisnici[korisnicko_ime]["status"] == "neaktivan" and korisnici[korisnicko_ime]["uloga"] == "registrovan član":
            nadjen = True
            print(f"Korsinik {korisnicko_ime} je neaktivan.")
    if not nadjen:
        print("Svi korisnici su trenutno aktivni.")
    if nadjen:
        izbor = input("Da li želite da aktivirate nekog korisnika (da/ne): ")
        if izbor.lower() == 'da':
            aktiviraj_clana(korisnici)
        elif izbor.lower() == 'ne':
            print("Povratak na glavni meni.")


def aktiviraj_clana(korisnici):

    korisnicko_ime = input("Unesite korisničko ime člana za aktivaciju: ").strip()

    if korisnicko_ime not in korisnici:
        print("Ne postoji korisnik sa unetim korisničkim imenom.")
        return
    if korisnici[korisnicko_ime]["status"] == "aktivan":
        print("Član je već aktivan.")
        return

    korisnici[korisnicko_ime]["status"] = "aktivan"
    korisnici[korisnicko_ime]["datum"] = datetime.now().strftime("%d.%m.%Y.")
    danas = datetime.now()
    isticanje_datum = danas + timedelta(days=30) #postavljanje nove granice aktivnosti
    formatiran_isticanje = isticanje_datum.strftime("%d.%m.%Y.")
    korisnici[korisnicko_ime]["isticanje"] = formatiran_isticanje
    print(f"Status člana '{korisnicko_ime}' je uspešno aktiviran!")
    sacuvaj_korisnike(korisnici)


def automatska_deaktivacija(korisnici):

    danas = datetime.now()
    for korisnicko_ime, podaci in korisnici.items():
        isticanje = datetime.strptime(podaci["isticanje"], "%d.%m.%Y.")
        if danas > isticanje and korisnici[korisnicko_ime]["uloga"] == "registrovan član":
            korisnici[korisnicko_ime]["status"] = "neaktivan"

    sacuvaj_korisnike(korisnici)


def aktiviraj_premium_paket(korisnici):

    korisnicko_ime = input("Unesite korisničko ime: ")
    if korisnicko_ime not in korisnici:
        print("Korisnik sa unetim korisničkim imenom ne postoji.")
        return

    korisnik = korisnici[korisnicko_ime]
    if korisnik["status"] != "aktivan":
        print(f"Korisnik {korisnicko_ime} nema aktivan status. Ne možete aktivirati premium paket.")
        return

    datum_aktivacije = korisnik["datum"]
    datum_isteka = datetime.strptime(datum_aktivacije, "%d.%m.%Y.") + timedelta(days=30)
    danasnji_datum = datetime.now()

    if danasnji_datum > datum_isteka:
        print(f"Korisniku {korisnicko_ime} je isteklo aktivno članstvo.")
        return

    korisnik["paket"] = "premium"
    print(f"Premium paket za korisnika {korisnicko_ime} je aktiviran do {datum_isteka.strftime("%d.%m.%Y.")}.")




if __name__ == "__main__":
    pass