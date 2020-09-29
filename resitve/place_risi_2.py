from place_beri import uvozi_place # funkcija za uvoz
import matplotlib.pyplot as plt

# uvozi podatke v slovar
place = uvozi_place('place.csv')

# sprehod čez vse sektorje
for sektor in place:
    mesec = place[sektor]['mesec']
    znesek = place[sektor]['bruto']
    plt.plot(mesec, znesek, label=sektor) 

# dodaj oznake
plt.xlabel("mesec")
plt.ylabel("znesek [EUR]")
plt.title("Povprečne mesečne plače")
plt.legend()

oznake = []
for m in mesec[::12]: # vzamemo vsako 12-to oznako
    oznake.append(m[:4]) # vzamemo samo podatek o letu

# vsaka 12-ta lokacija
lokacije = range(0, len(mesec), 12) 

plt.xticks(lokacije, oznake)

plt.show() # prikaži graf
