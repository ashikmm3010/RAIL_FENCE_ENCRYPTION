# RAIL FENCE CIPHER
The rail fence cipher (also called a zigzag cipher) is a form of transposition cipher. It derives its name from the way in which it is encoded. 

## ENCRYPTION
* The alphabets are rearranged to create the cipher-text in a transposition cipher.  
* The plain-text is written downhill and diagonally on a series of rails of an imagined fence in the rail fence cypher.
* After reaching the bottom rail, we move diagonally upward before changing directions once more to reach the top rail. As a result, the message's alphabets are written in a zigzag pattern.
* The cipher-text is created by combining the various rows after each letter has been written.

## DECRYPTION
* The length of a plain-text message is maintained as the number of columns in the rail fence cypher.
* The number of rails and the key match.
* As a result, the rail matrix can be built appropriately. 
* Once we have the matrix, we can use the same method of moving diagonally up and down alternately to determine the locations where messages should be inserted.
* The cipher-text is then filled in row by row. After filling it out, we zigzag across the matrix to find the original text.

## SOURCE CODE
### main.py
It contains the main framework for implementing encryption and decryption.
### Functions.py
Functions for encryption and decryption are programmed in this file.
