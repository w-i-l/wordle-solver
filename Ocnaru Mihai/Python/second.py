from math import log2
import os
import time
import random

clear = lambda: os.system('cls')

f = open("cuvinte_wordle.txt",'r')

words = set(x.strip() for x in f)

def entropy(word):

    patterns = {}

    for x in words:
        pattern = ''
        for i in range(5):
            if word[i] in x:
                pattern += '🟨'
            elif x[i] == word[i]:
                pattern += '🟩'
            
            elif not word[i] in x:
                pattern += '⬜'
        
        if pattern not in patterns:
            patterns[pattern] = 1
        else:
            patterns[pattern] += 1
    
    entropy = 0

    # if len(words) < 20:
    #     print("--------------",word,"--------------" )
    #     for x,y in sorted(patterns.items()):
    #         print(x,y)
    #     print(words)

    for x in patterns:

        score = 0
        for a in x:
            if a == '🟩':
                score += 2
            elif a == '🟨':
                score += 1
            elif a == '⬜':
                score += 0

        probability = patterns[x] / len(words)
        entropy += probability*log2(probability)

    return -entropy

def find_best_word():
    global best_word,max_entropy
    max_entropy = 0
    for word in words:
        word_entropy = entropy(word)
        if word_entropy > max_entropy:
            max_entropy = word_entropy
            best_word = word


def check_letters():
    global words
    for i in range(5):
        
        if best_word[i] == chosen_word[i]:
            # for word in words:
            #     if words[i] not == best_word[i]:
            #         words.remove[word]
            words = {word for word in words if word[i] == best_word[i] }
        elif best_word[i] in chosen_word:
            words = {word for word in words if best_word[i] in word }
        elif best_word[i] not in chosen_word:
            words = {word for word in words if best_word[i] not in word }
    

best_word = ''
max_entropy = 0

# chosen_word = random.sample(words,1)[0]
chosen_word = "ARCAT"
# chosen_word = "TAPUL"
# chosen_word = "PILON"
# before = time.time() 
# find_best_word()
# print(time.time()-before)
# print(best_word,max_entropy)

def solve():
    # print(words)
    check_letters()
    find_best_word()
    print(best_word,max_entropy)

print('-------',chosen_word,'-------')
best_word = "TAREI"
for x in range(10):
    solve()
