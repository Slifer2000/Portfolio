import time
loop1 = True
loop2 = True
loop3 = True
loop4 = True
loop5 = True
loop6 = True
loop7 = True
loop8 = True
loop9 = True
armour = False
TL50 = False
thermaldetonator = False
def start():
    print ("You are in Tantive IV.")
    time.sleep(2)
    print ("Your mission is to sabatage the weapons firing mechanism before it is range of Yavin IV.")
    time.sleep(2)
    while loop1 == True:
        choice = input("n, e, s, w ")
        if choice == "w":
            print ("Well done, next objective incoming.")
            hanger()
            Loop1 = False
        else:
            print ("You aren't permitted to go that way.")

def hanger():
    print ("You have entered the hanger.")
    time.sleep(2)
    print ("As you exit your ship, you spot a stormtrooper guarding the way.")
    time.sleep(2)
    shipguard()
    time.sleep(2)
    Interact1()

def armoury():
    time.sleep(2)
    print ("You have entered the armoury.")
    Interact2()
    time.sleep(2)
    Interact3()

def detentionblock():
    print ("You have entered the detention block.")
    choice = input("n, e, s, w ")
    if choice == "e":
        print ("Well done, next objective incoming.")
        elevator()
    elif choice == "s":
        print ("Well done, next objective incoming.")
        weaponcontrols()
    elif choice == "w":
        armoury()
    else:
        print ("You aren't permitted to go that way.")

def canteen():
    print ("You have entered the canteen.")
    choice = input("n, e, s, w ")
    if choice == "n":
        armoury()
    else:
        print ("You aren't permitted to go that way.")

def weaponcontrols():
    print ("You have entered the weapon crontrols point.")
    choice = input("n, e, s, w ")
    if choice == "n":
        detentionblock()
    elif choice == "e":
        print ("Well done, next objective incoming.")
        hanger2()
    else:
        print ("You aren't permitted to go that way.")

def elevetor():
    print ("You have entered the elevator.")
    choice = input("n, e, s, w ")
    if choice == "n":
        print ("Well done, next objective incoming.")
        throneroom()
    elif choice == "w":
        detentionblock()
    else:
        print ("You aren't permitted to go that way.")

def throneroom():
    print ("You have entered the throne room.")
    choice = input("n, e, s, w ")
    if choice == "s":
        elevator()
    else:
        print ("You aren't permitted to go that way.")

def hanger2():
    print ("You have entered the second hanger.")
    choice = input("n, e, s, w ")
    if choice == "e":
        weaponcontrols()
    elif choice == "s":
        print ("Well done, you have escaped incoming.")

    else:
        print ("You aren't permitted to go that way.")

def shipguard():
    takedown1 = input("What would you like to do? ")
    if takedown1 == "kill":
        print ("You have dragged the guard into your ship and taken him out silently.")
        print ("Hurry, a guard is coming.")

    else:
        print ("You have been spotted and are taken prisoner to the detention block.")
        detentionblock()
    
def Interact1():
    interact1 = input("Would you like to interact? ")
    if interact1 == "yes":
        item1 = input("What would you like to take? ")
        if item1 == "armour":
            armour = True
            global loop2
            while loop2 == True:
                choice = input("n, e, s, w ")
                if choice == "e":
                    start()
                elif choice == "s":
                    print ("Well done, next objective incoming.")
                    armoury()
                    loop2 = False
                else:
                    print ("You aren't permitted to go that way.")                    
    else:
        armoury()
        armour = False

def Interact2():
    interact2 = input("Would you like to interact? ")
    if interact2 == "yes":
        item2 = input("What would you like to take? ")
        if item2 == "blaster":
            TL50 = True
            print ("You have acquired a TL50 heavy blaster with a secondary fire function.")
            Interact3()                  
    else:
        canteen()
        TL50 = False
        thermaldetonator = False

def Interact3():
    interact3 = input("Would you like to interact? ")
    if interact3 == "yes":
        item3 = input("What would you like to take? ")
        if item3 == "thermal detonator":
            thermaldetonator = True
            print ("You have acquired a bag full of thermal detonators.")
            global loop3
            while loop3 == True:
                choice = input("n, e, s, w ")
                if choice == "n":
                    hanger()
                elif choice == "e":
                    print ("Well done, next objective incoming.")
                    detentionblock()
                elif choice == "s":
                    print ("Well done, next objective incoming.")
                    canteen()
                else:
                    print ("You aren't permitted to go that way.")                   
    else:
        canteen()
        thermaldetonator = False
        
start()
                
    #if armour == True:   
        #Interact2()
        #time.sleep(2)
        #Interact3()
    #else:
        #time.sleep(2)
        #print("INTRUDER DETECTED! You have been spotted and taken to the detention block.")
        #detentionblock()
