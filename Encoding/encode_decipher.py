"""
By using the encode function, each character in a user-inputted string is shifted by k positions in the alphabet.
Each k is stored in l1, therefore l1 is needed to decode the encoded string. Make sure you save l1 for the decode function.
"""

import random

#Encode will shift each letter in your string a certain amount, each shift will be appended to l1
def encode(s):
    res=""
    #initialize list of shifts for each letter
    l1 = []
    for i in range(len(s)):
        #.isalpha only accepts letters in the alphabet, no special characters
        if s[i].isalpha():
            #check for upper letters, to make sure they remained unchanged when decoded
            if s[i].isupper():
                #k is a random integer between 0 and 10
                k = random.randint(0,11)
                l1.append(k)
                #the character is then moved forward k places
                res+=chr(ord('A')+(ord(s[i])-ord('A')+k)%26)
            #check for upper letters, to make sure they remained unchanged when decoded
            else:
                k = random.randint(0,11)
                l1.append(k)
                res+=chr(ord('a')+(ord(s[i])-ord('a')+k)%26)    
        #check for special characters, make sure they remain unchanged
        else:
            l1.append(0)
            res+=s[i]
    #print result and l1 (l1 is needed to decode the output)
    if res != s:
        print(res, l1)
        print('Encoding was completed succesfully')

#decode accepts the encoded string and the list of how much each letter was shifted
#decode will loop through the encoded string and l1, and shift the letters to normal
def decode(s,l1):
    res=""
    for i in range(0,len(s)):
            if s[i].isalpha():
                if s[i].isupper():
                    #k is now the number each letter was shifted
                    k = l1[i]
                    #the character is now shifted backwards, reverting it back to normal.
                    res+=chr(ord('A')+(ord(s[i])-ord('A')-k)%26) 
                else:
                    k = l1[i]
                    res+=chr(ord('a')+(ord(s[i])-ord('a')-k)%26)    
            else:
                res+=s[i]
    print(res)
    print('Encoding was completed succesfully')

#encode('Hello, My Name is David_Kaler;')
decode('Qepwv, Sz Yavl lb Eibrm_Plpna;', [9, 0, 4, 11, 7, 0, 0, 6, 1, 0, 11, 0, 9, 7, 0, 3, 9, 0, 1, 8, 6, 9, 9, 0, 5, 11, 4, 9, 9, 0])
