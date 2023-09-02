'''## Bottle Deposits
#
# Take inputs from the users
n1= int(input("number of bottle of size less than 1 liter:"))
n2=int(input("number of bottle of size more than 1 litre:"))
Rs1=0.1 
Rs2=0.25 

T= Rs1*n1 + Rs2*n2

print("total refund amount:", T,"$")
       
'''

'''# Case 2

def Totle():
    n1 = int(input("number of bottle less than 1 ltr :"))
    n2 = int(input("number of bottle more than 1 ltr :"))
    Rs1=0.1
    Rs2=0.25

    T = n1*Rs1 + n2*Rs2

    print("return amount:",T)

Totle()
'''

## case 3

def total(n1,n2,Rs1,Rs2):

    T = n1*Rs1 + n2*Rs2

    print("return amount:",T)
n1 = int(input("number of bottle less than 1 ltr :"))
n2 = int(input("number of bottle more than 1 ltr :"))
Rs1=0.1
Rs2=0.25
total(n1,n2,Rs1,Rs2)



