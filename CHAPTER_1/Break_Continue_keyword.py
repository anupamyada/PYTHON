##
for i in range(1,11,1):
    if i==4 or i==7:
        continue
    else:
        print(i)
##
i = 1
while i<=10:
    if i==4 or i==7:
        i+=1
        continue
    else:
     print(i)
     i+=1
##

i = 1
while i<=50:
    if i==11 or i ==22 or i ==33 or i==44:

        i+=1
        continue
    else:
     print(i)
    i+=1
##

i = 1
while i<=10:
    if i==7:
        break
    else :
        print(i)
    i+=1
print('loop terminate')
