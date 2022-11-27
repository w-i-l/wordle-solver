from math import log2
import time
import random
from multiprocessing import Pool
f = open("cuvinte_wordle.txt",'r')
out_txt = open("with_letters.txt",'a')
words = [x.strip() for x in f]
f = open("cuvinte_wordle.txt",'r')
words2 = [x.strip() for x in f]

best_word = ''
max_entropy = 0
max_letters_worth = 0 

def Entropy(word):
    patterns={}
    for x in words:
        pattern=''
        for i in range(5):
            if x[i]== word[i]:
                pattern+='🟩'
            elif word[i] in x:
                pattern+='🟨'    
            else:
                pattern+='⬜'

        if pattern in patterns:
            patterns[pattern]+=1
        else:
            patterns[pattern]=1
        # print(pattern)
    entropy=0
    for x in patterns:

        score = 1
        for a in x:
            if a=='🟩':
                score += 5
            elif a == '🟨':
                score += 3
        
        # if len(words) < 100:
        #     print(x,patterns[x])
        
        probability = patterns[x]/len(words)
        entropy += probability*log2((probability))
    return -entropy

letters = {}
def count_letters():
    global letters
    letters = {chr(key):0 for key in range(ord("A"),ord('Z')+1)}

    for word in words:
        for letter in word:
            letters[letter] += 1
    

def compute_letters_worth(word):

    score = 1
    for letter in word:
        score *= letters[letter]/(len(words)*5)
    return score

chosen_word = ''


def are_all_letters_different(word):
    return len(set(word)) == 5

def find_best_word():
    global best_word,max_entropy,max_letters_worth

    best_word = ''
    max_entropy = 0
    max_letters_worth = 0

    for word in words:
        entropy = Entropy(word)
        # max_letters_worth_value = compute_letters_worth(word)

        if entropy > max_entropy and  len(words)>1:
            best_word  = word
            max_entropy = entropy
            # max_letters_worth = max_letters_worth_value
        elif len(words) == 1:
            best_word = words[0]
    




def check_letters():
    global words

    for i in range(5):
        if chosen_word[i] == best_word[i]:
            words = [x for x in words if x[i] == best_word[i]]
        elif best_word[i] in chosen_word:
            words = [x for x in words if best_word[i] in x and best_word[i] != x[i]]
        elif best_word[i] not in chosen_word:
            words = [x for x in words if best_word[i] not in x]


# chosen_word = "ORALA"

def solve():
    global chosen_word,best_word,max_entropy
    # count_letters()
    check_letters()
    find_best_word()

best_word = "TAREI"


def tester(no_of_cases):
    global chosen_word,best_word,max_entropy,words,no_try

    before = time.time()

    teste_ok = 0
    nr_incercari = 0

    for i in range(no_of_cases[0],no_of_cases[1]):
        words = words2.copy()
        chosen_word = words2[i]
        best_word = 'AURIE'
        max_entropy = 0
        # print('*'+chosen_word)    
        out_txt.write(chosen_word)
        # print("*TAREI")
        out_txt.write(" AURIE")

        i=1
        while not chosen_word == best_word:
            solve()
            # print("*"+best_word)
            out_txt.write(" "+best_word)
            i += 1
        if chosen_word == best_word:
            teste_ok += 1
        nr_incercari += i
        # print("Incercari: ",i)
        
        # print("------------------------------------")
        out_txt.write("\n")
    out_txt.write("\n")
    print("Incercari ok: ",teste_ok)
    out_txt.write("Incercari ok: "+str(teste_ok)+'\n')
    print("Incercari: ",nr_incercari/(no_of_cases[1]-no_of_cases[0]))
    out_txt.write("Incercari: "+str(nr_incercari/(no_of_cases[1]-no_of_cases[0]))+'\n')
    print((time.time()-before)//60,"min ",(time.time()-before)%60,'sec'+'\n')
    out_txt.write(str((time.time()-before)//60)+"min "+str((time.time()-before)%60)+'sec'+'\n')

#test exclusiv pe un range
# tester([0,10])



# uncomment pt multiprocesare
if __name__ == '__main__':

    ranges = [(0,2863),(2863,5727),(5727,8590),(8590,11454)]

    p = Pool(6)

    before = time.time()

    p.map(tester,ranges)

    print((time.time()-before)//60,' min ',(time.time()-before)%60)


#test pe un singur cuvant
def one_word():
    global chosen_word,best_word
    chosen_word = random.sample(words2,1)[0]
    # chosen_word = 'BUCIN'
    best_word = "TAREI"
    print('=='+chosen_word)
    print("*TAREI")
    before = time.time()
    i=1
    while not chosen_word == best_word:
        # print(words)
        # count_letters()
        # print(letters)
        solve()
        # if len(words)<100:
        
        
            # for x in words:
                # print(x,Entropy(x))
        print("*"+best_word)
        i += 1
    print("Incercari: ",i)
    print(time.time()-before)

#Apel pe un singur cuvant   
# one_word()
