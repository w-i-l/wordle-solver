from math import log2
import os
import time
import random


clear = lambda: os.system('cls')



words_count = 11454
previous = ''

##green - g
##yellow - y
##gray - w

f = open("cuvinte_wordle.txt","r")
cuvinte = {x.strip() for x in f}

# cuvant_ales = "OSPAT"

def entropy(word,test):
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
    if test:
        if len(cuvinte) < 5:
            for x,y in sorted(modele.items()):
                print(x,y)
    # entropia = 0
    entropia = 1

    for x in modele:
        score = -1
        for a in x:
            if a == '🟩':
                score += 2
            elif a == '🟨':
                score += 1
            elif a == '⬜':
                score += 0
        probabilitatea = modele[x] / len(cuvinte) 
        entropia += probabilitatea*log2(probabilitatea)*score
        # entropia *= probabilitatea*score
    
    return -entropia

max_entropy = 0
best_word = ''

before = time.time()
def find_best_word(test):
    global max_entropy,best_word,previous
    max_entropy = 0
    # best_word = ''

    copie = cuvinte.copy()

    for x in copie:
        entropia = entropy(x,test)
        # clear()
        # print(x,entropia)   

        if test:
            print("TEST::::::::: ",x==best_word,'previous ',previous,'---','best_word',best_word)
        if previous == best_word :
            try:
                cuvinte.remove(previous)
                previous = best_word
            except:
                pass
            # best_word =  x
            # find_best_word()
            
            

        if entropia > max_entropy and len(cuvinte)>1:
            max_entropy = entropia
            previous = best_word
            best_word = x
        elif len(cuvinte) == 1:
            best_word =  list(cuvinte)[0]
            max_entropy = 0.0

        


def check_letters(test):
    global cuvinte
    for i in range(5):
        if test:
            print(best_word,len(best_word))
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
        
cuvant_ales = random.sample(cuvinte,1)[0]
# cuvant_ales = 'IURIE'
# cuvant_ales = 'FOSIL'
# cuvant_ales = "ORBIE"
# cuvant_ales = "CARPA"
# cuvant_ales = 'ALIAI' MAZUR
best_word = 'TAREI'
print(len(cuvinte))
def solver(test):
    check_letters(test)
    find_best_word(test)
    print('----------------------------------------------')
    # print('----------------------------------------------')
    print('BEST WORD: ',best_word,max_entropy)
    # print('----------------------------------------------')
    # print('----------------------------------------------')
    # print(cuvinte)

print("Picked WORD: ",cuvant_ales)


def tester():
    for cuv in cuvinte:
        best_word = "TAREI"
        cuvant_ales = cuv
        

i=1
while not best_word == cuvant_ales  and i<12:
    solver(0)
    i+=1

print("GUESSES",i)

# for x in range(10):
#     solver()
# print(entropy("TAREI"))
