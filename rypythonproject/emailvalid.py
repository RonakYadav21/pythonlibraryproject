#check  email validator manually
email=input("enter email  ")
if len(email)>=6:
    if email[0].isalpha():
        if '@' in email and email.count('@')==1:
            if email.islower():
                if email[-3]=='.' or email[-4]=='.':
                    if email.isspace()!=True:
                        for i in email:
                            if i.isdigit():
                                continue
                            elif i =='!' or i=='#' or i=='%' or i=='$' or i=='^' or i=='%' or i=='*' or i=='()' or i=="~":
                                print("Wrong Email")  
                            else:pass
                        print("Correct Email")          
                    else:
                        print("Wrong Email 6")
                else:
                    print("Wrong Email 5")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")



# using valid_email from valid_email lib
"""from validate_email import validate_email(thrid part lib)
email=input("enter email")
isvalid=validate_email(email)
if isvalid:
    print("Valid Email")
else:
    print("Invalid Email")

#check for valid email using regular expression
"""
# by using regular expression
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
  if(re.fullmatch(regex, email)):
        print("Valid Email")
 
  else:
        print("Invalid Email")
email=input("enter email  ")
check(email)

    

