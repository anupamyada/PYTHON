print("****\\\Menu\\*****"'\n 1. employee'\
      '\n 1. show employee details'\
      '\n 3. enter name of employee'\
      '\n 4. update employee details')

while True:
    ch = int(input("enter your choice:"))
    match ch:
            case 1:
                e = {"seeta":123,"geeta":456,"reeta":789}
                print(e)

            case 2:
                for i,j in e.items():
                    print(i,j)
            case 3:
               print(e.keys())

            case 4:
                e["seeta"]=9354542762
                print(e)
##
##                case_:

        

      
