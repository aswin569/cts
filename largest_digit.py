num = int(input("Enter a number"))
max =0
digit =0
print("Largest no")

while num >0:
    digit = num %10
    if digit > max:
        max = digit
    num = num //10

print(max)

    