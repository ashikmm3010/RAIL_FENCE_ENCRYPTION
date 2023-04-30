#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:02:05 2023

@author: treewalker && Wander_Lust
"""
global l
global rows

def cipher_array(text, key):
    global rows
    rows = key
    global l
    l = len(text)
    
    cipher_arr = [ ["0" for col in range(l)] for row in range(rows)]
    
    r=0
    c=0
    traverse = "up"
    
    cipher_arr[r][c] = text[0]
    
    
    for i in range (1,l):
        
        if traverse == "up":
            r+=1
        elif traverse == "down":
            r-=1
        c+=1
        
        if r<0:
            r = 1
            traverse = "up"
        if r>rows-1:
            r = rows - 2
            traverse = "down"
        
        cipher_arr[r][c] = text[i]
        
    # print("iteration: " ,i)
    # print("r=" ,r, "; c=", c)
    
    return cipher_arr 

def array_to_cipher(array):
    cipher = ""
    for r in array:
        for c in r:
            cipher = cipher + c
            cipher = cipher.replace("0","")
    return cipher

def print_array(array):
    for r in array:
        for c in r:
            print(c,end = " ")
        print()
    print("\n")
    
def cipher_to_array(cipher, key):
    global rows 
    decipher_arr = [ ["0" for col in range(l)] for row in range(rows)]
    
    r=0
    c=0
    index = 0
    decipher_arr[r][c] = cipher[0]
    
    
    text1 = ""
    for i in range(len(cipher)):
        text1 += "*"
    decipher_arr = cipher_array(text1, key)
    
    i=0
    
    for r in range(0,rows):
        for c in range(0,len(cipher)):
            # print(r)
            # print(c)
            if decipher_arr[r][c] == "*":
                # print(1)
                # print(cipher[i])
                
                decipher_arr[r][c] = decipher_arr[r][c].replace("*",cipher[i])
                i += 1
    # 
    #print_array(decipher_arr)
    
    return decipher_arr
        
def array_to_text(array):
    r=0
    c=0
    traverse = "up"
    
    text = ""
    
    text = text + array[r][c]
    
    
    for i in range (1,l):
        
        if traverse == "up":
            r+=1
        elif traverse == "down":
            r-=1
        c+=1
        
        if r<0:
            r = 1
            traverse = "up"
        if r>rows-1:
            r = rows - 2
            traverse = "down"
        
        text = text + array[r][c]  
    return text 