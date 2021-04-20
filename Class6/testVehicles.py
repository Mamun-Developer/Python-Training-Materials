from Class6.cycle import cycle
from Class6.bike import bike


def testCycle():
    cycle_ob = cycle(2, 1)
    print("The vehicle is: " + cycle_ob.getRunningDirection())
    cycle_ob.goForwad(20)
    cycle_ob.goBackward(20)
    print("Running: " + str(cycle_ob.isRunning()))
    cycle_ob.brake()
    print(cycle_ob.getRunningDirection())
    print(cycle_ob.isRunning())
    cycle_ob.lockVehicle("123456")
    print("Locked: " + str(cycle_ob.isLocked()))
    cycle_ob.goForwad(30)
    print(cycle_ob.isRunning())
    cycle_ob.unlockVehicle("123456")
    print("Locked: " + str(cycle_ob.isLocked()))
    cycle_ob.horn()


def testBike():
    bikeOb = bike(2, 2)
    print(bikeOb.isRunning())
