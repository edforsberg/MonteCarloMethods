import initialize as init
import model as md
import simulate as sim
import copy


def main():
    ## Global parameters
    q = [2, 4, 8, 20]
    s = [8, 16, 32]
    nmeas = 10000
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






if __name__ == '__main__':
    main()