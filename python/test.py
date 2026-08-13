

dic={ "dic1" : { "number" : 7003092759 , "email" : "bcskolkata1@gmail.com", "city" : "bangalore" } , "dic2" : { "number" : 8100282789 , "email" : "bcskolkata@gmail.com" , "city" : "kolkata" }} 

dic["dic1"]["number"] = 7003092750 
print(dic)
del dic["dic2"]["number"]
print(dic)

for i in dic.items():
    print(i)

a=int(input("Enter a number : "))
found = False
for i in dic.values():
    if i.get("number") == a:
        print(i["email"])
        print(i["city"])
        found = True
        break
if not found:
    print("No record found for that number")

