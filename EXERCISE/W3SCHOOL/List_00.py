l1=[1,2,3,4,5]
l1.append("hello")
print(l1)
l2 = [11,55.6,"pune"]
l2.append(33.3)
print(l2)
l1.insert(1,47)
print(l1)
s1 = [11,22,355.6,"p"]
s1.extend([9,1,4])
print(s1)
s2 = [11,22,33,44,55]
####s2.pop(3)
##print(s2)
##s2.remove(22)
##print(s2)
##s2.clear()
##print(s2)
print(s2.count(11))
print(s2)
print(s2.index(33))
s3 = s2.copy()
print(s3)
s3.sort()
print(s3)
s3.sort(reverse = True)
print(s3)