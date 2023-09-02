'''def grand_total():
    n1=float(input("number of plate ordered:"))
    Rs = float(input("price of plate without tax:"))
    Rs1= 0.07*Rs
    Rs2= 0.18*Rs
    T = n1*Rs + Rs1+  Rs2
    print("grand total bill:",T)
grand_total()

'''
'''x=12
name = "Anupam"
numCookies = 13
print("%.2f" % x)
print("%s ate %d cookies!" % (name, numCookies))'''

'''# Read the names from the user
first = input("Ente the first name:")
last = input("Enter the last name:")

# Concatenate the strings
both = last + "," + first

# Display the Result
print(both)
                     
'''

'''# Read the name from the user
first = input("Enter your first name: ")

# Compute Its Length
num_chars = len(first)

# Display the result

print(" Your first name contains",num_chars, "characters")'''

# read the user's name
first = input("Enter your first name: ")
middle = input("Enter your middle name:")
last = input("Enter your last name : ")

# Extract the first character from each string and concatenate them

initials = first [0] + middle[0] + last[0]

# Display the initials

print("Your initials are",initials)
