# Requirement
# 1. Gun magazine limit = 6
# 2. Per trigger bullet fires = 1
# 3. Reload time = 3
# 4. Total Bullet in the box = 50
# 5. Auto reload support = True
# 6. Bullet size = 9mm
import time
class gun:
    def __init__(self,magazineLimit = 6,perTrigerOutput = 1, reloadTime = 3,
                 autoReload = True,bulletSize = "9mm",bulletsInTheBox=20):
        self.magazineLimit = magazineLimit
        self.perTrigerOutput = perTrigerOutput
        self.reloadTime = reloadTime
        self.autoReload = autoReload
        self.bulletSize = bulletSize
        self.loadedBulletsCount = 0
        self.bulletsInTheBox = bulletsInTheBox
        self.stopFiring = False

    def fire(self):
        if self.getRemainingBulletsInGun()==0:
            print("Magazine Empty")
            if self.autoReload == True:
                print("Auto Reloading")
                self.reload()
            else:
                PROCEED_RELOAD = 1
                DONT_RELOAD = 2
                command = int(input("1. Reload\n2. Dont reload\n"))
                if command==PROCEED_RELOAD:
                    print("Reloading")
                    self.reload()
                elif command==DONT_RELOAD:
                    print("Reload Required")

        if self.getRemainingBulletsInGun()>0:
            self.loadedBulletsCount = self.loadedBulletsCount - 1
            print(f"Fire: {self.magazineLimit}/{self.loadedBulletsCount}")

    def reload(self):
        print("Wait for "+str(self.reloadTime)+"secs")
        time.sleep(self.reloadTime)
        bulletToReload = self.magazineLimit - self.getRemainingBulletsInGun()
        if self.getRemainingBulletsInBox()>=bulletToReload:
            self.loadedBulletsCount = self.loadedBulletsCount + bulletToReload
            self.bulletsInTheBox = self.bulletsInTheBox - bulletToReload
            print("reloaded: Magazine Full")
        elif self.getRemainingBulletsInBox()==0:
            print("Not enough bullets in the box")
            self.stopFiring = True

        elif self.getRemainingBulletsInBox()<bulletToReload:
            self.loadedBulletsCount = self.loadedBulletsCount + self.getRemainingBulletsInBox()
            self.bulletsInTheBox = 0
            print("reloaded: Magazine - "+str(self.loadedBulletsCount))


    def clearMagazine(self):
        temp = self.loadedBulletsCount
        self.loadedBulletsCount = 0
        self.bulletsInTheBox = self.bulletsInTheBox + temp

    def getRemainingBulletsInGun(self):
        return self.loadedBulletsCount

    def getRemainingBulletsInBox(self):
        return self.bulletsInTheBox

shortGun = gun()
# Gun Commands
# RBIB- Remaining Bullet in BOX
FIRE = 1
RELOAD = 2
CLEAR_MAGAZINE = 3
LOADED_BULLETS = 4
RBIB = 5
REMAINING_BULLETS_IN_BOX = 5
STOP_FIRING = 6

while shortGun.stopFiring == False:
    print("COMMAND LIST:\n1. Fire \n2. Reload \n3. Clear Magazine  \n4. Loaded Bullets \n5. Bullets in the box \n6. Stop Firing")
    command = int(input("COMMAND NO: "))

    if command == FIRE:
        shortGun.fire()
    elif command == RELOAD:
        shortGun.reload()
    elif command == CLEAR_MAGAZINE:
        shortGun.clearMagazine()
        print("Magazine Cleared")
    elif command == LOADED_BULLETS:
        print("Bullets in the MAGAZINE: "+str(shortGun.getRemainingBulletsInGun()))
    elif command == REMAINING_BULLETS_IN_BOX:
        print("Bullets in the BOX: "+str(shortGun.getRemainingBulletsInBox()))
    elif command == STOP_FIRING:
        shortGun.stopFiring = True
        print("Firing stopped")
    else:
        print("Wrong Command. Try again")