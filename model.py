import numpy as np
import math


class Spin:
    def __init__(self, lattice_size, value, position):
        ls = lattice_size
        pos = position
        self.value = value
        q, r = divmod(pos, ls)

        neig_l = r-1+q*ls if r-1 > 1 else lattice_size-1+q*ls
        neig_r = r+1+q*ls if r+1 < ls else q*ls
        neig_u = (q+1)*ls+r if q+1 < ls else r
        neig_d = (q-1)*ls+r if q-1 > 0 else r+ls*(ls-1)

        self.neighbours = [neig_l, neig_r, neig_u, neig_d]


class Observables:
    def __init__(self):
        self.Energy = []
        self.Magnetisation = []

        def add_values(model):
            self.Energy.append(model.H)
            magnetisation = 0
            for spin in model.lattice:
                if spin.value == 0:
                    magnetisation += 1
            self.Magnetisation.append(magnetisation)


class Model:
    def __init__(self, lattice_size, q, alpha, j, m):
        self.ls = lattice_size
        self.Q = q
        self.J = j
        self.M = m
        self.H = 0
        self.beta = j/alpha
        self.alpha = alpha

        self.ls_sqr = lattice_size**2
        lattice = np.ndarray((self.ls_sqr,), dtype=np.object)
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
                        h -= 1
            self.H = h

        elif mode == 'hot':
            for spin in self.lattice:
                spin.value = np.random.randint(0, self.Q)

            h = 0
            for spin in self.lattice:
                for n in spin.neighbours:
                    if spin.value == self.lattice[n].value:
                        h -= 1
            self.H = h

        else:
            return "mode must be set to cold or hot!"

    def n_sweeps(self, nr_sweeps):
        for n in range(nr_sweeps):
            new_spin = np.random.randint(0, self.Q)
            site = np.random.randint(0, self.ls_sqr)

            new_lattice = self.lattice
            new_lattice[site].value = new_spin
            new_h = 0
            for spin in new_lattice:
                for n in spin.neighbours:
                    if spin.value == self.lattice[n].value:
                        new_h -= 1

            delta = math.exp(-self.beta*(new_h-self.H))
            threshold = np.random.random()
            if delta>threshold:
                self.H = new_h
                self.lattice = new_lattice

    def compute_observables(self):
        Observables.add_values(self)