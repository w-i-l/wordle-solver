import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import random
from tkinter import Widget
from termcolor import colored
from tkinter import colorchooser
from tkmacosx import *
import tkinter.messagebox as tkmb




#generare cuvant random
f = open("cuvinte.txt", "r")
words = list(x.strip() for x in f)

k = 3


#tkinter interfata
root = tk.Tk()
root.title("Wordle Game")
root.geometry('800x800')
word_to_guess = random.choice(words)
print(word_to_guess)

'''def clear():
    for widgets in root:
        widgets.destroy()
  '''
def color():
    global k
    word=e.get()
    #if word in words:
    if word == word_to_guess:
            tk.messagebox.showinfo('CF')
    else:
        for i in range (5):
                label = Label(test1, text=word[i], relief=GROOVE)
                label.grid(row=k, column=i , padx=10, pady=10)
        
                if word[i] == word_to_guess[i]:
                    label.config(foreground = 'green')
                elif word[i] in word_to_guess:
                    label.config(foreground = 'yellow')
                else:
                    label.config(foreground= 'white')
    k += 1
                
            


def instantiate_manual():
    root.destroy()
    global test1
    test1 = tk.Tk()
    global e
    e = Entry(test1, width=50)
    e.grid(column = 0, row=1, columnspan=10)
    e.bind('<Return>',color)
    '''button_go=Button(test1, text='GO!', command= color)'''
    '''button_go.grid(column = 10, row=1)'''
    test1.geometry("800x800")
    test1.title("Manual Mode")
    label1=Label(test1, text = 'Enter the word...', font= ('Times New Roman', 30), justify = CENTER, anchor=CENTER)
    label1.grid(row=0, column=5 ,columnspan = 15, sticky=N+S+E+W)
    test1.mainloop()

    
    
def instantiate_auto():
    root.destroy()
    test2 = tk.Tk()
    test2.geometry("800x800")
    test2.title("Auto_Mode")
    Label(test2, text = "Press Enter...", font=('Times new Roman', 20)).grid()
    btn = Button(test2, text = "Genereaza cuvantul random", command = pick_word).pack()
    test2.mainloop()
    


#Butoane meniu
label1 = Label(root, text = 'Wordle Game', font=('Times New Roman', 40, 'bold')).pack(padx=30, pady=100)
button1 = Button(root, text = "Manual", command =  instantiate_manual).pack()
button2 = Button(root, text = "Auto", command = instantiate_auto).pack()

root.mainloop()