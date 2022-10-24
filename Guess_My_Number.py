# See the Instructions tab

# Set secret number

import random

secret_number = random.randint(1, 99) 

print("I'm thinking of a number between 1 and 99")
guess = None

# Ask the user to guess

# Check to see if the guess is <, >, or = secret number

while guess != secret_number:
  try:
    guess = int(input("Enter a guess: "))
    if int(guess) == secret_number:
      print(f"Congrats the number is {guess} \nYou won")
    elif int(guess) < secret_number:
      print("Your guess is too low")
    else:
      print("Your guess is too high")
  except:
    print("ERROR! Not a number")
# Print the right message


