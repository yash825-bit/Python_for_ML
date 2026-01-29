num = (int)(input("Enter a number to find the factorial : "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(num))
