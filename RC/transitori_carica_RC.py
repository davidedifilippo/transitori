import matplotlib.pyplot as plt
import numpy as np

E = 20
R_carica = 1500
C = 4E-3

tau = R_carica*C

t = np.linspace(0, 5*tau, num=1000)

vc = E*(1-np.exp(-t/tau))
ic = E/R_carica*(np.exp(-t/tau))

print ("\n\nCorrente di carica")
print ("Tempo[s]", "Corrente[mA]")

for n in range(0, 5, 1):
    print(n*tau, "\t", round(E/R_carica*(np.exp(-n))*1000, 1))

print("\n\nTensione di carica")
print("Tempo[s]", "Tensione[V]")

for n in range(0, 5, 1):
    print(n * tau, "\t", round(E * (1-np.exp(-n)), 1))

plt.figure(1)
plt.title('Tensione di carica del condensatore')
plt.plot(t, vc, 'g')
plt.grid(True)
plt.ylabel('Vc [volt]')
plt.xlabel('Tempo [s]')

plt.figure(2)
plt.title('corrente di carica del condensatore')
plt.plot(t, ic, 'purple')
plt.grid(True)
plt.ylabel('Ic [A]')
plt.xlabel('Tempo [s]')

plt.show()

