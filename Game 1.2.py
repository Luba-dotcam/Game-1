import random

number_to_Guess = random.randint(1,100)

user_Guess=-1

while True:
    try:
        user_Guess != number_to_Guess

        user_Guess = int(input("Guess the number:"))

    except ValueError:
        print("It's not a number")
    
    if user_Guess > number_to_Guess:
        print("Too big!")
    
    elif user_Guess < number_to_Guess:
        print("Too small!")
    
    else:
         print("You win!")
    
  