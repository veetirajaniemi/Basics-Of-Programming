######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Veeti Rajaniemi
# Opiskelijanumero: 0599190
# Päivämäärä: 12.11.2021 
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# HARJOITUSTYÖ PERUSTASO

# eof

import HTPerusKirjasto



def Valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    
    valinta = int(input("Valintasi: "))
    return valinta

def paaohjelma():
    kaikkitiedot = []
    analyysi = []

    while True:
        toiminto = Valikko()

        if (toiminto == 1):
            x = input("Anna luettavan tiedoston nimi: ")
            HTPerusKirjasto.TiedostoLuku(x, kaikkitiedot) #"kaikkitiedot" sisältää oliot
            print()
            print("Anna uusi valinta.")

        elif (toiminto == 2):
            if (kaikkitiedot == []):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
                print()
                print("Anna uusi valinta.")
            else: 
                HTPerusKirjasto.Analysoija(kaikkitiedot, analyysi) #listassa 'analyysi' olioina tehtävä + lkm
                tulokset = HTPerusKirjasto.Tulokset(analyysi) #oliossa 'tulos' tiedot
                print()
                print("Anna uusi valinta.")

        elif (toiminto == 3):
            if (kaikkitiedot == []):
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
                print()
                print("Anna uusi valinta.")
            else:
                y = input("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.Tallentaja(y, analyysi, tulokset)
                print()
                print("Anna uusi valinta.")

        elif (toiminto == 0):
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
            print("Anna uusi valinta.")

    print("Kiitos ohjelman käytöstä.")

    return None
            
            
            
paaohjelma()
