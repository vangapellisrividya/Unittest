def sum(self,num1,num2):
    
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return num1+num2
    else:
        raise ValueError(" num1 and num2 must be int or float")

def mul(self,num1,num2):
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return num1*num2
    else:
        raise ValueError(" num1 and num2 must be int or float")

def sub(self,num1,num2):
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return num1-num2
    else:
        raise ValueError(" num1 and num2 must be int or float")

