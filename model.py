import numpy as np

class Spin:

    def __init__(self, lattice_size, value, position):
        ls = lattice_size
        pos = position
        self.value = value
        q, r = divmod(pos, ls)

        self.neig_l = r-1+q*ls if r-1 > 1 else lattice_size-1+q*ls
        self.neig_r = r+1+q*ls if r+1 < ls else q*ls
        self.neig_u = (q+1)*ls+r if q+1 < ls else r
        self.neig_d = (q-1)*ls+r if q-1 > 0 else r+ls*(ls-1)

class Model:

    def __init__(self, lattice_size):
        self.lattice_size = lattice_size
        ls_sqr = lattice_size**2

        lattice = np.ndarray((ls_sqr,), dtype=np.object)
        for i in range(ls_sqr):
            lattice[i] = Spin(lattice_size, 0, i)
        self.lattice = lattice



    def initialize(self, mode):
        if mode == 'hot':
            indexes = np.random.choice(list(range(self.lattice_size)), size=3, replace=False)
            for i in indexes:
                self.lattice[i] = 1
        elif mode == 'cold':
            return 2
        else:
            return "mode must be set to cold or hot!"

    def sweep(self, nr_sweeps):
        return

    def compute_observables(self):
        return
