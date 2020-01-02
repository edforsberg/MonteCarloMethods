import numpy as np
import model as md
import copy
import math as mt


def main():
    ## Global parameters
    q = 4
    s = 60
    jc = mt.log(1+mt.sqrt(q))
    js = np.linspace(0, 2*jc, num=20)
    nmeas = 500
    nskip = 10
    nequi = 100

    data_energy = np.empty([0, 2])
    data_magnetisation = np.empty([0, 2*q])

    for j in js:

        observables = md.Observables(q=q)
        '''
        model_cold = md.Model(lattice_size=s, q=q, j=j, m=0)
        model_hot = copy.copy(model_cold)
        model_cold.initialize("cold")
        model_hot.initialize("hot")
        

        while model_cold.H < model_hot.H:
            model_hot.n_sweeps(nskip)
            model_cold.n_sweeps(nskip)
            
        '''

        model = md.Model(lattice_size=s, q=q, j=j, m=0)
        for i in range(nequi):
            model.n_sweeps(nskip)

        for i in range(nmeas):
            model.n_sweeps(nskip)
            observables.add_values(model)

        e, m = observables.calculate_statistics()
        data_energy = np.vstack([data_energy, e])
        data_magnetisation = np.vstack([data_magnetisation, m])
        print('j=' + str(j))

    data_energy = data_energy.transpose()/s
    data_magnetisation = data_magnetisation.transpose()/s
    write_scv(data_magnetisation, name='magnetisation', model=model)
    write_scv(data_energy, name='energy', model=model)


def write_scv(data, name, model):
    name_magnetisation = 'data/'+name+'_L' + str(model.ls) + 'Q' + str(model.Q) + '.csv'
    np.savetxt(name_magnetisation, data, delimiter=',', fmt='%1.4f')


if __name__ == '__main__':
    main()