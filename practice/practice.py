
def convert(temp  , to):
    if to == "F":
        tem = temp*1.8 + 32 
        return tem 
    elif to ==  "C": 
        tem= (temp-32)/1.8
        return tem 

a=int(input("Enter temperature :"))
b= input("Enter C or F to convert :")
print("The converted temperature is :" , convert(a,b))