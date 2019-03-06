numpeople = input("How many people are taking the journey? ")
nummiles = input("How many miles is your trip? ")
price = 3
if int(numpeople) < 5:
    price = price
    if int(nummiles) == 1:
        price = price
    elif int(nummiles) > 1:
        price = ((price * 2) - 1)
elif int(numpeople) >= 5:
    price = (price * 2)
print (("Your price is £") + str(price))
