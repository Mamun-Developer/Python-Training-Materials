class vehicle:
    def __init__(self, wheel, totalSeat):
        self.wheel = wheel
        self.totalSeat = totalSeat

    def goForwad(self, speed):
        self.runForward = True
        self.runBackward = False
        self.speed = speed

    def goBackward(self, speed):
        self.runForward = False
        self.runBackward = True
        self.speed = speed

    def brake(self):
        self.runForward = False
        self.runBackward = False
        self.speed = 0

    def lockVehicle(self, password):
        self.locked = True
        self.password = password

    def unlockVehicle(self, password):
        if self.password == password:
            self.locked = False

    def getWheels(self):
        return self.wheel

    def getSeats(self):
        return self.totalSeat

    def isRunning(self):
        if self.speed == 0:
            return False
        else:
            return True

    def getRunningDirection(self):
        if self.runForward == True:
            return "Forward"
        elif self.runBackward == True:
            return "Backward"
        else:
            return "Stalled"
