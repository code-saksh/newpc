
def grade(marks):
    if marks >=90:
        return "A"
    elif marks >=70:
        return "B" 
    elif marks >=50:
        return "C" 
    elif marks <50:
        return "FAIL"

a=int(input("Enter marks :"))
print("Your grade is :" , grade(a))
