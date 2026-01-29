n = (int)(input("Enter a number : "))
first = 0;
second = 1;
if n>=1:
    print(first, end=" ")
if n>=2:
    print(second, end=" ")
for i in range(3, n+1):
    updated = first + second
    print(updated, end=" ")
    first = second
    second = updated