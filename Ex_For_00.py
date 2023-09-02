##
##'''limit = int(input("Enter an integer :"))
##
##print("the multiple of 3 upto and including",limit,"are:")
##for i in range(3,limit+1,3):
##    print(i)
##
##    '''
##
##'''for i in range(1,10,1):
##    print(i)
##'''
##i = 3
##while i<=10:
##    if i ==3 or  i==6:
##        i+=1
##        continue
##    else: 
##      print(i)
##      i+=1
##    ## Doubt: It does not work upon "and"
##
##'''i = 1
##while i<=50:
##    if i==11 or i ==22 or i==25 or i ==30 or i==33:
##        
##        continue
##    else:
##        print(i)
##        i+=1
##        
##''' ## Doubt: why It stopped here.and why i need to write increment in "if" and else also. but while using break i dont need to write both places.
##'''i=1
##while i<=20:
##    if i==11 and i==14 or i==16 or i==18 or i==20:
##        i+=1
##        continue
##    else:
##       print(i)
##       i+=1'''
#### Doubt : why it is including when I used "and " Operators
##
##'''i = 1
##while i<=10:
##    if i==7:
##        break
##    else:
##        print(i)
##        i+=1
##print("Loop Terminated")'''
##
##'''
##count = 0
##while count<5:
##    print("count is :",count)
##    count+=1
##
#### Q1
##
##for i in range(1,11,1):
##    print(i)
##'''
#### Q2
##
##list = ["apple","banana","pomigranate","grapes","kiwi"]
##
##for num in list:
##    print(list)
##
##
##
##
##
##
##
##

##'''i=1
##while  i<=10:
##    
##    if i==6:
##        i+=1
##        continue
##    print(i)
##    i+=1
##
##''''''
##i=1
##while i<=10:
##    
##     if i==6:
##         break
##     print(i)
##     i+=1
##     
##       ## i+=1
##'''
##for i in range(10):
##    if i==2 or i==5:
##       continue
##    print(i)
##for i in range(2,20,2):
## print(i)
##for i in range(1,20,2):
##    print(i)
##    

##i = 1
##while i<10:
##    print(i)
##    i+=2

bill = 0
def coffee():
    global bill
    n=int(input("how many coffee u want ??"))
    x = 20*n
    bill = bill + 20*N
    print("coffee bill=",x)

def tea():
    global bill
    n = int(input("how many tea do you want ??"))
    y = 10*n
    bill = bill +10*n
    print("tea bill =",y)

def burger():
    global bill
    n= int(input("how many pizza u want ??"))
    p = 60*n
    bill = bill +110*n
    print("burger bill =",z)

def pizza():
    global bill
    n=int(input("how many pizza u want ??"))
    p = 110*n
    bill = bill +110*n
    print("pizza bill=",p)

print("***Menu ***\n\coffee ->20 Rs"\
      "\n 2. tea -> 10 Rs"\
      "\n 3. Burger -> 60 Rs "\
      "\n 4. Pizza -> 110 Rs"\
      "n 5. Exit")
while True:
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            coffee()

    
    
    

    
       
    
