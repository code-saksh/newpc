
a=int(input("Enter a number : "))
c=a
count =0 
count1=0
while a>0:
    b=a%10
    if b%2==0:
        count= count +1 
    else: 
        count1=count1+1

    a=a//10

print("odd digits" , count1)
print("even digits" , count)