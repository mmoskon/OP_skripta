from place_beri import uvozi_place # funkcija za uvoz
import matplotlib.pyplot as plt

MJ, ZJ, MZ, ZZ = uvozi_place('place.csv')
plt.plot(MJ, ZJ) # riši javni sektor
plt.plot(MZ, ZZ) # riši zasebni sektor

# dodaj oznake
plt.xlabel("mesec")
plt.ylabel("znesek [EUR]")
plt.title("Povprečne mesečne plače")
plt.legend(['javni', 'zasebni'])

oznake = []
for mj in MJ[::12]: # vzamemo vsako 12-to oznako
    oznake.append(mj[:4]) # vzamemo samo podatek o letu

# vsaka 12-ta lokacija
lokacije = range(0, len(MJ), 12) 

plt.xticks(lokacije, oznake)

print(plt.axis())

plt.show() # prikaži graf
