#2nd entry - creating link bewtween two screens
#3rd entry - creating database
#4th entry - creating tkinter button and screen for
#5th entry - creating cleaner homescreen and quit function
from tkinter import *
import pygame
import sqlite3
import random
Conn = sqlite3.connect("AccountDetails.db")
cursor = Conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY,
username text NOT NULL,
password text NOT NULL);""")
Conn.commit()

#This determines the size of the screen that will be created in the pygame section of the program.
x,y= 1280,1024
screen=pygame.display.set_mode((x,y),pygame.FULLSCREEN)


def Level1():
    play = True
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                
        TextDisplay1("What settings would you like to change?",(x/3),(y/3),500,25,(255,255,255),(125,125,125),Level1)
        Buttons1("Token Colour",(x/2)/2,((y/4)*3),200,25,(255,255,255),(125,125,125,),Level1)
        Buttons1("Background Colour",((x/3)*1.5),((y/4)*3),200,25,(255,255,255),(125,125,125),Level1)
        Buttons1("Quit",((x/4)*3),((y/4)*3),100,25,(255,255,255),(125,125,125),Level2)

        pygame.display.update()

        pygame.display.flip()

def TextDisplay1(txt,x,y,w,h,colour1,colour2,command):

    pygame.draw.rect(screen, colour1, (x,y,w,h))

    DisplayText = pygame.font.Font("JAi_____.TTF", 20)

    TextSurface, TextRectangle = RenderFont(txt, DisplayText)

    TextRectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(TextSurface, TextRectangle)


def Level(root):
    root.destroy()
    pygame.init()
    #This sets play as being true.
    play = True
    #This itteration allows the game to be played and will give the option for the player to quit the game.
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        TextDisplay1("Welcome to Connect 4.",(x/3),(y/3),500,25,(255,255,255),(125,125,125),Level1)        
        #These are the variables that are called for the Buttons1 function. It says the name, position of the button,
        #size of the box and the colour of the font.
        Buttons1("Play",(x/2)/2,((y/4)*3),100,25,(255,255,255),(125,125,125,),Maingame)
        Buttons1("Settings",((x/3)*1.5),((y/4)*3),100,25,(255,255,255),(125,125,125),Level1)
        Buttons1("Quit",((x/4)*3),((y/4)*3),100,25,(255,255,255),(125,125,125),Level2)
        #This will update a portion of the screen for the display.    
        pygame.display.update()
        #This will update the entirety of the screen for the display.
        pygame.display.flip()

#def dbupdate(root):
    #global e1
    #global e2
    #global e3
    #newid=input(e1)
    #newusername=input(e2)
    #newpassword=input(e3)
    #cursor.execute("""INSERT INTO users (id,username,password)
    #VALUES (?,?,?)""",(newid,newusername,newpassword))
    #Conn.commit()
    #level(dbupdate)

root = Tk()

T = Text(root, height=2, width=100)
T.grid(row=0)
T.insert(END, "Please insert your login details\n")
L1 = Label(root, text="ID Number").grid(row=4)
L2 = Label(root, text="Username").grid(row=5)
L3 = Label(root, text="Password").grid(row=6)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=4, column=2)
e2.grid(row=5, column=2)
e3.grid(row=6, column=2)
B = Button(root, text ="Login", width=100, command = lambda:Level(root))

    
B.grid()


def RenderFont(txt,font):
    #This line determines the colour of the text.
    TextSurface = font.render(txt, True, (0,0,0))
    #This returns the new text to be the text that appears on the text box.
    return TextSurface, TextSurface.get_rect()

#http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

#These are the colours I'll be using in my game.
Black = [0,0,0]
Grey = [211,211,211]
Yellow = [150,150,0]
Red = [150,0,0]

#Some colours have been stored in this dictionary.
Colourgame = { 1 : Grey,
               2 : Yellow,
               3 : Red
               }

size = 150

Grid = [
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1]
        ]

def TextDisplay2(txt,x,y,w,h,colour1,colour2,command):

    pygame.draw.rect(screen, colour1, (x,y,w,h))

    DisplayText = pygame.font.Font("JAi_____.TTF", 20)

    TextSurface, TextRectangle = RenderFont(txt, DisplayText)

    TextRectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(TextSurface, TextRectangle)


#def PlayerCheck():
    for X in Grid:
        for Y in Grid:
            if X == [2,3,3,3,3,1,1]:
                print ("Win")
        print(Y)
    #if Grid [X] in int(X == [3,3,3,3]):
        #TextDisplay2("You win.",(x/3),(y/3),500,25,(255,255,255),(125,125,125),Maingame)
    #else:
        #Maingame()

def TextDisplay3(txt,x,y,w,h,colour1,colour2,command):

    pygame.draw.rect(screen, colour1, (x,y,w,h))

    DisplayText = pygame.font.Font("JAi_____.TTF", 20)

    TextSurface, TextRectangle = RenderFont(txt, DisplayText)

    TextRectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(TextSurface, TextRectangle)


#def ComputerCheck():
    if Grid [X] in int(X == [2,2,2,2]):
        TextDisplay3("Computer win.",(x/3),(y/3),500,25,(255,255,255),(125,125,125),Maingame)
    else:
        Maingame()
                

def Maingame():
    #This sets play as being true in order to play the game.
    play = True
    #This sets counter to True in order for the player and the AI to take their turn placing a counter.
    counter = True
    #This itteration allows the game to be played and will give the option for the player to quit the game.
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            #This will get the mouse position    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                X = Position[1] // (size + 0)
                Y = Position[0] // (size + 0)
                #print(X)
                #print(Y)
                #while counter is True, it will allow the user to take their turn.
                while counter == True:
                    #This will move the counter down if the X value is not on the bottom row or if the colour is set to grey.
                    if X != 5 or Grid[X] == 1:
                        X = X + 1 
                        counter = True
                    #This will check if the row below in the specific column has an AI's token in it, therefore it will place the token
                    #in the position it is on.
                    elif X + 1 == Grid[2]:
                        Grid[X][Y] = 3
                        counter = False
                        #PlayerCheck()
                    #If anything else happens, then the counter position will be set to the player's token colour.
                    else:
                        Grid[X][Y] = 3
                        counter = False
                        #PlayerCheck()

                print(Grid)

                #0 1156 832
                #This is the variable I have used in order to allow the AI to operate.
                A = 1
                while A == 1:
                    #This will get the random number for the token positioning on the grid. 
                   X = random.randint(0,870) // (size + 0)
                   Y = random.randint(0,870) // (size + 0)
                   #print(X)
                   #print(Y)
                   #print("")
                   #This will move the counter down if the X value is not on the bottom row or if the colour is set to grey.
                   if X != 5 or Grid[X] == 1:
                       X = X + 1
                       A = 1
                   #This will check if the row below in the specific column has a player's token in it, therefore it will place the token
                   #in the position it is on.
                   elif Grid[X] == 3:
                       X = X - 1
                       Grid[X][Y] = 2
                       A = 2
                       counter = True
                   #If anything else happens, then the counter position will be set to the AI's token colour.
                   else:
                       Grid[X][Y] = 2
                       A = 2
                       counter = True

                

                    
                    

        screen.fill(Black)

        for row in range(6):
            for column in range(7):
                #circle(screen,color,(x,y),radius,thickness)
                pygame.draw.circle(screen, Colourgame[Grid[row][column]],(column*size+75, row*size+75),75, 0)

        Position = pygame.mouse.get_pos()
        X = Position[1] // (size + 0)
        Y = Position[0] // (size + 0)


        
        
        #This will update a portion of the screen for the display.    
        pygame.display.update()
        #This will update the entirety of the screen for the display.
        pygame.display.flip()

        


            


    
def Level2():
    pygame.quit()


#This is the function that determines the position, colour, size and hover function of the two buttons for the login / register screen.
def Buttons1(txt,x,y,w,h,colour1,colour2,command):
    #This allows the user to use there mouse when determining to click the buttons. The line gets the position of the cursor.
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #This selection determines the colour of each of the boxes depending on whether the cursor is hovering over a box or not.
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, colour2,(x,y,w,h))
        if click[0] == 1:
           command()

    else:
        pygame.draw.rect(screen, colour1,(x,y,w,h))
    #This sets the font that will be used for the buttons and the font size which will be 20.
    ButtonText = pygame.font.Font("JAi_____.TTF", 20)
    #This renders the font for the text overall to be the button text.
    TextSurface, TextRectangle = RenderFont(txt, ButtonText)
    #This determines the positions of the button text within the button so that it is central.
    TextRectangle.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(TextSurface, TextRectangle)




root.mainloop()

     

