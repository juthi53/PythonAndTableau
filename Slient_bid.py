# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:21:31 2023

@author: Ananya
"""
def max_bid_func(bid_dict):
    max_bid=0
    max_name=""
    for key in bid_dict:
        if max_bid<bid_dict[key]:
            max_bid=bid_dict[key]
            max_name=key
    print(f"The winner is {max_name} with a bid of {max_bid}")
    
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
continue_input="yes"
bid_dict={}
while continue_input=="yes":
    name=input("What is your name?: ").lower()
    bid=int(input("What is your bid?: "))
    continue_input=input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    bid_dict[name]= bid  
    if continue_input=="yes":
        from IPython import get_ipython
        get_ipython().magic('clear')
    
    max_bid_func(bid_dict)
    