import initialize as init
import model as md
import simulate as sim


def main():
    ## Global parameters
    q = [2, 4, 8, 20]
    s = [8, 16, 32]

    model = md.Model(8, 4,1, 1, 0)
    print(model.ls)
    print(model.lattice)
    model.initialize('hot')
    delta = model.n_sweeps(9)
    print(delta)

if __name__ == '__main__':
    main()