## Q11
def bike_cost():
    price=int(input("enter bike price"))

    if price > 100000:
        print("tax is 15%")
    if price>50000 and price <=100000:
        print("tax is 10%")
    if price <= 50000:
        print("tax is 5%")
bike_cost()

## Q12
def leap():
    yr=int(input("enter the year:"))

    L =



## Q13

def age():
    a1= int(input("enter age1:"))
    a2= int(input("enter age2:"))
    a3= int(input("enter age3:"))
    a4= int(input("enter age4:"))

    if a1<a2 or a1<a3 or a1<a4:
        print("print a1 youngest")

    elif a2<a1 or a2<a3 or a2<a4:
        print("a2 is youngest")
        
    elif a3<a1 or a3<a2 or a3<a4:
        print("a3 youngest")
        
    else: 
        print("a4 youngest")
            
age() 
