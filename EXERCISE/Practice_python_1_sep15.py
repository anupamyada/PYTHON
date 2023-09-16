##functions

def add():
    x=10
    y=30
    print("Addition\n=",x+y)
def sub():
    x=12
    y=15
    print("substraction\n=",y-x)
def mul():
    x=20
    y=50
    print("multiplication\n=",x*y)
def div():
    x=10
    y=2
    print("division\n=",x/y)

add()
sub()
mul()
div()

##type casting
y = int(input("enter any number:"))
print(y)
print(type(y))

##user defined function
def add(x,y):
    z=x+y
    print("addition=",z)
add(2,4)
