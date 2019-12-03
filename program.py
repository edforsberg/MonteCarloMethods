import initialize as init
import model as md
import simulate as sim
import copy


def main():
    ## Global parameters
    q = [2, 4, 8, 20]
    s = [8, 16, 32]

    model_cold = md.Model(lattice_size=8, q=4, j=0.8, m=0)
    model_cold.initialize("cold")
    observables = md.Observables(q=4)
    model_cold.n_sweeps(10)
    #print(observables.Magnetisation)
    observables.add_values(model_cold)
    #print(observables.Magnetisation)
    observables.add_values(model_cold)
    print(observables.Magnetisation[1])

'''
    model_cold = md.Model(lattice_size=8, q=4, alpha=1, j=100, m=0)
    model_hot = copy.copy(model_cold)
    model_cold.initialize("cold")
    model_hot.initialize("hot")

    #while model_hot.H > model_cold.H:
       # model_cold.n_sweeps(100)
        #model_hot.n_sweeps(100)
    for i in range(100):
        model_hot.n_sweeps(100)
        model_cold.n_sweeps(100)
        print("C:" + str(model_cold.H))
        print("H:" + str(model_hot.H))
'''





if __name__ == '__main__':
    main()