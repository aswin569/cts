no_of_ticket= int(input("Enter the number of tickets :"))
total_cost =0
discount =0
if not(5 <= no_of_ticket <=40):
    print("Minimum 0f 5 and maximum of 40 tickets")
else:
    ref = input("Do you want refreshments :")
    coupen = input("Do you have coupen code :")
    circle = input("Enter the circle :")
    if circle =="k":
        total_cost = total_cost+ (no_of_ticket*75)
    elif circle =="q":
        total_cost= total_cost+(no_of_ticket*150)
    else:
        print("Invalid input")
    if no_of_ticket>20:
        total_cost= total_cost - (total_cost*.1)
    if coupen == "y":
        total_cost= total_cost- (total_cost*.02)
    if ref == "y":
        total_cost= total_cost + (no_of_ticket*50)
print(total_cost)
    
   




