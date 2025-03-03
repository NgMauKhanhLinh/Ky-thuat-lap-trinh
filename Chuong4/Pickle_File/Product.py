class Product:
    def __init__(self):
        self.id = 1
        self.name = "Coca"
        self.price = 100.0

    def __str__(self):
        return (str(self.id) + "\t"
                + self.name + "\t"
                + str(self.price))
