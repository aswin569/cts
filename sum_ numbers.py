num = int(input("Enter a number :"))
print("Sum of n  numbers")

sum =0
sq_sum =0 
cube_sum =0

if num <0 :
    print("Enter a positive number")
    for i in range(1, num +1):
        sum = sum +i
        sq_sum = sq_sum +(i*i)
        cube_sum =cube_sum+(i*i*i)

else :
    for i in range(1, num +1):
        sum = sum +i
        sq_sum = sq_sum +(i*i)
        cube_sum =cube_sum+(i*i*i)


print("sum", sum)
print("square sum", sq_sum)
print("cube sum ", cube_sum)