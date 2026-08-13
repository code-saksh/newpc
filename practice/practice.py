
a=int(input("Enter a number : "))
c=str (a)
d=len(c)
sum=0
rev=""
while a>0:
    b=a%10
    rev=rev+ str(b)

    a=a//10

e= int(rev[0])
f=int(rev[d-1])
sum=sum+e+f 
print(sum)