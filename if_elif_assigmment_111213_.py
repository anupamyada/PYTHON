## Q14
def attendence(T,A):
    pec = (T-A)/T*100
    print("% attendence:",pec)
    return pec
T=int(input("Enter total working days:"))
A=int(input("enter total absent days:"))

a=attendence(T,A)


if a <75:
   print("Student not eligible to sit in exam")
else:
    print("eligible to sit in exam")
    
## Q15
Y = int(input("Enter Year of Service:"))
S = int(input("enter current salary:"))

if Y > 10:
    perc_b=10 
    print(perc_b,"%")
elif Y>=6 and Y<=10:
    perc_b = 8
    print(perc_b,"%")
else:
   perc_b = 5
   print(perc_b,"%")
   
b = (perc_b*S)/100
print(b,"Rs")
