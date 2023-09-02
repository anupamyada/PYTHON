##ex 01
l1 = ["apple","banana","cherry","kiwi","mango"]
l2 = [x for x in l1 if "a" in x]
print(l2)


##ex02
l2 = [ x for x in l1 if "e" in x]
print(l2)


##ex03

l = [x for x in l1 if x!="apple" and x!="mango"]
print(l)

##ex04
l = [x if x!="banana" else "orange" for x in l1]
print(l)
