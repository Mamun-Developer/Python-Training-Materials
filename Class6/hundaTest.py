from Class6.vehiclePractice import amarVehicle


class hunda(amarVehicle):
    def __init__(self, wheel, seats):
        super().__init__(wheel, seats)

    def horn(self):
        print("Ring ring")
