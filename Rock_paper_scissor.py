import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
Player_choice=[rock,paper,scissors]
player1=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(Player_choice[player1])
print("Computer chose:\n")
player2=random.randint(0,2)
print(Player_choice[player2])

try:
    if player1==player2:
        print("Draw!")
    elif player1>player2:
        print("You Won!")
    else:
        if (player1==0) and (player2==2):
            print("You Won!")
        else:
            print("You Lost!")
except:
    print("Invalid Input")