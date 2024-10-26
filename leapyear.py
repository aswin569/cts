year = int(input("Enter a year :"))

if year == 0:
    print("Invaid year")
else:
    if (year % 400 ==0) or (year % 4 == 0 and year % 100 !=0):
        print("Leap Year")
    else:
        print("Not a leap year")
