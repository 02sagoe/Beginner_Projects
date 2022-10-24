import random

# deck of cards stored in a list

card_deck = ["A-H", "2-H", "3-H", "4-H", "5-H", "6-H", "7-H", "8-H", "9-H", "10-H", "J-H", "Q-H", "K-H", "A-D", "2-D", "3-D", "4-D", "5-D", "6-D", "7-D", "8-D", "9-D", "10-D", "J-D", "Q-D", "K-D", "A-S", "2-S", "3-S", "4-S", "5-S", "6-S", "7-S", "8-S", "9-S", "10-S", "J-S", "Q-S", "K-S", "A-C", "2-C", "3-C", "4-C", "5-C", "6-C", "7-C", "8-C", "9-C", "10-C", "J-C", "Q-C", "K-C"]

# ACSII art to show break points of the different rounds

diagram = ("""
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
""")


print("""

 __        _______ _     ____ ___  __  __ _____ 
 \ \      / / ____| |   / ___/ _ \|  \/  | ____|
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
   \ V  V / | |___| |__| |__| |_| | |  | | |___ 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|
                    
                      _        
                     | |_ ___  
                     | __/ _ \ 
                     | || (_) |
                      \__\___/ 

                  
 __  ___ ____  __   __  ___    ___ __  ___ __    __  
| _\| __/ _/ |/ /  /__\| __|  / _//  \| _ \ _\ /' _/ 
| v | _| \_|   <  | \/ | _|  | \_| /\ | v / v |`._`. 
|__/|___\__/_|\_\  \__/|_|    \__/_||_|_|_\__/ |___/ 

                                                                            
                                                                            

                                                             
    
                               

The rules are simple.

1. You must have 4 players to play this game

2. Each player is required to enter their required name for the duration of the game

3. The first player will draw 6 cards whilst the other 3 players will draw 5 cards

4. Player 2 will draw a card from Player 1; Player 3 will draw a card from Player 2; Player 4 will draw a card from Player 3 & Player 1 will draw a card from Player 4

5. You can choose one of the 6 cards the player holds

6. The above step will ensure that for one ROUND every player will have 6 cards which will be passed around. 

7. There are a total of 5 ROUNDS

8. All of the 6 cards are allowed to be picked even the one the previous player selected

9. You would be allowed to see everyones deck immediately after all the cards have been drawn

10. There will be a points calculation at the end of the of the 5 ROUNDS and the person with the most points will win.


--------------Card Denotions------------------

A-H - Ace of Hearts
Q-H - Queen of Hearts 
7-D - Seven of Diamonds
3-D - Three of Diamonds 
5-S - Five of Spades
J-S - Jack of Spades
K-C - King of Clubs
2-C - Two of Clubs 

----------------------------------------------

--------------------Points---------------------

2-10 : 1 Point

 J   : 2 Points

 Q   : 3 Points

 K   : 4 points

 A   : 5 points

-----------------------------------------------

""")

# code to enter player names

player_1_name = input("Player 1 - Enter your name: ")
print()
print()
player_2_name = input("Player 2 - Enter your name: ")
print()
print()
player_3_name = input("Player 3 - Enter your name: ")
print()
print()
player_4_name = input("Player 4 - Enter your name: ")
print()
print()

# emtpy lists for each player to store the cards

player_1 = []
player_2 = []
player_3 = []
player_4 = []


input("Press enter to draw all the cards\n\n")

# code to randomly share all the cards

for i in range(0, 5):
    player_1.append(random.choice(card_deck))
    card_deck.pop(i)
    player_2.append(random.choice(card_deck))
    card_deck.pop(i)
    player_3.append(random.choice(card_deck))
    card_deck.pop(i)
    player_4.append(random.choice(card_deck))
    card_deck.pop(i)
player_1.append(random.choice(card_deck))
card_deck.pop(i)


# code to show the cards that each player holds

print(f"{player_1_name} your hand is:\n")
print(player_1)
print()
print()
print(f"{player_2_name} your hand is:\n")
print(player_2)
print()
print()
print(f"{player_3_name} your hand is:\n")
print(player_3)
print()
print()
print(f"{player_4_name} your hand is:\n")
print(player_4)
print()
print()


# function to pick a card from each player when the game starts

def pick_a_card(choice, selector, recipient):
    while True:
        if choice.isdigit() != True:
            print()
            print("Wrong input.")
            print()
            choice = input("Please try again: ")
            print()
        elif int(choice) > 6 or int(choice) < 1:
            print("Wrong input.")
            choice = input("Please try again: ")
        else:
            break
    if int(choice) == 1:
        selector.append(recipient[0])
        recipient.pop(0)
    elif int(choice) == 2:
        selector.append(recipient[1])
        recipient.pop(1)
    elif int(choice) == 3:
        selector.append(recipient[2])
        recipient.pop(2)
    elif int(choice) == 4:
        selector.append(recipient[3])
        recipient.pop(3)
    elif int(choice) == 5:
        selector.append(recipient[4])
        recipient.pop(4)
    elif int(choice) == 6:
        selector.append(recipient[5])
        recipient.pop(4)
    else:
        print("Wrong input. Please try again")


input("Press enter to ROUND 1:")

print(diagram)

print(diagram)

print(diagram)

print(diagram)


# code to play the game over 5 rounds

for i in range(0, 5):
    print(f"ROUND {i+1}")
    print()
    print()
    print(diagram)
    print()
    print()
    choice = input(f"{player_2_name} pick a card from {player_1_name}: ")
    pick_a_card(choice, player_2, player_1)
    print()
    choice = input(f"{player_3_name} pick a card from {player_2_name}: ")
    pick_a_card(choice, player_3, player_2)
    print()
    choice = input(f"{player_4_name} pick a card from {player_3_name}: ")
    pick_a_card(choice, player_4, player_3)
    print()
    choice = input(f"{player_1_name} pick a card from {player_4_name}: ")
    pick_a_card(choice, player_1, player_4)
    print()

print()

# code to remove a card randomly from a players hand

input(f"Press enter to remove a random card from {player_1_name}\n\n")
random_pick = random.choice(player_1)
player_1.remove(random_pick)
print(f"The card you removed was {random_pick} from {player_1_name}''")


score_1 = 0
score_2 = 0
score_3 = 0
score_4 = 0

# code for calculating indivdual scores

for i in player_1:
    for x in i:
        if x in "123456789":
            score_1 = score_1 + 1
        elif x in "J":
            score_1 = score_1 + 2
        elif x in "Q":
            score_1 = score_1 + 3
        elif x in "K":
            score_1 = score_1 + 4
        elif x in "A":
            score_1 = score_1 + 5
print()
print(f"{player_1_name} your hand at the end was: ")
print(player_1)
print(f"Your score is {score_1}")
print()


for i in player_2:
    for x in i:
        if x in "123456789":
            score_2 = score_2 + 1
        elif x in "J":
            score_2 = score_2 + 2
        elif x in "Q":
            score_2 = score_2 + 3
        elif x in "K":
            score_2 = score_2 + 4
        elif x in "A":
            score_2 = score_2 + 5
print()
print(f"{player_2_name} your hand at the end was: ")
print(player_2)
print(f"Your score is {score_2}")
print()


for i in player_3:
    for x in i:
        if x in "123456789":
            score_3 = score_3 + 1
        elif x in "J":
            score_3 = score_3 + 2
        elif x in "Q":
            score_3 = score_3 + 3
        elif x in "K":
            score_3 = score_3 + 4
        elif x in "A":
            score_3 = score_3 + 5
print()
print(f"{player_3_name} your hand at the end was: ")
print(player_3)
print(f"Your score is {score_3}")
print()


for i in player_4:
    for x in i:
        if x in "123456789":
            score_4 = score_4 + 1
        elif x in "J":
            score_4 = score_4 + 2
        elif x in "Q":
            score_4 = score_4 + 3
        elif x in "K":
            score_4 = score_4 + 4
        elif x in "A":
            score_4 = score_4 + 5
print()
print(f"{player_4_name} your hand at the end was: ")
print(player_4)
print(f"Your score is {score_4}")
print()

# code for finding the winner of the game

if score_1 > score_2 and score_1 > score_3 and score_1 > score_4:
    print(f"{player_1_name} you won! With a score of {score_1}")
elif score_2 > score_1 and score_2 > score_3 and score_2 > score_4:
    print(f"{player_2_name} you won! With a score of {score_2}")
elif score_3 > score_1 and score_3 > score_2 and score_3 > score_4:
    print(f"{player_3_name} you won! With a score of {score_3}")
elif score_4 > score_1 and score_4 > score_2 and score_4 > score_3:
    print(f"{player_4_name} you won! With a score of {score_4}")
else:
    print("There was a tie")

print()
print()


input("Press enter to end the game: ")
print()
print()
print()

print("""

THANK YOU FOR PLAYING
 **       *     * * *
   **  *   ** **   * 
*     * *        *   
  *             *    
    *                
*              *     
        *            
   *               * 
       *  **         
              *     *
 *    *          *   
            *     *  

""")