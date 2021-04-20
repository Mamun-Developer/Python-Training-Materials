from Class6.vehicle import vehicle


class bike(vehicle):
    def __init__(self, wheel, seat):
        super().__init__(wheel, seat)

    def horn(self):
        print("Pip pip")
