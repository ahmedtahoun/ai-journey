weight = int(input("What is your weight in kg? "))
height = float(input("What is your height in m? "))

BMI = weight / (height* height) 

if BMI < 18.5 :
    print (f" Your BMI is {BMI} you're underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI} you're normal")
elif BMI < 30: 
    print(f'Your BMI is {BMI} you"re your"re overweight')
elif BMI < 35: 
    print (f"your bmi {BMI} you're obese")

else: 
    print("Your BMI is {BMI}, you're clinically obese.")


print(f"Your BMI is {BMI} ")