from datetime import datetime, timedelta
import login_logout_signin
from sale import *
from login_logout_signin import *

def dodela_nagrada_lojalnosti():

    rezervacije = ucitaj_rezervacije()
    korisnici = login_logout_signin.ucitaj_korisnike()

    danas = datetime.now()
    if danas.day != 1:
        print("Ova funkcija se može pokrenuti samo prvog dana u mesecu.")
        return

    granica_dana = danas - timedelta(days=30)

    broj_rezervacija = {} #recnik prati br rezervacija svakog korisnika
    for rez in rezervacije:
        datum_str = rez["datum"].strip()
        try:
            datum_rez = datetime.strptime(datum_str, "%d.%m.%Y.") #proveravam datum
        except ValueError:
            continue

        if datum_rez >= granica_dana:
            korisnik = rez["korisnicko_ime"] #ako je u opsegu
            if korisnik not in broj_rezervacija:
                broj_rezervacija[korisnik] = 0
            broj_rezervacija[korisnik] += 1


    nagradjeni = []
    for korisnicko_ime, broj in broj_rezervacija.items():
        if broj > 27 and korisnicko_ime in korisnici: #ako ima vise od 27 onda ga aktiviraj
            korisnici[korisnicko_ime]["paket"] = "premium"
            korisnici[korisnicko_ime]["status"] = "aktivan"
            korisnici[korisnicko_ime]["datum"] = danas.strftime("%d.%m.%Y.")
            korisnici[korisnicko_ime]["isticanje"] = (danas + timedelta(days=30)).strftime("%d.%m.%Y.")
            nagradjeni.append(korisnicko_ime)

    if not nagradjeni:
        print("Nijedan korisnik nije ispunio uslov za nagradu lojalnosti.")
        return


    login_logout_signin.sacuvaj_korisnike(korisnici)




if __name__ == "__main__":
    dodela_nagrada_lojalnosti()