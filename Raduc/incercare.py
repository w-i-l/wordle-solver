from cmath import log
from collections import Counter
import math

LettersInOrder=['A','I','E','U','R','T','O','L','S','C','N','M','P','D','B','G','Z','V','F','H','J','X','K','Y','W','Q']
Word='AUIRE'

Words=open('D:\python projects\wordl\ASM-Project\Raduc\cuvinte.txt').read().split('\n')


letters=['a','b','c']
def ListCleaner(List,Letters):
    for word in List:
        if ''.join(Letters) not in word:
            return 1

def LetterCounter(NewList):

    N=len(''.join(NewList)) #Total number of letters in list
    Letters={}
    Letters=Counter(''.join(NewList)) #Frequency of letters
    return N,Letters
def EntropyOfWords(List):
    R=LetterCounter(List) #R is the Total Number of letters and the frequency of each
    ListOfEntropy=[]
    for word in List:
        Entropy=0
        for letter in word:
            p=R[1][letter]/R[0] #probability of each letter in word
            Entropy+=-(p*math.log(p,2)) #calc entropy of words in list
        ListOfEntropy.append(Entropy)
    c=0
    for word in List:
        if word=='ABILE':
            break
        c+=1
    print(ListOfEntropy[c])
            
    #BestWordIndex=ListOfEntropy.index(max(ListOfEntropy)) #Index of the word with the best entropy
    
   # return List[BestWordIndex]
def WordTest(Word,Guess,List):
      #  if letter not in Word:
      pass
            
EntropyOfWords(Words)
    
        
    
    

