import initialize as init
import model as md


def main():
    model = md.Model(8)
    print(model.lattice_size)
    print(model.lattice)
    i = model.initialice('codeld')
    print(i)

if __name__ == '__main__':
    main()