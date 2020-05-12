import numpy as np
A1 = np.genfromtxt("stevila1.csv", encoding="utf8", delimiter=",")
B1 = np.loadtxt("stevila1.csv", encoding="utf8", delimiter=",")

A2 = np.genfromtxt("stevila2.csv", encoding="utf8", delimiter=",")
B2 = np.loadtxt("stevila2.csv", encoding="utf8", delimiter=",", dtype='str')

A3 = np.genfromtxt("stevila3.csv", encoding="utf8", delimiter=",", names=True)
B3 = np.loadtxt("stevila3.csv", encoding="utf8", delimiter=",", dtype='U', skiprows=0)


