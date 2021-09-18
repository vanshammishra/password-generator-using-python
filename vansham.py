import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4 = string.punctuation
    n = 0 # number of attempts a user must be given
    #print(s4)

    #passlen = int(input("Please enter the length of the password\n"))

    while True:
        
            try:
            
             passlen = int(input("Please enter the length of the password\n"))
             s = []
             s.extend(list(s1))
             s.extend(list(s2))
             s.extend(list(s3))
             s.extend(list(s4))
             #print(s)
             random.shuffle(s)
             #print(s)
             # print("".join(s[0:passlen])) this is the first method to generate the random password
             print("Your random password is: ")
             print("".join(s[0:passlen]))            
             break
            except ValueError:

                print("You have entered something wrong Please enter a valid number in digits\n")
        
            n = n+1
            

      


    

