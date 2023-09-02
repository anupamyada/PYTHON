bill = 0
def coffee ():
    n=int(input("How many coffee?"))
    x= 20*n
    
    print("coffee bill = ",x)

def tea():
    n=int(input("How many tea?"))
    y = 10*n
    
    print("tea bill ",y)
def burger():
    n = int(input("How many burger?"))
    z=60*n

    print ("burger bill",z)

def pizza():
    n = int(input("how many pizza?"))
    p=110*n
    print("pizza bill",p)

print ('***Menu ***\n 1. coffee ->20,Rs'\
          '\n 2. tea -> 10,Rs' \
          '\n 3. burger -> 60, Rs' \
          '\n 4. pizza -> 110, Rs'\
          '\n 5. exit')

while True:
    ch = int(input('Enter your Choice:'))
    match ch :
        case 1:
            coffee()
        case 2:
            tea()
        case 3:
            burger()
        case 4:
            pizza()
        case 5:
            print('Total bill = ',bill)
            break
            
                
                                
