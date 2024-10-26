num = int(input("Enter a number : "))

string = str(num)

print("Reverse")
print(string[::-1])

num = int(input("Enter a number : "))
rev =0
digit =0
print("Reverse")
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

print(rev)



