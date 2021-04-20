from Class6.vehicle import vehicle


class cycle(vehicle):
    def __init__(self, wheel, seats):
        super().__init__(wheel, seats)

    def horn(self):
        print("Ring ring")
