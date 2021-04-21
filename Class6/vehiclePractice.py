class vicle:
    def __init__(self, wheel, totalSeat):
        self.wheel = wheel
        self.totalSeat = totalSeat
        self.locked=False
        self.runbackword=False
        self.runForward=False
        self.speed=0

    def goForward(self, speed):
        if isLocked() == False:
            self.runbackword = False
            self.runForward = True
            self.speed =speed
        else:
            self.unauthorizedAcces()

    def goBackward(self):
        if isLocked() == False:
            self.runForward = False
            self.runbackword = True
            self.speed = speed
        else:
            self.unauthorizedAcces()
    def Break(self):
        self.runbackword = False
        self.runForward = False
        self.speed=0

    def lockVicle(self, password):
        self.locked = True
        self.password = password

    def isLocked(self):
        return self.lockVicle()

    def unlockVicle(self, password):
        self.password==password
        self.locked=False

    def unauthorizedAcces(self):
        import time
        print("Unauthorized Access")
        time.sleep(2)

    def getWheeel(self):
        return self.wheel

    def getSeat(self):
        return self.getSeat()
    def isRunning(self):
        if speed == 0:
            return False
        else:
            return True
    def horn(self):
        pass

