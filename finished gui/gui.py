import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import random
import tkinter.messagebox as tkmb
import time



#generare cuvant random
f = open("cuvinte_wordle.txt", "r")
words = list(x.strip() for x in f)


k2 = 1
word = ''

word_to_guess = random.choice(words)
print(word_to_guess)


def color2():
    global k2
    global pattern,word
    f=open('output.txt','r+')
    f.seek(0)
    word=f.read()
    pattern=''
    
    for i in range (5):
        label = Label(test2, text=word[i].upper())
        
        if word[i] == word_to_guess[i]:
            label.config(background = '#538d4e')
            pattern+='🟩'
        elif word[i] in word_to_guess:
            label.config(background = '#b59f3a')
            pattern+='🟨'
        else:
            label.config(background = '#3a3a3c')
            pattern+='⬜'
        label.config(foreground='#d7dadc',font=('Arial',30),width=2,justify='center',anchor='center')
        label.grid(row=k2, column=i , padx=5, pady=5)
        time.sleep(0.1)
        test2.update()
        # label.pack()
    f=open('output.txt','w',encoding='utf-8')
    f.write(pattern)
    print(pattern)
    k2 += 1

    f=open('output.txt','r+',encoding='utf-8')
    word = f.read()

    f=open('output.txt','r+',encoding='utf-8')

    while word == f.read():
         f=open('output.txt','r+',encoding='utf-8')
         f.seek(0)
    
    if word == '🟩🟩🟩🟩🟩':
        return
    
    time.sleep(0.1)
    color2()
    


    


def instantiate_auto():
    global test2
    test2 = tk.Tk()
    test2.config(background='#151515')
    print('====',word_to_guess)

    test2.title("Wordle")
    label1=Label(test2, text = word_to_guess, font= ('Calibri', 30), justify = 'center', anchor=CENTER,background='#151515',foreground='#f5f5f5')
    label1.grid(row=0, columnspan=5, sticky=N+S+E+W,padx=30,pady=10)

    color2()

    
    # test2.geometry("720x720")
   
    test2.mainloop()


instantiate_auto()


