
a=int(input("Enter a number : "))
c=a
rev=""
while a>0:
    b=a%10
    rev=rev+str(b)
    a=a//10

print(rev)