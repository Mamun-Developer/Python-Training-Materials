from Class6.vehicle import vehicle


class cycle(vehicle):
    def __init__(self, wheel, seats):
        super().__init__(wheel, seats)


cycleOb = cycle(2, 1)
print(cycleOb.getWheels())
