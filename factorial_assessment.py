value=int(input("enter the num:"))
fact=1
for i in range(1, value+1):
    fact = fact*i
print("The factorial value is : ", end="")
print(fact)