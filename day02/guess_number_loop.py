secret = 9 
tries = 0 

while True: 
    guess = int(input("Guess a number between 1 to 10: "))
    tries = tries + 1 

    if guess == secret: 
       print(f"You win! and got it in {tries} tries!")
       break 
    else: 
       print("Wrong number! Try again!")


