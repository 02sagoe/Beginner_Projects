# Write your solution below the starter code
# Follow the instructions in the tab to the right

import random

# Welcome the user to the game

print("Welcome to rock, paper, scissors. Good luck!")

# Make a choice for the computer player

options = ["Rock", "Paper", "Scissors"]



computer_choice = random.choice(options)
lower_computer_choice = str.lower(computer_choice) #using the str.lower() command to make all leters in the input string in lowercase letters hence making them easily comparable. Futhermore even if an input is in lowercase the lowercase will still be returned

# Get a choice from the user
user_choice = input("Chose one: Rock, Paper or Scissors? ")
lower_user_choice = str.lower(user_choice)

# Compare the user and computer choice
# Print the right message, based on the choices

print(f"The computer choses {computer_choice}")

if lower_user_choice == "rock" and lower_computer_choice == "rock":
  print("Rock on Rock. It's a draw!")
elif lower_user_choice == "rock" and lower_computer_choice == "paper":
  print("Paper covers Rock. You lose!")
elif lower_user_choice == "rock" and lower_computer_choice == "scissors":
  print("Rock smashes Scissors. You win!")
elif lower_user_choice == "paper" and lower_computer_choice == "rock":
  print("Paper covers Rock. You win!")
elif lower_user_choice == "paper" and lower_computer_choice == "paper":
  print("Paper and Paper. It's a draw!")
elif lower_user_choice == "paper" and lower_computer_choice == "scissors":
  print("Scissors cuts Paper. You lose!")
elif lower_user_choice == "scissors" and lower_computer_choice == "rock":
  print("Rock smashes Scissors. You lose!")
elif lower_user_choice == "scissors" and lower_computer_choice == "paper":
  print("Scissors cuts Paper. You win!")
elif lower_user_choice == "scissors" and lower_computer_choice == "scissors":
  print("Scissors and Scissors. It's a draw!")
else:
  print("You have to enter Rock, Paper, or Scissors")
  
