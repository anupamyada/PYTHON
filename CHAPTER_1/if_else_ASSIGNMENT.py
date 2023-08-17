##Q -1

'''def bill(Unit,RS):
    amount = Unit*RS
    if Unit>0 and Unit<100:
     print("No charge applied")

    elif Unit > 100 and Unit < 200:
     RS = 10,"PER UNIT"

    elif Unit >200:
     RS = 10,"per unit"
    print(amount)
RS = 5
Unit = float(input("Unit of the month:",))
bill(Unit,RS)'''


## Q2
def num():
    
    a= float(input("number:",))

    if a%11==0:
     print("number is divisible by 11")
    elif a%5==0:
        print("number is divisible by 5")
    else:
     print("neither divisible by 11 nor 5")

num()
