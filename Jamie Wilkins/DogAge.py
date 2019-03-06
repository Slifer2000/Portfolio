DogAge = int(input("How old is your dog? "))
if DogAge <= 2:
    DogAge1 = (DogAge)*12
    print ("Your dog is " + str(DogAge1) + " years old in human equivalent.")
else:
    DogAge1 = (DogAge)*6
    DogAge1 = (DogAge1)+24
    print ("Your dog is " + str(DogAge1) + " years old in human equivalent.")
