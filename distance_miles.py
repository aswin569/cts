litre = int(input("Enter the no of litres to fill the tank"))
distance = int(input("Enter the distance covered "))
print("Litres/100Km")
for_km = (litre / distance)*100
print(round(for_km,2))
print("Miles/gallons")
gallon = 0.2642*litre
mile = 0.6214*distance
for_mile = (mile / gallon)
print(round(for_mile,2))




