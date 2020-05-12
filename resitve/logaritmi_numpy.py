import numpy as np
import matplotlib.pyplot as plt

# hitro generiranje vrednosti na osi x
X = np.arange(0.001, 5.001, 0.001) 

# računanje logaritmov brez zanke for 
Y_2 = np.log2(X)
Y_e = np.log(X)
Y_10 = np.log10(X)

# nespremenjena koda od prej
plt.plot(X,Y_2, label="$log_2(x)$")
plt.plot(X,Y_e, label="$log_e(x)$")
plt.plot(X,Y_10, label="$log_{10}(x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
