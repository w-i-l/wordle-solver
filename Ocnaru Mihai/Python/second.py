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

        probability = patterns[x]/ len(words)
        entropy += probability*log2(probability)

    return -entropy

def find_best_word():
    global best_word,max_entropy
    max_entropy = 0
    for word in words:
        word_entropy = entropy(word)
        if word_entropy > max_entropy and len(words)>1:
            max_entropy = word_entropy
            previous = best_word
            best_word = word
        elif len(words)==1:
            best_word = list(words)[0]

def check_letters():
    global words
    
    try:
        words.remove(best_word)
    except:
        pass
    for i in range(5):
        if best_word[i] == chosen_word[i]:
            words = {word for word in words if word[i] == best_word[i] }
        elif best_word[i] in chosen_word:
            words = {word for word in words if best_word[i] in word }
        elif best_word[i] not in chosen_word:
            words = {word for word in words if best_word[i] not in word }
    

best_word = ''
previous = ''
max_entropy = 0

chosen_word = random.sample(words,1)[0]
# chosen_word = "IMENS"
# chosen_word = "TAPUL"
# chosen_word = "PILON"
# chosen_word = "ERMIT"
# before = time.time() 
# find_best_word()
# print(time.time()-before)
# print(best_word,max_entropy)

def solve():
    global best_word,max_entropy,chosen_word
    
    check_letters()
    find_best_word()
    # print(words)
    # print(best_word,max_entropy)


# best_word = "TAREI"
# for x in range(10):
#     solve()

def tester(no_tests):
    i = 0
    global best_word,max_entropy,chosen_word,words,f
    for j in range(no_tests):
        f = open("cuvinte_wordle.txt",'r')
        words = set(x.strip() for x in f)
        
        # print(words)
        chosen_word = list(words)[int(random.random()*11000)]
        # chosen_word = 'IMENS'
        
        print('-------',chosen_word,'-------')
        best_word = "TAREI"
        previous = "TAREI"
        for x in range(10):
            
            solve()
        if best_word == chosen_word:
            i += 1
    print("TESTE BUNE",i)

tester(100)

