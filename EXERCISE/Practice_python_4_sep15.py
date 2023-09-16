def add():
    x = int(input("a"))
    y= int(input("b"))
    z= x+y
    print("addition:\n",z)

def sub():
    x = int(input("a"))
    y= int(input("b"))
    z= x-y
    print("substraction:\n",z)

def     mul():
    x = int(input("a"))
    y= int(input("b"))
    z= x*y
    print("multiplication:\n",z)

def div():
    x = int(input("a"))
    y= int(input("b"))
    z= x/y
    print("division:\n",z)

print("**\\Menu\\**\n"" 1. addition"\
      "\n 2. Substraction"\
      "\n 3. multiplication"\
      "\n 4. division")
while True:
 ch = int(input("Enter your choice:"))
 match (ch):
    case 1:
        add()
    case 2:
        sub()
    case 3:
        mul()
    case 4:
        div()
    case _:
        print("invalid choice")
        break
