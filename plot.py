import numpy as np
import math as m
import matplotlib.pyplot as plt

q = 2
s = 16
nmeas = 10000
jc = m.log(1+m.sqrt(q))
print('j_crit=' + str(jc))
js = np.linspace(0.65*jc, 1.3*jc, num=15)

name_magnetisation = 'data/magnetisation_L' + str(s) + 'Q' + str(q) + '.csv'
name_energy = 'data/energy_L' + str(s) + 'Q' + str(q) + '.csv'

data_energy = np.genfromtxt(name_energy, delimiter=',')
data_magnetisation = np.genfromtxt(name_magnetisation, delimiter=',')

fig, ax = plt.subplots()
ax.errorbar(js, data_energy[0],
            yerr=data_energy[1],
            fmt='-o')

ax.set_xlabel('J')
ax.set_ylabel('<E>/V')
ax.set_title('Energy, q='+str(q)+', lattice_size = '+str(s)+', 1E5 measurements')
locs, _ = plt.xticks()
locs = np.delete(locs, 4)
labels = np.append([str(round(i, 2)) for i in locs], 'Jc')
locs = np.append(locs, jc)
plt.xticks(locs, labels)

fig, ax = plt.subplots()
for i in range(q):
    ax.errorbar(js, data_magnetisation[i],
                yerr=data_magnetisation[q+i],
                fmt='-o')

ax.set_xlabel('J')
ax.set_ylabel('<Mr>/V')
ax.set_title('Magnetisation, q='+str(q)+', lattice_size = '+str(s)+', 1E5 measurements')
locs, _ = plt.xticks()
locs = np.delete(locs, 4)
labels = np.append([str(round(i, 2)) for i in locs], 'Jc')
locs = np.append(locs, jc)
plt.xticks(locs, labels)

plt.show()
