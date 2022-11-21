import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import random
from tkinter import colorchooser




#generare cuvant random
f = open("cuvinte.txt", "r")
words = list(x.strip() for x in f)

#tkinter interfata
root = tk.Tk()
root.title("Wordle Game")
root.geometry('800x800')
YELLOW='#b89e1f'
GREEN='#29d93b'
P='#5e1e43'



            
        
    



def pick_word():
    return random.choice(words)
    #guess =  Label(root, text = 'Cuvântul de ghicit este: {}'.format(random_word)).pack()
    
  
def color(word):
    word_to_guess= pick_word()
    word=e.get()
    if word in words:
        if word == word_to_guess:
            messagebox.showinfo('Winner', 'Felicitari ai castigat')
        else:
            k = 0
            for letter in word:
                if letter == word_to_guess[k]:
                   pass
                    
            
            
    

def instantiate_manual():
    root.destroy()
    test1 = tk.Tk()
    global e
    e = Entry(test1, width=50)
    e.pack(side=BOTTOM)
    def ef():
        word = e.get()
        label3=Label(test1, text=word)
        label3.pack()
        label3.config(font=('Times New Roman', 18), justify=CENTER, highlightbackground='red')
    button_go=Button(test1, text='GO!', command=ef)
    button_go.pack(side=BOTTOM)
    test1.geometry("800x800")
    test1.title("Manual Mode")
    label1=Label(test1, text = 'Enter the word...', font= ('Times New Roman', 30))
    label1.pack()
    test1.mainloop()

    
    
def instantiate_auto():
    root.destroy()
    test2 = tk.Tk()
    test2.geometry("800x800")
    test2.title("Auto_Mode")
    Label(test2, text = "Press Enter...", font=('Times new Roman', 20)).pack()
    btn = Button(test2, text = "Genereaza cuvantul random", command = pick_word).pack()
    test2.mainloop()
    


#Butoane meniu
label1 = Label(root, text = 'Wordle Game', font=('Times New Roman', 40, 'bold')).pack(padx=30, pady=100)
button1 = Button(root, text = "Manual", command =  instantiate_manual).pack()
button2 = Button(root, text = "Auto", command = instantiate_auto).pack()

root.mainloop()