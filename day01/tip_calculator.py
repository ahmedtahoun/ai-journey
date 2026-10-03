bill = float(input("How much your bill amount? "))
tip_percent = float(input("Tip Percentage: "))

tip = bill * (tip_percent /100)

total = bill + tip 

print(f"Tip: {tip}")
print(f"Total is {total}")
