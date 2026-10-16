print ("Welcome to rollercoaster!")
height = int(input("What is your heightin cm? "))

if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay 5$)")
    elif age <= 18:
        print("Please pay 7$")
    elif age < 22:
        print("Please pay 12$")
    elif age <= 40:
        print ("pay 17$")
    else:
        print("Your age is not allowed")    
    gender = str(input("What is your gender male or female?"))
    if gender == 'male':
        print ("You ride with men section")
    else:
        print("you ride with female section")
else: 
    print("Sorry, You can't ride the rollercoaster.")
