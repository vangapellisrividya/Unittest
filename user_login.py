'''
@Date:  2021-11-28	
@Author:Srividya
@Title : User_login

'''

import re
    
def firstname(self):
    """"
        Description: this function will take the input from user as firstname
        Parameter: self
        Return: firstname
    """

    firstname= input("enter the Firstname: ")
    pattern="^[A-Z]{1}|[a-z][.]+\s[A-Z][a-z]+$"
    result=re.match(pattern,firstname)
    if result:
        return firstname
    else:
        raise TypeError("name must be in string format")

def lastname(self):
    """"
        Description: this function will take the input from user as lasstname
        Parameter: self
        Return: lastname
    """
    lastname= input("enter the Lastname: ")
    pattern="^[A-Z]{1}|[a-z][.]+\s[A-Z][a-z]+$"
    result=re.match(pattern,lastname)
    if result:
        return lastname
    else:
        raise TypeError("name must be in string format")

def email(self):
    """"
        Description: this function will take the input from user as email
        Parameter: self
        Return: emai
    """
    email= input("enter the E-mail: ")
    pattern="^[a-zA-Z0-9]+([.#_$+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.][a-zA-Z]{2})?$"
    result=re.match(pattern,email)
    if result:
        return email
    else:
        raise ValueError("email must be in given format")

def phonenumber(self):
    """"
        Description: this function will take the input from user as email
        Parameter: self
        Return: emai
    """
    phonenumber= input("enter the PhoneNumber: ")
    pattern="((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
    result=re.match(pattern,phonenumber)
    if result:
        return phonenumber
    else:
        raise ValueError("PhoneNumber must be in given format")

def password(self):
    """"
        Description: this function will take the input from user as password
        Parameter: self
        Return: password
    """
    password= input("enter the Password: ")
    #pattern= "^[A-Z]+[a-zA-Z](\s)*$"
    pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,8}$"
    result=re.match(pattern,password)
    if result:
        return password
    else:
        raise ValueError("password must be in given format includes A,a,0-9,and special characters ")
    

# if __name__=='__main__':
    # firstname(self="")
    # lastname(self="")
    # email(self="")
    # password(self="")
    # phonenumber(self="")
