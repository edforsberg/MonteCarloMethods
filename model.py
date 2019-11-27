import numpy as np

class Model:

    def __init__(self, lattice_size):
        self.lattice_size = lattice_size*lattice_size
        self.lattice = np.zeros([lattice_size*lattice_size])



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
        

    def compute_observables(self):
        return
