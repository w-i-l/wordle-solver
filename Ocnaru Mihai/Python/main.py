from math import log2
import os
import time
import random


clear = lambda: os.system('cls')



words_count = 11454

##green - g
##yellow - y
##gray - w

f = open("cuvinte_wordle.txt","r")
cuvinte = set(x.strip() for x in f)

# cuvant_ales = "OSPAT"

def entropy(word):
    modele = {}

    for cuv in cuvinte:
        model = ''
        for i in range(5):
            if cuv[i] == word[i]:
                model += '🟩'
            elif cuv[i] in word:
                model += '🟨'
            elif not cuv[i] in word:
                model += '⬜'



        if not model in modele:
            modele[model] = 1
        else:
            modele[model] += 1
    
    # for x,y in sorted(modele.items()):
    #     print(x,y)
    entropia = 0

    for x in modele:
        probabilitatea = modele[x] / len(cuvinte)
        entropia += probabilitatea*log2(probabilitatea)
    
    return -entropia

max_entropy = 0
best_word = ''

before = time.time()
def find_best_word():
    global max_entropy,best_word
    max_entropy = 0
    best_word = ''
    for x in cuvinte:
        entropia = entropy(x)
        # clear()
        # print(x,entropia)   
        
        if entropia >= max_entropy and not len(cuvinte) == 1:
            max_entropy = entropia
            best_word = x
        elif len(cuvinte) == 1:
            best_word =  list(cuvinte)[0]
            max_entropy = 0.0


def check_letters():
    global cuvinte
    for i in range(5):
        # print(best_word,len(best_word))
        if best_word[i] == cuvant_ales[i]:
            # copie = cuvinte.copy()
            # for x in copie:
            #     if not x[i] == best_word[i]:
            #         cuvinte.remove(x)
            cuvinte = {cuv for cuv in cuvinte if cuv[i]==best_word[i]}
        elif best_word[i] in cuvant_ales:
            # copie = cuvinte.copy()
            # for x in copie:
            #     if not best_word[i] in x:
            #         cuvinte.remove(x)
            cuvinte = {cuv for cuv in cuvinte if best_word[i] in cuv}
        elif not best_word[i] in cuvant_ales:
            # copie = cuvinte.copy()
            # for x in copie:
            #     if best_word[i] in x:
            #         cuvinte.remove(x)
            cuvinte = {cuv for cuv in cuvinte if not best_word[i] in cuv}
        
# cuvant_ales = random.sample(cuvinte,1)[0]
cuvant_ales = 'IURIE'
# cuvant_ales = 'FOSIL'
best_word = 'TAREI'

def solver():
    check_letters()
    find_best_word()
    print(best_word,max_entropy)
    # print(cuvinte)

print(cuvant_ales)

while not best_word == cuvant_ales:
    solver()
# print(entropy("TAREI"))
