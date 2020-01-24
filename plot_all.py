import numpy as np
import math as m
import matplotlib.pyplot as plt


ss = [8, 16, 32]
q = 20
jc = m.log(1+m.sqrt(q))
#print('j_crit=' + str(jc))
js = np.linspace(0.65*jc, 1.3*jc, num=15)


names_magnetisation = ['data/magnetisation_L' + str(s) + 'Q' + str(q) + '.csv' for s in ss]
names_energy = ['data/energy_L' + str(s) + 'Q' + str(q) + '.csv' for s in ss]

fig, ax = plt.subplots()
ax.set_xlabel('J')
ax.set_ylabel('<E>/V')
for i in range(len(ss)):
    data_energy = np.genfromtxt(names_energy[i], delimiter=',')
    plt.plot(js, data_energy[0])

#plt.show()


fig, ax = plt.subplots()
ax.set_xlabel('J')
ax.set_ylabel('<Mr>/V')
for i in range(len(ss)):
    data_magnetisation = np.genfromtxt(names_magnetisation[i], delimiter=',')
    for j in range(1):
        plt.plot(js, data_magnetisation[j])

#ax.set_title('Magnetisation, q='+str(q)+', lattice_size = '+str(s)+', 1E5 measurements')
plt.show()
