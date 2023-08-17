def add():
    x = int(input("Enter 1st number"))
    y = int(input("Enter 2nd number"))
    z = x+y
    print("Addition=",z)
def sub():
    x = int(input("Enter 1st number"))
    y = int(input("Enter 2nd number"))
    z = x-y
    print("Substraction=",z)
def mul():
    x = int(input("Enter 1st number"))
    y = int(input("Enter 2nd number"))
    z = x*y
    print("Multiplication=",z)
def div():
    x = int(input("Enter 1st number"))
    y = int(input("Enter 2nd number"))
    z = x/y
    print("Division=",z)
    
print('***Menu***\n 1. Addition '\
      '\n 2.Substraction '\
      '\n 3. Multiplication'\
      '\n 4. Division '\
      )
ch = int(input("Enter your choice :"))
'''match (ch):
    case 1:
        add()
    case 2:
        sub()
    case 3:
        mul()
    case 4:
        div()
    case _ :
        print("invalid choice")'''
if ch ==1:
    add()
elif ch==2:
    sub()
elif ch ==3:
    mul()
elif ch==4:
    div()
else:
    print("invalid chice")

        
