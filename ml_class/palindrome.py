num = (int)(input("Enter a number to check palindrome or not : "))

rev_num = 0
old_num = num

while num > 0:
    lastDigit = num % 10
    rev_num = rev_num*10+lastDigit
    num = num//10


if rev_num == old_num:
    print(f"{old_num} is palindrome");
else:
    print(f"{old_num} is not a plaindrome")
