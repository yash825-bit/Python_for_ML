print("program to find largest of three")
a = (int)(input("Enter the first number : "))
b = (int)(input("Enter the second number : "))
c = (int)(input("Enter the third number : "))


if a>b and a>c:
    print(f"{a} is largest")
elif b>c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")