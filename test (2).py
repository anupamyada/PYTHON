
'''
Write a python program to to calculate percentage of student
using parameterised function take 5 subject marks as an
input from user
'''


    



def perc(s1,s2,s3,s4,s5):#parameters
    sum1 = s1 + s2 + s3 + s4 + s5

    percentage = (sum1/500)*100

    print('Percentage of student=',percentage)


m1 = int(input('Enter marathi marks:'))#55
m2 = int(input('Enter Math marks:'))
m3 = int(input('Enter Bio marks:'))
m4 = int(input('Enter Physics marks:'))
m5 = int(input('Enter Chemistry marks:'))


perc(m1,m2,m3,m4,m5)#arguments


