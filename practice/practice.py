
a=int(input("Enter a number : "))
c=a
rev=""
while a>0:
    b=a%10
    rev=rev+str(b)
    a=a//10

rev= int (rev)
if rev==c:
    print(f"{c} is a Palindrome number ")
else:
    print(f"{c} is not a Palindrome number ")