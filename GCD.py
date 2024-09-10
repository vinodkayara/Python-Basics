num1=int(input("enter the 1st number:"))
num2=int(input("enter the 1st number:"))

if num2>num1:
    min=num1
else:
    min=num2

for i in range (1,min+1):
    if num1%i==0 and num2%i==0:
        hcf=i

print("the hcf of two number is",+hcf)