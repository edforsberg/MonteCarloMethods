import numpy as np
import model as md
import copy


def main():
    ## Global parameters
    q = [2, 4, 8, 20]
    s = [8, 16, 32]
    nmeas = 100
    nskip = 10

    model_cold = md.Model(lattice_size=8, q=4, j=0.8, m=0)
    model_hot = copy.copy(model_cold)
    model_cold.initialize("cold")
    model_hot.initialize("hot")
    observables = md.Observables(q=4)

    while model_cold.H > model_hot.H:
        model_hot.n_sweeps(nskip)
        model_cold.n_sweeps(nskip)

    model = copy.copy(model_cold)

    for i in range(nmeas):
        model.n_sweeps(nskip)
        observables.add_values(model)

    print([observables.Magnetisation, observables.Energy])
    write_scv(observables, model)


def write_scv(observables, model):
    name_magnetisation = 'data/Magnetisation_L' + str(model.ls) + 'Q' + str(model.Q) + '.csv'
    name_energy = 'data/Energy_L' + str(model.ls) + 'Q' + str(model.Q) + '.csv'
    np.savetxt(name_magnetisation, observables.Magnetisation, delimiter=',', fmt='%i')
    np.savetxt(name_energy, observables.Energy, delimiter=',', fmt='%i')






if __name__ == '__main__':
    main()