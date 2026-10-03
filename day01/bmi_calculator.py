height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))

bmi = weight / (height **2)

print(f"Your Bmi is: {round(bmi, 2)}")
