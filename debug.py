import numpy as np
import model as md
import copy
import math as mt


def main():
    q = 2
    s = 8
    jc = mt.log(1 + mt.sqrt(q))
    js = np.linspace(jc / 3, 2 * jc, num=15)
    nmeas = 1000
    nskip = 10

    data_energy = np.empty([0, 2])
    data_magnetisation = np.empty([0, 2 * q])

    model = md.Model(lattice_size=s, q=q, j=jc, m=0)

    a = model.lattice[56].neighbours
    print(a)


if __name__ == '__main__':
    main()