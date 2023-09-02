def leap():
    Y = int(input("Enter Year:"))

    if Y%4==0 and Y%400 ==0:
        print("This is leap Year")
    elif Y % 100==0:
        print("Ordinary year")
    else:
        print("ordinary year")
leap()
