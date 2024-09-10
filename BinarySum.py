def SunBinary(n):
    sum=0
    while n>0:
        binary=n%2
        sum+=binary
        n//=2
    return sum
n=int(input("number:"))
sumOfDigit=SunBinary(n)
print(sumOfDigit)

