##case 1

def myfunc(n):
    return abs(n-50)


l1 = [1,2,3,4,5]
l1.sort(key = myfunc)
print(l1)

l2 = ["banana","Orange","kiwi","cherry"]
l2.sort(key=str.lower)

print(l2)

##case 2
####Note: what is case sensitive & insensitive in case of list
##sorting.
l2.reverse()
print(l2)
