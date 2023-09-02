## case 1

def Area():
    l=10
    b=20
    A=l*b
    print("Area of the room", A,"mm**2")
Area()


## Case 2

def Area(l,b):
    a=l*b
    print("area of room",a,"mm**2")
l=10
b=20
Area(l,b)

## compute the area of the room
#
# Read the dimension from the user

length = float(input("enter the length of the room in feet:"))
width =  float(input("enter the width of the room in feet:"))

# compute the area of the room
area = length*width

# Display the result
print("the area of the room is",area,"square feet")
