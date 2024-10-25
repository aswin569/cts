m = int(input("Enter the month :"))

if 1 <= m <= 12:
    if 3<= m<=5:
        print("Spring")
    elif 6<= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Autumn")
    else :
        print("Winter")
else:
    print("Invalid month")
