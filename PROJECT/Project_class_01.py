class employee:
    print("1.email id \n 2. name \n 3.address\n 4. salary \n5. adhar\
          \n 6. contact")
    def __str__(self):
        return (f'1.emailId={self.emailId}\n 2. name={self.name} \
                  \n 3. address={self.address} 4.salary={self.salary}\
                  \n 5.adhar = {self.adhar} \n 6. contact = {self.contact}')
    def display(self):
        while True:
            ch = int(input("Enter your Choice:"))
        
        
            match (ch):
          
                 case 1:
                    print()
                    print("email Id of employee:")
                    print()
                    l = ["Ram@gmail.com","shyam@gmail.com","krish@gmail.com"\
                  "vishal@gmail.com","ravi@gmail.com"]
                    for i in l:
                      print(i)
                      print()
                    print()
                
                 case 2:
                    print()
                    print("name of corresponding employee:")
                    print()
                    m = ["Ram","Shyam","krish","vishal","ravi"]
                    d=dict(zip(m,l))
                    print(d)
                    for i,j in d.items():
                        print(i,j)
                        print()
                    print()     
                 case 3:
                    add = ["Pune","nashik","mumbai","nagpur","satara"]

                    a=dict(zip(m,add))
                    print(a)
                    print()
                    for i,j in a.items():
                        print(i,j)
                        print()
                 case 4:
                     s=[1000,2000,3000,4000,5000]
                     S=dict(zip(m,s))
                     print(S)
                     print()
                     for i, j in S.items():
                         print(i,j)
                         print()
                 case 5:
                     print("employee and corresponding ahar number")
                     print()
                     adhar = [123,234,345,456,567]
                     Adhar = dict(zip(m,adhar))
                     print(Adhar)
                     print()

                     for i,j in Adhar.items():
                         print(i,j)

                         print()
                 case 6:
                     print("employee and their corresponding contact:")
                     print()
                     c=[123,123,123,123,123]
                     C=dict(zip(m,c))
                     print(C)
                     for i,j in C.items():
                         print(i,j)
                         print()
                     break

e=employee()
e.display()

##             
