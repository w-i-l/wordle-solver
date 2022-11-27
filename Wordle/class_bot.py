from math import log2
import time
import random

#File with all words
f = open("cuvinte_wordle.txt",'r')
#Intercomunicating file 
out_txt = open("out.txt",'a')
##Uncomment to see the word structure file
## g = open("output.txt",'w',encoding='utf-8')
#Lists with all words
words = [x.strip() for x in f]
f = open("cuvinte_wordle.txt",'r')
words2 = [x.strip() for x in f]

#Best word used to guess
best_word = ''
max_entropy = 0

#Calculate the entropy for a word
def Entropy(word):

    #Dictionarry with all patterns generated
    #for the word variable
    patterns={}

    for x in words:
        #Pattern for a word related to given one
        pattern=''

        for i in range(5):
            if x[i]== word[i]:
                pattern+='🟩'
            elif word[i] in x:
                pattern+='🟨'    
            else:
                pattern+='⬜'
        
        #Add to dict
        if pattern in patterns:
            patterns[pattern]+=1
        else:
            patterns[pattern]=1

    #The return entropy value        
    entropy=0
    for x in patterns:
        
        #Compute the probability
        probability=patterns[x]/len(words)
        entropy+=probability*log2(probability)

    return -entropy

#Find the best word that fits
def find_best_word():
    global best_word,max_entropy

    best_word = ''
    max_entropy = 0

    for word in words:
        entropy = Entropy(word)
        
        #If the current word has the
        #greatest entropy
        if entropy > max_entropy and len(words)>1:
            best_word  = word
            max_entropy = entropy

        #If there is only one word left
        elif len(words) == 1:
            best_word = words[0]


#Check the word if it fits the pattern
def check_word(word,pattern):
    
    if len(pattern) <5:
        return 0

    for i in range(5):
        if pattern[i] == '⬜':
            if best_word[i] in word:
                return 0
        elif pattern[i] == '🟨':
            #MAROI TAREI
            if best_word[i] == word[i]:
                return 0
            if best_word[i] not in word:
                return 0
        elif pattern[i] == '🟩':
            if not best_word[i] == word[i]:
                return 0
    return 1

#Deletes the word that doesn't fit           
def check_letters():
    global words

    f = open('output.txt',encoding='utf-8')

    pattern = f.readline()

    copie = words.copy()

    for word in copie:
        if check_word(word,pattern) == 0:
            words.remove(word)

chosen_word = ''
response = ''

#Wait until the the contet of 
#intercomunicating file changes
def wait_for_response():
    global response
    #File used to intercomunicate
    output_txt = open('output.txt','r+',encoding='utf-8')
    pattern = output_txt.read()
    output_txt.seek(0)

    #If the readed file content is not good
    while pattern == output_txt.read() or not(len(response)>0 and response[0]  in ['⬜','🟨','🟩']):
        output_txt.seek(0)
        response = output_txt.read()
        output_txt = open('output.txt','r+',encoding='utf-8')
    
    output_txt.close()

#Writes the best word to output.txt
def write_best_word():
     output_txt = open('output.txt','w',encoding='utf-8')
     output_txt.write(best_word)

#Main function call
def solve():
    global chosen_word,best_word,max_entropy,response
    wait_for_response()
    check_letters()
    find_best_word()
    write_best_word()

best_word = "TAREI"

#Writes first guess which is always TAREI
def write_tarei():
    f = open('output.txt','w',encoding='utf-8')
    f.write("TAREI")

#Generates bot
def auto():
    write_tarei()
    #If the word is not guessed
    while not response == '🟩🟩🟩🟩🟩':
        solve()
