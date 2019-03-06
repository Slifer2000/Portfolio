Teddy = int(input("How many teddy bears have you made? "))
Hours = int(input("How many hours have you worked? "))
TeddyMoney = (Teddy)*2
HoursMoney = (Hours)*5
if TeddyMoney > HoursMoney:
    print ("You have earned " + "£ " + str(TeddyMoney))
else:
    print ("You have earned " + "£" + str(HoursMoney))
