num = int(input("Enter a number : "))
rev =0
digit =0
print("Reverse")
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

if num == rev:
    print("Palindrome")
else:
    print("Not palindrome")