import sqlite3
import time
IMDB = sqlite3.connect(":memory:")
c = IMDB.cursor()
print("Time to enter Actors.")
time.sleep(1)
c.execute("""CREATE TABLE IF NOT EXISTS Actor(id integer PRIMARY KEY,
Actorname text NOT NULL,
film text NOT NULL,
dateofbirth date NOT NULL);""")
IMDB.commit()
yes = True
while yes == True:
    newid = input("Enter ID number: ")
    newActorname = input("Enter name: ")
    newfilm = input("Enter film: ")
    newdateofbirth = input("Enter dateofbirth: ")
    c.execute("""INSERT INTO Actor (id,Actorname,film,dateofbirth)
    VALUES (?,?,?,?)""",(newid,newActorname,newfilm,newdateofbirth))
    IMDB.commit()
    c.execute("select * from Actor")
    for x in c.fetchall():
        print (x) 
    Continue = input("Do you wish to continue? ")
    if Continue == "yes":
        yes = True
    else:
        yes = False

time.sleep(1)
print("Time to enter Directors.")
time.sleep(1)
c.execute("""CREATE TABLE IF NOT EXISTS Director(id integer PRIMARY KEY,
Directorname text NOT NULL,
film text NOT NULL,
dateofbirth date NOT NULL);""")
IMDB.commit()
yes2 = True
while yes2 == True:
    newid = input("Enter ID number: ")
    newDirectorname = input("Enter name: ")
    newfilm = input("Enter film: ")
    newdateofbirth = input("Enter dateofbirth: ")
    c.execute("""INSERT INTO Director (id,Directorname,film,dateofbirth)
    VALUES (?,?,?,?)""",(newid,newDirectorname,newfilm,newdateofbirth))
    IMDB.commit()
    c.execute("select * from Director")
    for x in c.fetchall():
        print (x) 
    Continue = input("Do you wish to continue? ")
    if Continue == "yes":
        yes2 = True
    else:
        yes2 = False


time.sleep(1)
print("Time to enter Films.")
time.sleep(1)
c.execute("""CREATE TABLE IF NOT EXISTS Film(id integer PRIMARY KEY,
Filmname text NOT NULL,
rating text NOT NULL,
dateofrelease date NOT NULL);""")
IMDB.commit()
yes3 = True
while yes3 == True:
    newid = input("Enter ID number: ")
    newFilmname = input("Enter name: ")
    newrating = input("Enter rating 1-5: ")
    newdateofrelease = input("Enter dateofrelease: ")
    c.execute("""INSERT INTO Film (id,Filmname,rating,dateofrelease)
    VALUES (?,?,?,?)""",(newid,newFilmname,newrating,newdateofrelease))
    IMDB.commit()
    c.execute("select * from Film")
    for x in c.fetchall():
        print (x) 
    Continue = input("Do you wish to continue? ")
    if Continue == "yes":
        yes3 = True
    else:
        yes3 = False
        IMDB.close() 
