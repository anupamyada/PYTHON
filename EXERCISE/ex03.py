Amount = 2000
def withdrawl():
    global Amount
    w = float(input("Enter withdrawl amount:"))
    rm= Amount - w
  
    print("remaining amount:",rm)
    

def deposit():
    M = float(input("Account Balance:"))
    D= float(input("Deposit amount:"))
    TM = M + D

    print("account balance:",TM)

def bal():
    M = 30000
    D=1000
    w = 1500
    B = M +D-w
    print(B)
print("***Menu***\n 1. Withdrawl"\
      "\n 2.Deposit"\
      "\n 3.Account balance")

while True:
    ch = int(input("choice:"))
    match ch:
        case 1:
          withdrawl()
        case 2:
          deposit()
        case 3:
          bal()
        case _:
            print("Error")
            break 
