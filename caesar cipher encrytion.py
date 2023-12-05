# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:17:07 2023

@author: Ananya
"""
def caeser(encode_type,message,shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    step=shift
    if encode_type=="decode":
        step=shift * -1
    message_length=len(message)
    message_list=[]
    for i in range(0,len(message)):
        message_list += message[i]
    for i in range(0,len(message)):
        test=message_list[i]
        if test in alphabet:
            message_list[i]=alphabet[alphabet.index(test)+step]
            #print(f"{alphabet.index(test)+step},{alphabet[alphabet.index(test)+step]}")
    print(f"Here's the {encode_type}d result: {''.join(message_list)}") 
    


from art import logo
print(logo)
repeat_type="yes"
while repeat_type=="yes":
    encode_type=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while encode_type not in ("decode","encode"):
        print("Wrong input")
        encode_type=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
    message=input("Type your message:\n").lower()
    try:
        shift=int(input("Type the shift number:\n"))
        while shift > 26:
            shift =shift % 26
        caeser(encode_type,message,shift)
        repeat_type=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if repeat_type !="yes":
            repeat_type="no"
            print("Goodbye")
    except:
        print("Shift can not be a string")
        repeat_type="no"
    