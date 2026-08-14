
a=int(input("Enter a number : "))
for i in range(1,a+1):
    count=0 
    if a%i==0:
        count=count+1
    if count>2:
        continue
    else:
        print(i)         