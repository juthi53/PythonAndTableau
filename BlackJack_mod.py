# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:44:53 2023

@author: Ananya
"""
def addlist_func(your_list):
    import random
    cards=["11","1","2","3","4","5","6","7","8","9","10","10","10","10"]
    #for i in range(0,2):
    random_number=int(random.choice(cards))
    #your_score +=random_number
    your_list.append(random_number)
    return your_list

def score_func(your_list):
    sum_list=sum(your_list)
    if sum_list==21 and len(your_list)==2:
        return 0
    for i in range(len(your_list)):
        if your_list[i]==11 and sum_list>21:
            your_list[i]=1 
    
    return sum(your_list)

def compare(your_score,computer_score):
    
    if computer_score==0: 
        print("computer gets blackjack. You lose")        
    elif your_score==0:
        print("Congratulations! You get blackjack. You won")    
    elif your_score>21:
        print("You went over. You lose")
    elif computer_score>21:
        print("Computer went over. You won")
    elif computer_score>your_score:
        print("You lose")
    elif computer_score==your_score:
        print("Draw")
    else:
        print("You won")

def blackjack_func():
    from BlackJack_logo import logo
    print(logo)
    your_list=[]
    computer_list=[]
    deck="y"
    for i in range(0,2):
        your_list=addlist_func(your_list)
        computer_list=addlist_func(computer_list)
    your_score= score_func(your_list)
    computer_score=score_func(computer_list)
    if computer_score==0 or your_score==0 or your_score>21:
        deck="n"    
    while (deck=="y") & (your_score<21):
         print(f"    Your cards: {your_list}, current score: {your_score}")
         print(f"    Computer's first card: {computer_list[0]}")
         deck=input("Type 'y' to get another card, type 'n' to pass: ").lower()     
         while deck not in ("y","n"):
             deck=input("Wrong Input! Type 'y' to get another card, type 'n' to pass: ").lower()
         if deck=="y":
             your_list=addlist_func(your_list)
             if computer_score< 17:
                 computer_list=addlist_func(computer_list)
             your_score= score_func(your_list)
             computer_score=score_func(computer_list)  
    compare(your_score,computer_score)
    print(f"    Your final hand: {your_list}, final score: {your_score}")
    print(f"    Computer's final hand: {computer_list}, final score: {computer_score}")
    
    
    
    
        
while  input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=="y":
    from IPython import get_ipython
    get_ipython().magic('clear')
    blackjack_func()