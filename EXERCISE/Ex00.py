##while True:
## def bill():
##    u=float(input("Enter Unit of electricity?"))
##   
##
##    if u==0:
##        print("free")
##    elif u>=101 and u==200:
##        bill = u*5 +0.2*(u*5)
##        print("bill",bill,"rs")
##    elif u>200:
##        bill =u*10+0.2*(u*10)
##        print("bill",bill,"rs")
##    
##bill()   
##Doubt : while loop is not working here


##def bill():
##    u=float(input("Enter Unit of electricity?"))
##   
##
##    if u==0:
##        print("free")
##    elif u>=101 and u==200:
##        bill = u*5 +0.2*(u*5)
##        print("bill",bill,"rs")
##    elif u>200:
##        bill =u*10+0.2*(u*10)
##        print("bill",bill,"rs")
##bill() 
##   Doubt: why upon taking 101 it is not giving any output 



def bill():
    u=float(input("Enter Unit of electricity?"))
   
while True:
    if u==0:
        print("free")
    elif u>=101 or u==200:
        bill = u*5 +0.2*(u*5)
        print("bill",bill,"rs")
    elif u>200:
        bill =u*10+0.2*(u*10)
        print("bill",bill,"rs")
bill() 


  
