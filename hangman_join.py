# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:32:48 2023

@author: Ananya
"""
#from hangman_words import word_list
import random
#from hangman_art import logo
#print(logo)

word_list=["apple","mango","strawberry","guava","banana"]
choosen_word_list=[]
choosen_word=random.choice(word_list)

#print(choosen_word)
life=6
word_length=len(choosen_word)
#print(f"{life}")
guess_word=""
guess_word_list=[]
for i in range(word_length):
    guess_word += "_ "
    guess_word_list += "_"
    choosen_word_list +=choosen_word[i]
print(f"Guess the word: {guess_word}")
#print(choosen_word_list)
match_letter=0
while (life>0) and (match_letter !=word_length):
    guess_letter=input("Guess a letter: ").lower()
    i=0    
    if guess_letter in guess_word_list:
        print("You already guessed this letter: {guess_letter}")
    elif guess_letter!="":
        for i in range(0,word_length):
            if guess_letter == choosen_word_list[i]:
                guess_word_list[i]=guess_letter
                match_letter +=1
            
           # print(f"{match}")
        if (guess_letter not in choosen_word_list) :
            life -= 1
            print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
    else :
        life -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
                
  
    
    print(f"{' '.join(guess_word_list)}")

if match_letter < len(choosen_word_list):
    print("Sorry you are out of Life!")
elif match_letter ==word_length:
    print(choosen_word)
    print("Wow! You have guessed the word")
#print(guess_word_list)
        
        