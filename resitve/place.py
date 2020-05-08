import matplotlib.pyplot as plt
import numpy as np

"""
Napisi funkcijo, ki prebere datoteko s placami, ki smo jo pridobili iz strani SURS
"""
def preberi(ime_datoteke):    
    javni = []
    mesci_javni = []
    zasebni = []
    mesci_zasebni = []

    f = open(ime_datoteke, encoding="cp1250")
    """
    # izpusti prve 3 vrstice
    f.readline()
    f.readline()
    f.readline()
    print(f.read())
    """
    # ali pa upostevaj samo vrstice, ki se zacnejo z "20...       
    for vrstica in f:
        if vrstica.startswith('"20'):
            vrstica = vrstica.strip()
            mesec, sektor, placa = vrstica.split("\t")
            mesec = mesec.replace('"','')
            sektor = sektor.replace('"','')
            if sektor.startswith("Javni"):
                javni.append(float(placa))
                mesci_javni.append(mesec)
            else:
                zasebni.append(float(placa))
                mesci_zasebni.append(mesec)

    return mesci_javni, javni, mesci_zasebni, zasebni
                
           

    
MJ, J, MZ, Z = preberi("0701054.csv")
avg_J = sum(J)/len(J)
avg_Z = sum(Z)/len(Z)

J = np.array(J)
MJ = np.array(MJ)
Z = np.array(Z)
MZ = np.array(MZ)

J1 = J[J>avg_J]
MJ1 = MJ[J>avg_J]

plt.plot(MJ, J, label="Javni sektor", color="#1b9e77")
plt.plot(MZ, Z, label="Zasebni sektor", color="#d95f02")
plt.plot(MJ1, J1, 'x', color="#1b9e77")
plt.plot(MZ[Z>avg_Z], Z[Z>avg_Z], 'x', color="#d95f02")
plt.title("Bruto plače")
plt.xlabel("Leto")
plt.ylabel("Znesek [EUR]")
plt.legend()

locs = range(0,len(J),12)
labs = MJ[::12]
for i in range(len(labs)):
    labs[i] = labs[i][:4]

plt.xticks(locs, labs)


avg_J = sum(J)/len(J)
avg_Z = sum(Z)/len(Z)

x1,x2,y1,y2 = plt.axis()

plt.plot([x1,x2], [avg_J, avg_J], 'k--', linewidth=0.5)
plt.plot([x1,x2], [avg_Z, avg_Z], 'k--', linewidth=0.5)

plt.axis([x1,x2,0,max(J)])    


plt.show()

J18 = []
MJ18 = []
Z18 = []
MZ18 = []

for i in range(len(MJ)):
    if '18' in MJ[i]:
        J18.append(J[i])
        MJ18.append(MJ[i][-2:])
    if '18' in MZ[i]:
        Z18.append(Z[i])
        MZ18.append(MZ[i][-2:])
    
lokacije1 = list(range(len(J18)))
lokacije2 = list(range(len(J18)))
for i in range(len(lokacije1)):
    lokacije1[i] -= 0.2
    lokacije2[i] += 0.2
plt.bar(lokacije1, J18, label="Javni", width=0.4)
plt.bar(lokacije2, Z18, label="Zasebni", width=0.4)
plt.xticks(range(len(MZ18)), MZ18)
plt.title("Plače v letu 2018")
plt.xlabel("Mesec")
plt.ylabel("Bruto plača [EUR]")
plt.legend()
plt.show()

plt.boxplot([J18, Z18])
plt.xticks([1,2],['Javni', 'Zasebni'])
plt.show()

from random import gauss
p = [gauss(10,5) for i in range(10000)]
plt.hist(p, bins=50)
plt.show()







