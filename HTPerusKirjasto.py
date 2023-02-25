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
# HTPerusKirjasto

import sys

class TIETO:
    tehtava = ""
    lkm = ""

class TULOS:
    palautusmaara = ""
    tehtavamaara = ""
    keskiarvo = ""
    enitentehty = ""
    eniten = ""
    vahitentehty = ""
    vahiten = ""
    

def TiedostoLuku(nimi, lista):
    try:
        tiedosto = open(nimi, "r", encoding = "utf-8")
        tiedosto.readline() #1. rivi (otsikko)
        n = 0

        while True:
            tieto = TIETO()
            y = tiedosto.readline()
            rivi = y[:-1]

            if (rivi == ""):
                break
            
            x = rivi.split(";")
            tieto.tehtava = x[2]
            lista.append(tieto)

            n = n + 1
            x.clear() #tyhjennetään rivilista

        print("Tiedostosta '{0:s}' luettiin listaan".format(nimi), end = " ")
        print(n, "datarivin tiedot.")
        

        tiedosto.close()

    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)


    return None

def Analysoija(lista, uusilista):

    uusilista.clear()
    #len uusilista on nolla!
    
    for i in lista:
        if (len(uusilista) == 0):
            i.lkm = 1
            uusilista.append(i)
            n = 1 # n on näiden määrä!

        elif (uusilista[len(uusilista) - 1].tehtava != i.tehtava): #eri ku edelline
            i.lkm = 1
            uusilista.append(i)
            n = 1

        else: #kun sama kuin edellinen
            n = n + 1
            uusilista[len(uusilista) - 1].lkm = n #edellinen lkm + 1

    print("Analysoitu", len(lista), "palautusta", len(uusilista), "eri tehtävään.")

    
    return uusilista
            

def Tulokset(lista):
    tulos = TULOS()

    # MÄÄRÄT
    
    maara = 0
    for i in lista:
        maara = maara + i.lkm
    tulos.palautusmaara = maara #palautuksia yhteensä

    x = len(lista)  # tehtäviä yhteensä
    tulos.tehtavamaara = x

    y = maara / x
    keskiarvo = int(y)
    tulos.keskiarvo = keskiarvo

    # ENITEN TEHTY
    
    n = 0
    for i in lista:
        if (i.lkm > n):
            n = i.lkm
            eniten = i.tehtava #tätä tehtävää tehty eniten
    
    tulos.enitentehty = eniten
    tulos.eniten = n

    # VÄHITEN TEHTY
    
    z = lista[0].lkm + 1 #nyt z isompi kun listan 1. olevan tehtävän tekomäärä

    for i in lista:
        if (i.lkm < z):
            z = i.lkm
            vahiten = i.tehtava #tätä tehtävää tehty vähiten
     
    tulos.vahitentehty = vahiten
    tulos.vahiten = z

    print("Tilastotiedot analysoitu.")
    

    return tulos


def Tallentaja(nimi, lista, tulos):

    try:
        tiedosto = open(nimi, "w", encoding = "utf-8")

        
        print("Palautuksia tuli yhteensä", str(tulos.palautusmaara) + ",", end = " ")
        print(tulos.tehtavamaara, "eri tehtävään.")
        print("Viikkotehtäviin tuli keskimäärin", tulos.keskiarvo, "palautusta.")
        print("Eniten palautuksia,", str(tulos.eniten) +  ", tuli viikkotehtävään", end = " ")
        print(tulos.enitentehty + ".")
        print("Vähiten palautuksia,", str(tulos.vahiten) + ", tuli viikkotehtävään", end = " ")
        print(str(tulos.vahitentehty) + ".")
        print()

        print("Tehtävä;Lukumäärä")
        for i in lista:
            print(i.tehtava + ";" + str(i.lkm))
        print("Tulokset tallennettu tiedostoon '{0:s}'.".format(nimi))

        tiedosto.write("Palautuksia tuli yhteensä " + str(tulos.palautusmaara) + ", ")
        tiedosto.write(str(tulos.tehtavamaara) + " eri tehtävään.\n")
        tiedosto.write("Viikkotehtäviin tuli keskimäärin " + str(tulos.keskiarvo) + " palautusta.\n")
        tiedosto.write("Eniten palautuksia, " + str(tulos.eniten) +  ", tuli viikkotehtävään ")
        tiedosto.write(tulos.enitentehty + ".\n")
        tiedosto.write("Vähiten palautuksia, " + str(tulos.vahiten) + ", tuli viikkotehtävään ")
        tiedosto.write(str(tulos.vahitentehty) + "." + "\n\n")
        tiedosto.write("Tehtävä;Lukumäärä\n")

        for i in lista:
            tiedosto.write(i.tehtava + ";" + str(i.lkm) + "\n")

        tiedosto.close()

    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(nimi))
        sys.exit(0)   

    return None
        
        
    
    
        
