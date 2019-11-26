class Model(object):
    def __init__(self, name):
        self.name = name

    def whatsyourname(self):
        print("My name is "+ str(self.name) + "!")


model = Model("Monte Carlo")
model.whatsyourname()

