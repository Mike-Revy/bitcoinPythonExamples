y = 3                                   # first we associate the name 'y' with the number 3

def print_stuff():              # then we associate the name print_stuff with this function
    print ("calling print_stuff")          #  (***)
    print (y)                                                                            
    z = 4     
    print (z)                
    print ("exiting print_stuff")

print_stuff()                      # we call print_stuff and the program execution goes to (***)
print (y)                              # works fine
print (z)
                               # NameError!!!