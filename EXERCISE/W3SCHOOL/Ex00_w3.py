##Arguments

##Ex01
##def my_function(fname):
##	print(fname +"Refsnes")
##my_function("email")
##my_function("Tobias")
##my_function("Linus")


##Parameters or Arguments?
##Ex 02
'''##def my_function(fname, lname):
##  print(fname + " " + lname)
##
##my_function("Emil", "Refsnes")'''
##
##def my_function(fname,lname):
##    print(fname , lname)
##my_function("email","refsnes")

##'''
##Arbitrary Arguments, *args
##
##EX03
##def my_function(*kids):
##  print("The youngest child is " + kids[2])
##
##my_function("Emil", "Tobias", "Linus")
##
##
def my_function(*kids):
    print("the youngest child is " + kids[2])

my_function("email", "Tobias", "Linus")

'''Doubt: why in above example + is written , what will be different in output using comma and +'''
def my_function(*kids):
    print("the youngest child is " , kids[2])
my_function("email","Tobios","Linus")

##\\\\\\\\\\\\\*********Keyword Arguments******\\\\\\\\\\
##
##def my_function(child3, child2, child1):
##  print("The youngest child is " + child3)
##
##my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
##
##def my_function(child3,child2,child1):
##    print("youngest child " + child3)
##
##my_function(child1="Email",child2 = "Tobias", child3 = "lenus")

## Q 01
## What is the difference between argument and keyword argument
