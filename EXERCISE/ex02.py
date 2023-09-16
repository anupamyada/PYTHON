Amount = 2000
def withdrawl():
    global Amount
    w = float(input("Enter withdrawl amount:"))
    rm= Amount - w
  
    print("remaining amount:",rm)
    if rm<1000:
         print("can't Withdraw bcoz amount is low")
    else:
         print("balance:",rm)
withdrawl()


##def deposit():
##    M = float(input("Account Balance:"))
##    D= float(input("Deposit amount:"))
##    TM = M + D
##
##    print("account balance:",TM)
##deposit()


##def deposit(M,D):
##    
##    TM = M + D
##
##    print("account balance:",TM)
##    
##M = float(input("Account Balance:"))
##D= float(input("Deposit amount:"))
##
##deposit(M,D)
