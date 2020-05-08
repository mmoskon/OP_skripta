from place_beri import uvozi_place # funkcija za uvoz
import matplotlib.pyplot as plt

# uvozi podatke v slovar
place = uvozi_place('place.csv')
# pridobi sezname iz slovarja
MJ = place['Javni sektor']['mesec']
ZJ = place['Javni sektor']['bruto']
MZ = place['Zasebni sektor']['mesec']
ZZ = place['Zasebni sektor']['bruto']


plt.plot(MJ, ZJ) # riši javni sektor
plt.plot(MZ, ZZ) # riši zasebni sektor

# dodaj oznake
plt.xlabel("mesec")
plt.ylabel("znesek [EUR]")
plt.title("Povprečne mesečne plače")
plt.legend(['Javni sektor', 'Zasebni sektor'])

oznake = []
for mj in MJ[::12]: # vzamemo vsako 12-to oznako
    oznake.append(mj[:4]) # vzamemo samo podatek o letu

# vsaka 12-ta lokacija
lokacije = range(0, len(MJ), 12) 

plt.xticks(lokacije, oznake)

plt.show() # prikaži graf
