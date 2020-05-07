def uvozi_place(ime_datoteke):
    
    # datoteka je zakodirana s cp1250
    f = open(ime_datoteke, encoding='cp1250')
    
    # prve tri vrstice vržemo proč
    f.readline()
    f.readline()
    f.readline()
    
    # prazni seznami
    mesci_javni = []
    zneski_javni = []
    mesci_zasebni = []
    zneski_zasebni = []
    
    for vrstica in f:
        # razbijmo vrstico na seznam s podatki
        seznam = vrstica.strip().split("\t")
        # razpakirajmo seznam
        mesec, sektor, bruto, neto = seznam
    
        # odstranimo dvojne navednice
        mesec = mesec.replace('"','')
        sektor = sektor.replace('"','')
    
        # zneske pretvorimo v števila
        bruto = float(bruto)
        neto = float(neto)
    
        # na podlagi sektorja podatke dodamo v seznama
        if sektor.startswith("Javni"):
            mesci_javni.append(mesec)
            zneski_javni.append(bruto)
        else:
            mesci_zasebni.append(mesec)
            zneski_zasebni.append(bruto)
    # podatki so zdaj pripravljeni
    return mesci_javni, zneski_javni, mesci_zasebni, zneski_zasebni
