import numpy as np
import math
import copy


def kronecker(a, b):
    if a == b:
        return 1
    else:
        return 0


class Spin:
    def __init__(self, lattice_size, value, position):
        ls = lattice_size
        pos = position
        self.value = value
        q, r = divmod(pos, ls)

        neig_l = r-1+q*ls if r > 0 else ls-1+q*ls
        neig_r = r+1+q*ls if r+1 < ls else q*ls
        neig_u = (q+1)*ls+r if q+1 < ls else r
        neig_d = (q-1)*ls+r if q > 0 else r+ls*(ls-1)

        self.neighbours = [neig_l, neig_r, neig_u, neig_d]


class Observables:
    def __init__(self, q):
        self.Energy = []
        self.Magnetisation = np.empty([0, q])

    def add_values(self, model):
        self.Energy.append(-model.H)
        magnetisation = np.zeros([1, model.Q]) #have to remove the first row somehow
        for r in range(model.Q):
            for spin in model.lattice:
                if spin.value == r:
                    magnetisation[0][r] += 1
        #self.Magnetisation = np.append(self.Magnetisation, magnetisation, axis=0)
        self.Magnetisation = np.vstack([self.Magnetisation, magnetisation])

    def calculate_statistics(self):
        avg_energy = np.sum(self.Energy) / len(self.Energy)
        std_energy = np.std(self.Energy)
        statistics_energy = np.array([avg_energy, std_energy])

        avg_magnetisation = np.sum(self.Magnetisation, axis=0)/self.Magnetisation.shape[0]
        std_magnetisation = np.std(self.Magnetisation, axis=0)
        arr_ixd = avg_magnetisation.argsort()
        avg_magnetisation = avg_magnetisation[arr_ixd[::-1]]
        std_magnetisation = std_magnetisation[arr_ixd[::-1]]
        statistics_magnetisation = np.concatenate([avg_magnetisation, std_magnetisation])

        return statistics_energy, statistics_magnetisation


class Model:
    def __init__(self, lattice_size, q, j, m):
        self.alpha = 1
        self.ls = lattice_size
        self.Q = q
        self.J = j
        self.M = m
        self.H = 0
        self.beta = j/self.alpha

        self.ls_sqr = int(lattice_size**2)
        lattice = np.ndarray(self.ls_sqr, dtype=np.object)
        for i in range(self.ls_sqr):
            lattice[i] = Spin(lattice_size, 0, i)
        self.lattice = lattice

    def initialize(self, mode):
        if mode == 'cold':
            for spin in self.lattice:
                spin.value = 0

            h = 0
            for spin in self.lattice:
                for n in spin.neighbours:
                    if spin.value == self.lattice[n].value:
                        h += 1
            self.H = h

        elif mode == 'hot':
            for spin in self.lattice:
                spin.value = np.random.randint(0, self.Q)

            h = 0
            for spin in self.lattice:
                for n in spin.neighbours:
                    if spin.value == self.lattice[n].value:
                        h += 1
            self.H = h

        else:
            return "mode must be set to cold or hot!"

    def n_sweeps(self, nr_sweeps):
        for n in range(nr_sweeps):
            for i in range(self.ls):
                new_spin = np.random.randint(self.Q)
                spin = self.lattice[i]
                sum_ = 0
                for j in range(4):
                    sum_ = sum_ + kronecker(new_spin, self.lattice[spin.neighbours[j]].value) \
                           - kronecker(spin.value, self.lattice[spin.neighbours[j]].value)

                delta = np.exp(self.J*sum_)
                if np.random.random() < delta:
                    self.lattice[i].value = new_spin
                    self.H = self.H-sum_