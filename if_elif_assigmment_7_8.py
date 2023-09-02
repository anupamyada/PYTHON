## 7

def profit():
    c=int(input("enter any number:"))
    s=int(input("enter any number:"))
    p= s-c
    p_1=(p/c)*100
    print(p_1)

    if p_1<0:
        print("loss")
    elif p_1 >0:
     print("profit")

profit()

## Q8

def month():
    a=int(input("enter any number:"))

    if a ==1:
      print("jan")
    if a==2:
      print("feb")
    elif a== 3:
        print("mar")
    elif a==4:
        print("april")
    
month()

