class Tree:
    def __init__(self, age, species):
        self.age = age
        self.species = species

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_species(self):
        return self.species

    def set_species(self, species):
        self.species = species

    def get_detail(self):
        return (
            ("age", str(self.age)),
            ("species", self.species)
        )


class NurseryTree(Tree):
    def __init__(self, age, species, cultivar, price):
        super().__init__(age, species)
        self.cultivar = cultivar
        self.price = price

    def get_cultivar(self):
        return self.cultivar

    def set_cultivar(self, cultivar):
        self.cultivar = cultivar

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_detail(self):
        return (
            *super().get_detail(),
            ("cultivar", self.cultivar),
            ("price", str(self.price))
        )


class ProtectedTree(Tree):
    def __init__(self, age, species, location):
        super().__init__(age, species)
        self.location = location

def get_location(self):
    return self.location

def set_location(self, location):
    self.location = location

def get_detail(self):
    return (
            *super().get_detail(),
            ("location", self.location)
        )


def print_detail(detail):
    for i in detail:
        if "age" == i[0]:
            print(f"This tree is {i[1]} years old.")
        elif "species" == i[0]:
            print(f"This tree belongs to {i[1]} species.")
        elif "location" == i[0]:
            print(f"This tree is located in {i[1]}.")
        elif "cultivar" == i[0]:
            print(f"This is {i[1]}.")
        elif "price" == i[0]:
            print(f"This tree costs {i[1]} dollars.")
    print()


# main program
if __name__ == '__main__':
    pine = Tree(80, "Pinus radiata")
    sequoia = ProtectedTree(1650, "Sequoiadendron giganteum", "Kings Canyon National Park")
    apple = NurseryTree(4, "Malus domestica", "Golden Delicious", 99.95)

    for tree in [pine, sequoia, apple]:
        print_detail(tree.get_detail())
