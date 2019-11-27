import initialize as init
import model as md
import simulate as sim


def main():
    ## Global parameters
    q = [2, 4, 8, 20]
    s = [8, 16, 32]

    model = md.Model(8)
    print(model.lattice_size)
    print(model.lattice)
    model.initialize('hot')
    sp = model.lattice[62]

if __name__ == '__main__':
    main()