
a=int(input("Enter a number : "))
c=a
while a>0:
    b=a%10
    print(f'{b} is a digit of {c}')
    a=a//10
    