a=int(input("Enter a number : "))
b=a
c=str(a)
d=len(c)
sum=0
while a>0:
    e=a%10
    sum=sum+(e**d)
    a=a//10

if sum==b:
    print("Armstrong number")
else:
    print("Not an armstrong number")