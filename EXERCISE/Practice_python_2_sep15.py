##case1
def perc(a,b,c,d,e):

    sum = a+b+c+d+e

    percentage= (sum/500)*100
    print("percentage marks:",percentage)

perc(20,30,40,50,60)
a=int(input("enter 1st sub marks:"))
b=int(input("enter 2nd sub marks:"))
c=int(input("enter 3rd sub marks:"))
d=int(input("enter 4th sub marks:"))
e=int(input("enter 5th sub marks:"))
perc(a,b,c,d,e)

##return keyword
def add():
    p=10
    q=30
    r=p+q

    return r
print(add())

##ex
balance= 2000
def withdraw():
    global balance
    amt=int(input("enter amount for withdraw:"))
    balance = balance - amt
    print("withdraw successful")
    return balance
bal = withdraw()
print(bal)

##ex
balance = 2000
def withdraw():
    global balance
    amt= int(input("enter withdraw amount:"))
    balance = balance -amt
    print("withdraw successful")
    return balance
bal = withdraw()
print(bal)


##ex
p = int(input("Enter pankaj age:"))
s= int(input("Enter sachin age:"))
if p<s:
    print("Pankaj is younger")
else:
    print("sachin is younger")

##ex
p = int(input("Enter pankaj age:"))
s= int(input("Enter sachin age:"))
if p<s:
    print("pankaj is younger")
elif p==s:
    print("both are of equal age")
else:
    print("sachin is younger")
    


