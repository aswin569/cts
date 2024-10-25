pizza = int(input("Enter the no of pizzas bought :"))
puffs = int(input("Enter the no of puffs bought :"))
cool = int(input("Enter the no of cooldrinks bought :"))


print("Bill Details")
print("No of pizzas :", pizza)
print("No of puffs :", puffs)
print("No of cooldrinks :", cool)
sum_pizza = 100 * pizza
sum_puffs = 20 * puffs
sum_cooldrinks = 10 * cool
total_price = sum_pizza + sum_puffs + sum_cooldrinks
print("Total price = ",total_price)
print("ENJOY THE SHOW!!!")