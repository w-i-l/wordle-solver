import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import random
#from tkinter import colorchooser - trebuie sa vedem cu culorile
from computer_plays import find_best_word


#generare cuvant random
f = open("cuvinte.txt", "r")
words = list(x.strip() for x in f)


out_to_computer = open("computer_in.txt", "w+")

#tkinter interfata
root = tk.Tk()
root.title("Wordle Game")
root.geometry('800x800')

                    
    



#random word picking
def pick_word():
    global word_to_guess
    word_to_guess = random.choice(words)
    Label(test2, text = word_to_guess, font=('Times new Roman', 20)).pack()
    #guess =  Label(root, text = 'Cuvântul de ghicit este: {}'.format(random_word)).pack()






def get_computer_guess():
    global next_word
    next_word = find_best_word()
    Label(game, text = next_word, font = ('Times new Roman', 20)).pack()
    return next_word



#aici trebuie sa coloram efectiv situatia
    '''
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
                                    
    '''



def show_it():
    Label(game, text = next_word)


def instantiate_game():
    test2.destroy()
    global game
    game = tk.Tk()
    game.title("A visualition of the the computer plays WORDLE")
    game.geometry("800x800")
    Label(game, text = "Cuvantul de ghicit este {}".format(word_to_guess), font= ('Times New Roman', 30)).pack()
    Label(game, text = "Cele mai bune guess-uri ale computerului sunt:").pack()
    Button(game, text = "Next best word", command = lambda : [color_word("TAREI")]).pack()
    



#aici trimit pattern-ul cuvantului catre un file pe care il acceseaza programul Radu-Mishu

def color_word(guessed_word):

    pattern_list = [""] * 5
    k = 0
    for letter in guessed_word:
        if letter  == word_to_guess[k]:
            pattern_list.append("verde")
        elif letter in word_to_guess and letter != word_to_guess[k]:
            pattern_list.append("galben")
        else: pattern_list.append("gri") 

    for el in pattern_list:
        out_to_computer.write(el)
        out_to_computer.write('\n')







    
#pauza
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
    global test2
    test2 = tk.Tk()
    test2.geometry("800x800")
    test2.title("Auto_Mode")
    text = Label(test2, text = "Apasa mai jos pentru a incepe", font=('Times new Roman', 20)).pack()
    btn = Button(test2, text = "Genereaza cuvantul random", command = lambda : [pick_word(), instantiate_game()]).pack()

   
    
    test2.mainloop()
    




#Butoane meniu
label1 = Label(root, text = 'Wordle Game', font=('Times New Roman', 40, 'bold')).pack(padx=30, pady=100)
button1 = Button(root, text = "Manual", command =  instantiate_manual).pack()
button2 = Button(root, text = "Auto", command = instantiate_auto).pack()


root.mainloop() 
