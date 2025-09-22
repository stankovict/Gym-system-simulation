import instruktor
import sale
from instruktor import *
from admini import *
from izvestaji import *
import prijavljeni_korisnik

def main_menu():

    korisnici = ucitaj_korisnike()
    automatska_deaktivacija(korisnici)


    while True:
        print("\nGlavni Meni")
        print("---------------")
        print("1. Prijava na sistem")
        print("2. Pregled dostupnih programa treninga")
        print("3. Pretraga programa treninga")
        print("4. Višekriterijumska pretraga programa treninga")
        print("5. Pretraga termina treninga")
        print("6. Registracija")
        print("x. Izlazak iz aplikacije")

        choice = input(">> ")

        if choice == '1':
            prijava()
        elif choice.lower() == 'x':
            print("Izlazak iz aplikacije...")
            break
        elif choice == '2':
            programi = ucitaj_programe_treninga()
            ispis_programa(programi)
            detaljno_programi(programi)
        elif choice == '3':
            programi = ucitaj_programe_treninga()
            pretraga_programa_treninga(programi)
        elif choice == '4':
            programi = ucitaj_programe_treninga()
            visekriterijumska_pretraga_programa(programi)
        elif choice == '5':
            recnik_termina = ucitaj_termine_treninga()
            recnik_treninga = ucitaj_treninge()
            pretrazi_termine(recnik_termina, recnik_treninga)
        elif choice == '6':
            registracija()
        else:
            print("Nevažeći izbor, pokušajte ponovo.")


def user_menu():

    while True:
        print("\nKorisnički Meni")
        print("------------------")
        print("1. Pregled dostupnih programa treninga")
        print("2. Pretraga programa treninga")
        print("3. Višekriterijumska pretraga programa treninga")
        print("4. Pretraga termina treninga")
        print("5. Rezervacija mesta")
        print("6. Pregled rezervisanih mesta")
        print("7. Poništavanje rezervacije")
        print("x. Odjava sa sistema")

        choice = input(">> ")

        if choice == '1':
            programi = ucitaj_programe_treninga()
            ispis_programa(programi)
            detaljno_programi(programi)
        elif choice.lower() == 'x':
            prijavljeni_korisnik.prijavljeni_korisnik = None
            print("Odjava...")
            break
        elif choice == '2':
            programi = ucitaj_programe_treninga()
            pretraga_programa_treninga(programi)
        elif choice == '3':
            programi = ucitaj_programe_treninga()
            visekriterijumska_pretraga_programa(programi)
        elif choice == '4':
            recnik_termina = ucitaj_termine_treninga()
            recnik_treninga = ucitaj_treninge()
            pretrazi_termine(recnik_termina, recnik_treninga)
        elif choice == '5':
            sale.rezervisi_mesto()
        elif choice == '6':
            sale.pregled_rezervisanih_mesta()
        elif choice == '7':
            sale.ponisti_rezervaciju()
        else:
            print("Nevažeći izbor, pokušajte ponovo.")


def admin_menu():

    while True:
        print("\nAdministratorski Meni")
        print("------------------------")
        print("1. Unos, izmena i brisanje programa treninga")
        print("2. Unos, izmena i brisanje treninga")
        print("3. Registracija novog instruktora")
        print("4. Pregled dostupnih programa treninga")
        print("5. Pretraga programa treninga")
        print("6. Višekriterijumska pretraga programa treninga")
        print("7. Pretraga termina treninga")
        print("8. Mesečna nagrada lojalnosti")
        print("9. Izveštavanje")
        print("x. Odjava sa sistema")

        choice = input(">> ")

        if choice == '1':
            while True:
                print("\nIzmena programa treninga")
                print("------------------")
                print("1. Unos novog programa treninga")
                print("2. Izmena postojećeg programa treninga")
                print("3. Brisanje postojećeg programa treninga")
                print("4. Dodavanje dužeg opisa za program treninga")
                print("x. Nazad")

                choice1 = input(">> ")
                if choice1 == '1':
                    programi = ucitaj_programe_treninga()
                    unos_programa_treninga(programi)
                    sacuvaj_programe_treninga(programi)
                elif choice1 == '2':
                    programi = ucitaj_programe_treninga()
                    izmena_programa_treninga(programi)
                    sacuvaj_programe_treninga(programi)
                elif choice1=='3':
                    programi = ucitaj_programe_treninga()
                    brisanje_programa_treninga(programi)
                    sacuvaj_programe_treninga(programi)
                elif choice1=='4':
                    programi = ucitaj_programe_treninga()
                    dodaj_opis_programa(programi)
                elif choice1 == 'x':
                    break


        elif choice == '2':
            while True:
                print("\nIzmena treninga")
                print("------------------")
                print("1. Unos novog treninga")
                print("2. Izmena postojećeg treninga")
                print("3. Brisanje postojećeg treninga")
                print("x. Nazad")

                choice2 = input(">> ")
                if choice2 == '1':
                    treninzi = ucitaj_treninge()
                    unos_treninga(treninzi)
                    sacuvaj_treninge(treninzi)
                elif choice2 == '2':
                    treninzi = ucitaj_treninge()
                    izmena_treninga(treninzi)
                    sacuvaj_treninge(treninzi)
                elif choice2=='3':
                    treninzi = ucitaj_treninge()
                    brisanje_treninga(treninzi)
                    sacuvaj_treninge(treninzi)
                elif choice2 == 'x':
                    break
        elif choice == '3':
            login_logout_signin.registracija_instruktor()

        elif choice == '4':
            programi = ucitaj_programe_treninga()
            ispis_programa(programi)
            detaljno_programi(programi)
        elif choice == '5':
            programi = ucitaj_programe_treninga()
            pretraga_programa_treninga(programi)
        elif choice == '6':
            programi = ucitaj_programe_treninga()
            visekriterijumska_pretraga_programa(programi)
        elif choice == '7':
            recnik_termina = ucitaj_termine_treninga()
            recnik_treninga = ucitaj_treninge()
            pretrazi_termine(recnik_termina, recnik_treninga)
        elif choice == '8':
            dodela_nagrada_lojalnosti()
        elif choice == '9':
            while True:
                print("\nIzveštavanje")
                print("------------------")
                print("1. Lista rezervacija za odabran datum rezervacije")
                print("2. Lista rezervacija za odabran datum termina treninga")
                print("3. Lista rezervacija za odabran datum rezervacije i odabranog instruktora")
                print("4. Ukupan broj rezervacija za izabran dan (u nedelji) održavanja treninga")
                print("5. Ukupan broj rezervacije po instruktorima (za svakog instruktora) u poslednjih 30 dana. Sortirati prikazane instruktore po ukupnom broju ostvarenih rezervacija u njihovim terminima treninga")
                print("6. Ukupan broj rezervacija realizovanih u terminima treninga za koje je potreban premium paket članstva kao i ukupan broj rezervacija realizovanih u terminima treninga za koje je potreban standardni paket članstva, u poslednjih 30 dana")
                print("7. Najpopularniji programi treninga. Pronaći najpopularnija 3 programa treninga po broju rezervacija izvršenih u poslednjih godinu dana.")
                print("8. Najpopularniji dan u nedelji. Utvrditi za koji dan u nedelji održavanja termina treninga je izvršeno najviše rezervacija")
                print("x. Nazad")

                choice3 = input(">> ")
                if choice3 == '1':
                    izvestaj_a()
                elif choice3 == '2':
                    izvestaj_b()
                elif choice3 == '3':
                    izvestaj_c()
                elif choice3 == '4':
                    izvestaj_d()
                elif choice3 == '5':
                    izvestaj_e()
                elif choice3 == '6':
                    izvestaj_f()
                elif choice3 == '7':
                    izvestaj_g()
                elif choice3 == '8':
                    izvestaj_h()
                elif choice3 == 'x':
                    break
        elif choice.lower() == 'x':
            prijavljeni_korisnik.prijavljeni_korisnik = None
            print("Odjava...")
            break
        else:
            print("Nevažeći izbor, pokušajte ponovo.")


def trener_menu():

    while True:
        print("\nInstruktorski Meni")
        print("---------------------")
        print("1. Aktivacija statusa člana")
        print("2. Aktivacija premium paketa članstva")
        print("3. Pregled dostupnih programa treninga")
        print("4. Pretraga programa treninga")
        print("5. Višekriterijumska pretraga programa treninga")
        print("6. Pretraga termina treninga")
        print("7. Izmeni rezervaciju")
        print("8. Pregled rezervacija")
        print("9. Poništi rezervaciju")
        print("10. Pretraži rezervaciju")
        print("11. Napravi rezervaciju")
        print("x. Odjava sa sistema")

        choice = input(">> ")

        if choice == '1':
            print("1. Prikaži trenutno neaktivne članove")
            print("2. Aktiviraj status člana")
            print("3. Nazad")
            choice = input(">> ")

            if choice == '1':
                korisnici = login_logout_signin.ucitaj_korisnike()
                instruktor.deaktivirani_korisnici(korisnici)
                login_logout_signin.sacuvaj_korisnike(korisnici)
            elif choice == '2':
                korisnici = login_logout_signin.ucitaj_korisnike()
                instruktor.aktiviraj_clana(korisnici)
                login_logout_signin.sacuvaj_korisnike(korisnici)
            elif choice.lower() == 'x':
                break
            else:
                print("Neispravan unos. Pokušaj ponovo.")
        elif choice == '2':
            korisnici = login_logout_signin.ucitaj_korisnike()
            instruktor.aktiviraj_premium_paket(korisnici)
            login_logout_signin.sacuvaj_korisnike(korisnici)
        elif choice == '3':
            programi = ucitaj_programe_treninga()
            ispis_programa(programi)
            detaljno_programi(programi)
        elif choice == '4':
            programi = ucitaj_programe_treninga()
            pretraga_programa_treninga(programi)
        elif choice == '5':
            programi = ucitaj_programe_treninga()
            visekriterijumska_pretraga_programa(programi)
        elif choice == '6':
            recnik_termina = ucitaj_termine_treninga()
            recnik_treninga = ucitaj_treninge()
            pretrazi_termine(recnik_termina, recnik_treninga)
        elif choice == '7':
            izmeni_rezervaciju()
        elif choice == '8':
            pregled_instruktorovih_rezervacija()
        elif choice == '9':
            ponisti_rezervaciju_instruktor()
        elif choice == '10':
            pretraga_instruktorskih_rezervacija()
        elif choice == '11':
            rezervisi_mesto_instruktor()
        elif choice.lower() == 'x':
            prijavljeni_korisnik.prijavljeni_korisnik = None
            print("Izlazak iz aplikacije...")
            break
        else:
            print("Nevažeći izbor, pokušajte ponovo.")

if __name__ == "__main__":
    main_menu()