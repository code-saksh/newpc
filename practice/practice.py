
a=int(input("Enter a number : "))
b=a
sum=0 
while a>0:
    c=a%10 
    sum=sum+c
    a=a//10

if b%sum==0:
    print("Niven number")
else:
    print("Not a Niven number")

    