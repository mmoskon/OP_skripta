from place_beri import uvozi_place # funkcija za uvoz
import matplotlib.pyplot as plt

# uvozi podatke v slovar
place = uvozi_place('place.csv')
# pridobi sezname iz slovarja
MJ = place['Javni sektor']['mesec']
ZJ = place['Javni sektor']['bruto']
MZ = place['Zasebni sektor']['mesec']
ZZ = place['Zasebni sektor']['bruto']

# izluščimo podatke za leto 2018
MJ_2018 = []
ZJ_2018 = []
MZ_2018 = []
ZZ_2018 = []

for mj, zj in zip(MJ, ZJ):
    if "2018" in mj:
        MJ_2018.append(mj[-3:]) # brez leta
        ZJ_2018.append(zj)

for mz, zz in zip(MZ, ZZ):
    if "2018" in mz:
        MZ_2018.append(mz[-3:]) # brez leta
        ZZ_2018.append(zz)


plt.bar(range(len(ZJ_2018)), ZJ_2018)
plt.bar(range(len(ZZ_2018)), ZZ_2018)

plt.xticks(range(len(MJ_2018)), MJ_2018)

plt.title('Podatki o plačah za leto 2018')
plt.legend(['Javni sektor', 'Zasebni sektor'])
plt.show()

