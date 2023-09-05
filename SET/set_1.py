##1

s = {1,2,3,4.5,"abc",False}
print(type(s))

## set

##2
s = {}
print(type(s))
## dict

##3
s = {1,2,3,4,5}
s.add(50)
print(s)

##4
s = {1,2,3,4,5}
s.add(45)
print(s)

##5
s = {1,2,3,4,5}
s.add(50)
s.add(45)
print(s)

##6
s = {1,2,3,4,5}
s.update({20,30,40})
print(s)

##7
s = {1,2,3,4,5}
s.update([20,30,40])
print(s)

##8
s = {5,6,7,8,9}
s.update((1,2,3))
print(s)

