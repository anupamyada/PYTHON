## Q3
'''def coord():

    a=float(input("enter num1:",))
    b=float(input("enter num2:",))
    x = (a,b)

    if a>0 and b > 0 :
        print("coorinate 1")
    elif a<0 and b>0:
        print("coordinate 2")
    elif a<0 and b<0:
        print("coordinate 3")
    elif a>0 and b<0 :
        print("coordinate 4")
coord()'''

## Q4
import math
def perc():

    a= input("enter the name of student:")
    b= input ("enter the roll number of the student:")
    c1= float(input("phy:"))
    c2= float(input("chem:"))
    c3= float(input("ca:"))
    s= c1+c2+c3
    p = (s/300)*100
    print(p)
    if p<55:
       print("3rd division")
    elif p >65 and p<75:
        print("2nd")
    elif p>75:
        print("1st division")
perc()        

    
    
