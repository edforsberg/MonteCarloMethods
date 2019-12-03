import numpy as np
import math as m
import matplotlib.pyplot as plt

q = 4
s = 32
jc = m.log(1+m.sqrt(q))
js = np.linspace(jc/2, 1.5*jc, num=20)

name_magnetisation = 'data/magnetisation_L' + str(s) + 'Q' + str(q) + '.csv'
name_energy = 'data/energy_L' + str(s) + 'Q' + str(q) + '.csv'

data_energy = np.genfromtxt(name_energy, delimiter=',')
data_magnetisation = np.genfromtxt(name_magnetisation, delimiter=',')#.transpose()


print(data_magnetisation[4])
print(js)


fig, ax = plt.subplots()
ax.errorbar(js, data_energy[0],
            yerr=data_energy[1],
            fmt='-o')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Line plot with error bars')

fig, ax = plt.subplots()
for i in range(q):
    ax.errorbar(js, data_magnetisation[i],
                yerr=data_magnetisation[q+i],
                fmt='-o')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Line plot with error bars')


plt.show()

