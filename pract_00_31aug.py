##ex01
l1 = [11,12,33,44]
print('sum',sum(l1))

##ex02
l = [1,2,3,4,5]
x = 1
for i in l :
    x*=i
print("multiplication =", x)

##ex03
l1 = [11,12,13,14,15,16,17]

## ex04
l1 = [11,12,13,14,15,16,17,18,19,20]
for i in l1:
    if i%2 ==0:
        print(i)

##ex05

l1 = [1,2,3,4,5,6,7,8,9]
l2 =[]
for i in l1:
    x = i**2
    l2.append(x)
    print("list of square", l2)

## ex06
    l1 =[10,20,30,40]
    l2 =[100,200,300,400]
    for i in range(len(l1)):
        print(l1[i],l2[3-i])
    
