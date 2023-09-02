#7> write a python program to print the even numbers of a specified list.
l = [12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100]
l1 =[]
for i in l:
    if i%2==0:
       l1.append(i)
print("Even:",l1)

# 8> write a python program to convert a list of character into a string.

##case 1
l = ['12','13','14','15','16']
print(l.copy()
      )
string = ''.join(l)
print(string)

##case 2
list = [5,1,6,9]
string = ""
for i in list:
    string+=str(i)
print(string)
print(type(string))
##case 3
lst = [5,6,9]
string = ""
for i in lst:
    string+=str(i)
integer = int(string)
print(type(integer))




    
    
