num = (int)(input("Enter a number to find reverse : "))
rev = 0;
old_num = num
while num>0:
    last_digit = num % 10
    rev = rev*10 + last_digit
    num = num // 10
print(f"reverse of {old_num} is {rev}")