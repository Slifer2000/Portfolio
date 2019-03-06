import time
import random

ThunderMountain = "Closed"
StarTours = "Closed"
PhantomManour = "Closed"
day = 1
hour = 0
ThunderMountainPeople = 0
StarToursPeople = 0
PhantomManourPeople = 0
while True:
    time.sleep(0.5)
    print (("Day ") + (str(day)))
    print ("Hour = " + str(hour))
    hour = hour + 1
    if hour == 10:
        ThunderMountain = "Open"
        print ("Thunder Mountain is open!")
        ThunderMountainPeople = random.randint(0,400)
        print((str((ThunderMountainPeople))) + (" people are in the queue"))
    if hour == 11:
        StarTours = "Open"
        print ("Star Tours is open!")
        StarToursPeople = random.randint(0,150)
        print((str((StarToursPeople))) + (" people are in the queue"))
    if hour == 13:
        PhantomManour = "Open"
        PhantomManourPeople = random.randint(0,400)
        print((str((PhantomManourPeople))) + (" people are in the queue"))
    if hour == 22:
        ThunderMountain = "Closed"
        StarTours = "Closed"
        PhantomManour = "Closed"
    if hour == 24:
        hour = 0
        day = day + 1
        print (("Day ") + (str(day)))
