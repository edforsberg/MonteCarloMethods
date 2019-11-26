import numpy as np

class Model:

    def __init__(self, lattice_size):
        self.lattice_size = lattice_size
        self.lattice = np.zeros([lattice_size, lattice_size])



    def initialice(self, mode):
        if mode == 'hot':
            return 1
        elif mode == 'cold':
            return 2
        else:
            return "mode must be set to cold or hot!"
