# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 05:42:59 2023

@author: Ananya
"""
def player_details(player1,order):
    from Higher_Lower_data import data      
    
    # populating player1 and player2 details from the data list      
    player1_name=data[player1]['name']
    player1_count=data[player1]['follower_count']
    player1_desc=data[player1]['description']
    player1_country=data[player1]['country']
    print(f"Compare {order}: {player1_name}, {player1_desc}, from {player1_country}")
    return player1_count

def player_choice():
    user_choice=input("Who has more followers? Type 'A' or 'B': ").upper()
    
    #this will wait for the correct input    
    while user_choice not in ("A", "B"):
        user_choice=input("Wrong Input! Type 'A' or 'B': ").upper()
    return user_choice

def higher_lower():
    import random      
    from Higher_Lower_data import data
    from Higher_Lower_Logo import logo,vs
    from IPython import get_ipython
    get_ipython().magic('clear')
        
    #generating a random integer number    
    player2=random.randint(0,(len(data)-1))
    choice="A"
    is_win=True
    user_score=0
    # if two random numbers are same then will generate new random number
    
      
    while (choice in ("A","B")) and (is_win==True):
        #Player1 will always get the value of player2 for each turn and player2 will get a new random number
        player1=player2
        player2=random.randint(0,(len(data)-1))
        
        # if two random numbers are same then will generate new random number
        while player1==player2:
            player2=random.randint(1,len(data))    
        
        #calling the fucntions and getting the details from the data list and displaying the result
        print(logo)            
        player1_count=player_details(player1,"A")
        print(vs)
        player2_count=player_details(player2,"B")
        choice=player_choice()
        
        #calculting the winner 
        if (player2_count>player1_count) and (choice=="B"):
            is_win=True
        elif (player1_count>player2_count) and (choice=="A"):
            is_win=True   
        else:
            is_win=False
            choice="End"
            print(f"Sorry, that's wrong. Final score: {user_score}")
        if is_win==True:
            user_score +=1
            get_ipython().magic('clear')
            print(f"You're right! Current score: {user_score}.")            

higher_lower()