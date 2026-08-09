
items = [1,2,2,3,3,3,4,5,7,7,9,9,10]
dup = [] 
for i in  items :
    count=0
    for j in items : 
        if i == j :
            count = count +1 
    if count > 1 and i not in dup :
                dup.append(i)

print(dup)