#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:23:56 2023

@author: treewalker && Wander_lust
"""
from Functions import *

global debug 
debug = False

global rows

def encrypt(text, key):
    global l
    l = len(text)
    global rows
    rows = key
    if l%rows != 0:
        for i in range(0,l%rows):
            text += " "             #appending blank space
    
    if debug:
        print(text)
        print(len(text))
    
    cipher_arr = cipher_array(text, key)
    if debug:
        print_array(cipher_arr)  
    cipher = array_to_cipher(cipher_arr)
    
    return cipher
        

def decrypt(cipher, key):
    global l
    
    decipher_arr = cipher_to_array(cipher, key)
    
    text = array_to_text(decipher_arr)
    return text 

print("RAIL FENCE ENCRYPTION\n"+
      "Enter the no. of rails as the key\n")

while True:
    text = input("TEXT : ")
    key = int(input("KEY  : "))
    rows = key
    print()
    cipher = encrypt(text, key)
    print("Encrypted Text  : ", cipher)
    decipher = decrypt(cipher, key)
    print("Decrypted Cipher: ", decipher)