## Practice01

def add():
    x = 10
    y=20
    print("addition: ",x+y)

def sub():
    x=12
    y=15
    print("subtraction: \n",y-x)

add()
sub()
##practice 02
## typecasting
y = float(input("enter any number"))
print(y)
print(type(y))

## practice 03

def add(x,y):
    z=x+y
    print("addition :",z)
##add()
##add(1,2,3)

def per(s1,s2,s3,s4,s5):
    sum1 = s1+s2+s3+s4+s5
    percentage = (sum1/500)*100
    print("percentage of student =", percentage)
s1 = int(input("enter marathi marks:"))
s2 = int(input("enter maths marks:"))
s3 = int(input("enter bio marks:"))
s4 = int(input("enter phy marks:"))
s5 = int(input("enter chem marks:"))

per(s1,s2,s3,s4,s5)

