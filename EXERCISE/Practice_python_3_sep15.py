def perc():
    s1 = int(input("Enter the Hindi marks:"))
    s2 = int(input("Enter the English marks:"))
    s3 = int(input("Enter the Maths marks:"))
    s4 = int(input("Enter the Physics marks:"))
    s5 = int(input("Enter the Chemistry marks:"))

    s=s1+s2+s3+s4+s5
    per = (s/500)*100
##    print (per)
    

    if per >=0 and per<35:
        print("fail")
    elif per>35 and per<55:
        print("d-grade")
    elif per >55 and per<65:
        print("c-grade")
    elif per >65 and per<75:
        print("b-grade")
    elif per>75 and per<85:
        print("a-grade")
    elif per >85 and per<=100:
        print("a+ grade")
    else:
        print("invalid")
        return per
     
perc()


