import matplotlib.pyplot as plt
import numpy as np

Vc_iniziale = 20
R_scarica = 2000
C = 4E-3

tau = R_scarica*C

t = np.linspace(0, 5*tau, num=1000)

vc = Vc_iniziale * np.exp(-t/tau)
ic = Vc_iniziale/R_scarica*(np.exp(-t/tau))

print("Costante di tempo di scarica: ", tau, "secondi")
print("Tempo di scarica: ", 5*tau, "secondi")


print ("\n\nCorrente di scarica")
print ("Tempo[s]", "Corrente[mA]")

for n in range(0, 5, 1):
    print(n*tau, "\t", round(Vc_iniziale/R_scarica*(np.exp(-n))*1000, 1))

print("\n\nTensione di scarica")
print("Tempo[s]", "Tensione[V]")

for n in range(0, 5, 1):
    print(n * tau, "\t", round(Vc_iniziale * (np.exp(-n)), 1))

plt.figure(1)
plt.title('Tensione di scarica del condensatore')
plt.plot(t, vc, 'g')
plt.grid(True)
plt.ylabel('Vc [volt]')
plt.xlabel('Tempo [s]')

plt.figure(2)
plt.title('corrente di scarica del condensatore')
plt.plot(t, ic, 'b')
plt.grid(True)
plt.ylabel('Ic [A]')
plt.xlabel('Tempo [s]')

plt.show()
