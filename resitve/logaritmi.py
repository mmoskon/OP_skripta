from math import log2, log, log10
import matplotlib.pyplot as plt

X_cel = range(1,5001,1) # predpriprava za koordinate x

X = []
Y_2 = []
Y_e = []
Y_10 = []

for x in X_cel:
    x /= 1000 # koordinata x
    X.append(x)
    
    Y_2.append(log2(x)) # dvojšiki
    Y_e.append(log(x)) # naravni
    Y_10.append(log10(x)) # desetiški

plt.plot(X,Y_2, label="$log_2(x)$")
plt.plot(X,Y_e, label="$log_e(x)$")
plt.plot(X,Y_10, label="$log_{10}(x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
