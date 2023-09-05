##1

s = {1,2,3,4,5}
s.remove(4)
print(s)
##result will be {1,2,3,5}

## 2

s = {1,2,3,4,5}
s.remove(10)
print(s)
## result will show --key error :10

##3
s= {1,2,3,4,5}
s.discard(1)
print(s)

## results: {2,3,4,5}

##4
s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}
print(s1|s2)
print(s1.union(s2))
## both way we can represent union

##5
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1&s2)
print(s1.intersection(s2))
