def uvozi_place(ime_datoteke):
    
    # datoteka je zakodirana s cp1250
    f = open(ime_datoteke, encoding='cp1250')
    
    # prve tri vrstice vržemo proč
    f.readline()
    f.readline()
    f.readline()
    
    # prazen slovar
    place = {}
    
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

        if sektor not in place: # če sektorja še ni
            place[sektor] = {'mesec':[], 'neto':[], 'bruto':[]}

        # dodamo podatke v ustrezen slovar
        place[sektor]['mesec'].append(mesec)
        place[sektor]['neto'].append(neto)
        place[sektor]['bruto'].append(bruto)
        
    # podatki so zdaj pripravljeni
    return place
