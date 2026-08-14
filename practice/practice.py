
a=int(input("Enter a number : "))
b=a
sum=0

while a>0:
    sum1=1
    c=a%10
    for i in range(1,c+1):
        sum1=sum1*i
    sum=sum+sum1
    a=a//10

if sum==b:
    print("Strong number")
else:
    print("Not a Strong number")