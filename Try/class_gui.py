import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import random
import tkinter.messagebox as tkmb
import time
import  second
from multiprocessing import Process

class Gui():

    def __init__(self):

        f = open("cuvinte_wordle.txt", "r")
        words = list(x.strip() for x in f)


        self.k2 = 1
        self.word = ''

        self.word_to_guess = random.choice(words)
        self.instantiate_auto()

    def color2(self):
        # global k2
        # global pattern,word
        f=open('output.txt','r+')
        f.seek(0)
        self.word=f.read()
        pattern=''
        
        for i in range (5):
            label = Label(test2, text=self.word[i].upper())
            
            if self.word[i] == self.word_to_guess[i]:
                label.config(background = '#538d4e')
                pattern+='🟩'
            elif self.word[i] in self.word_to_guess:
                label.config(background = '#b59f3a')
                pattern+='🟨'
            else:
                label.config(background = '#3a3a3c')
                pattern+='⬜'
            label.config(foreground='#d7dadc',font=('Arial',30),width=2,justify='center',anchor='center')
            label.grid(row=self.k2, column=i+1 , padx=3, pady=5)
            time.sleep(0.1)
            test2.update()
            # label.pack()
        f=open('output.txt','w',encoding='utf-8')
        f.write(pattern)
        print(pattern)
        self.k2 += 1

        f=open('output.txt','r+',encoding='utf-8')
        self.word = f.read()

        f=open('output.txt','r+',encoding='utf-8')

        while self.word == f.read():
            f=open('output.txt','r+',encoding='utf-8')
            f.seek(0)
        
        if self.word == '🟩🟩🟩🟩🟩':
            return
        
        time.sleep(0.1)
        self.color2()

    def new_game(self):

        second.auto()
        self.instantiate_auto()

    def instantiate_auto(self):
        global test2
        
        test2 = tk.Tk()
        test2.config(background='#151515')
        test2.title("Wordle")
        print('====',self.word_to_guess)

        for x in range(7):
            l = Label(test2,text=" ",font= ('Calibri', 30),background='#151515')
            l.grid(row=0, column=x, sticky=N+S+E+W,padx=30,pady=10)

        label1=Label(test2, text = self.word_to_guess, font= ('Calibri', 30), justify = 'center', anchor=CENTER,background='#151515',foreground='#f5f5f5')
        label1.grid(row=0, columnspan=7, sticky=N+S+E+W,padx=30,pady=10)

        


        self.color2()

        def destroy(self):
            test2.destroy()
            self.__init__()


        # test2.geometry("720x720")
        
        if self.word == '🟩🟩🟩🟩🟩':
            again = Label(test2,text="Again?",font=('',15),foreground='#f1f1f1',background='#252525',width=10,anchor='center')
            again.bind('<Button-1>',lambda self:[test2.destroy(),Process(target=second.auto).start(),Process(target=Gui).start()])
            again.grid(row=self.k2+1,columnspan=7,padx=10,pady=15)
            test2.update()

        test2.mainloop()



if __name__ == '__main__':
    
    gui = Process(target=Gui)
    bot = Process(target=second.auto)

    gui.start()
    bot.start()

    bot.join()
    gui.join()

# second.auto()
# g = Gui()
# g.instantiate_auto()