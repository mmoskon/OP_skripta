import pandas as pd

df = pd.read_csv('place.csv', encoding="cp1250", skiprows=2, sep='\t')

#df.head()

df.columns = ['mesec', 'sektor', 'bruto', 'neto']
df2 = df.set_index('mesec')

#df.plot()
import matplotlib.pyplot as plt
#plt.show()

df.plot(x='mesec', y=['neto','bruto'])
plt.show()


df_javni= df[df['sektor']=='Javni sektor'] 
df_zasebni = df[df['sektor']=='Zasebni sektor']

ax = plt.gca()
df_javni.plot(x='mesec',
              y=['neto','bruto'],
              ax = ax)
df_zasebni.plot(x='mesec',
                y=['neto','bruto'],
                ax = ax)
plt.legend(['Javni sektor (neto)',
          'Javni sektor (bruto)',
          'Zasebni sektor (neto)',
          'Zasebni sektor (bruto)'])
plt.ylabel('Znesek [EUR]')
plt.show()

df_javni.to_excel('place_javni.xlsx', index=False)
df_javni2 = pd.read_excel('place_javni.xlsx')


