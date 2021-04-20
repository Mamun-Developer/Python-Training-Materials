class vehicle:
    def __init__(self, wheel, totalSeat):
        self.wheel = wheel
        self.totalSeat = totalSeat
        self.locked = False
        self.runForward = False
        self.runBackward = False
        self.speed = 0

    def goForwad(self, speed):
        if self.isLocked() == False:
            self.runForward = True
            self.runBackward = False
            self.speed = speed
        else:
            self.unauthorizedAccess()

    def goBackward(self, speed):
        if self.isLocked() == False:
            self.runForward = False
            self.runBackward = True
            self.speed = speed
        else:
            self.unauthorizedAccess()

    def brake(self):
        self.runForward = False
        self.runBackward = False
        self.speed = 0

    def lockVehicle(self, password):
        self.locked = True
        self.password = password

    def isLocked(self):
        return self.locked

    def unlockVehicle(self, password):
        if self.password == password:
            self.locked = False

    def unauthorizedAccess(self):
        import time
        print("Unauthorized access detected. Please wait 10 sec before next try")
        time.sleep(2)

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

    def horn(self):
        pass
