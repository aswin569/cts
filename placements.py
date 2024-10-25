cse = int(input("Enter the number of students  placed in CSE :"))
ece = int(input("Enter the number of students  placed in ECE :"))
mech = int(input("Enter the number of students  placed in MECH :"))

if cse<0 or ece<0 or mech<0:
    print("Input invalid")
elif cse == ece == mech:
    print("None of the department has got the highest placement")
else:

 max_placement = max(cse, ece, mech)

 print("Highest placement")

 if cse == max_placement:
    print("CSE")
 if ece == max_placement:
    print("ECE")
 if mech == max_placement:
    print("MECH")
