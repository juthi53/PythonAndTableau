# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:59:02 2023

@author: Ananya
"""
def compare(user_number,computer_number,life):
    if user_number==computer_number:
        print(f"You got it! The answer was {computer_number}")
        return 0
    elif user_number>computer_number:
        print("Too High.\nGuess again.")
        return (life-1)
    else:
        print("Too low.")
        if (life-1)>0:
            print("Guess Again.")
            return (life-1)
        else:
            print("You've run out of guesses, you lose.")


def guess_a_number_game():
    import random
    from IPython import get_ipython
    get_ipython().magic('clear')
    from Number_Guess_Logo import logo
    print(logo)
    print("Welcome to the Number Guessing Game!")
    computer_number=random.randint(1,100)
    try:        
        print("I'm thinking of a number between 1 and 100: ")
        diff_level=input("Choose a difficulty type 'easy' or 'hard': ").lower()
        while diff_level not in ("easy","hard"):
            diff_level=input("Wrong Input! Choose a difficulty type 'easy' or 'hard': ").lower()
        if diff_level=="hard":
            life=5
        else:
            life=10
        while(life!=0):
            print(f"You have {life} attempts remaining to guess the number.")
            user_number=int(input("Make a guess: "))      
            life=compare(user_number,computer_number,life)
    except:
        print("Its not a number")


guess_a_number_game()