import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
import time
import class_bot
from multiprocessing import Process

class Gui:
    def __init__(self):

        f = open("cuvinte_wordle.txt", "r")
        #List with all words
        words = list(x.strip() for x in f)

        self.no_row = 1
        self.word = ""

        #Random word picked
        self.word_to_guess = random.choice(words)
        #Start the game
        self.init_auto()

    #Adds the tried word to the screen
    #and highlight the letters
    def add_word(self):

        #The file used to intercomunicate
        f = open("output.txt", "r+")
        f.seek(0)
        
        #the word received from the bot
        self.word = f.read()
        #Word highlighted pattern used to intercomunicate
        pattern = ""

        for i in range(5):
            #Label with a letter highlighted
            label = Label(root, text=self.word[i].upper())

            if self.word[i] == self.word_to_guess[i]:
                label.config(background="#538d4e")
                pattern += "🟩"

            elif self.word[i] in self.word_to_guess:
                label.config(background="#b59f3a")
                pattern += "🟨"

            else:
                label.config(background="#3a3a3c")
                pattern += "⬜"
                
            label.config(
                foreground="#d7dadc",
                font=("Arial", 30),
                width=2,
                justify="center",
                anchor="center",
            )
            label.grid(row=self.no_row, column=i+1, padx=3, pady=5)

            #Animation effect
            time.sleep(0.1)
            root.update()

        f = open("output.txt", "w", encoding="utf-8")
        #Write the highlighted pattern
        f.write(pattern)

        #Move to next row to display next word
        self.no_row += 1

        f = open("output.txt", "r+", encoding="utf-8")
        self.word = f.read()

        #Wait unil the bot program writes 
        #next word to try 
        f = open("output.txt", "r+", encoding="utf-8")
        while self.word == f.read():
            f = open("output.txt", "r+", encoding="utf-8")
            f.seek(0)

        #If the chosen word is found
        #it asked you for the next turn
        if self.word == "🟩🟩🟩🟩🟩":
            return

        #If the word is not guessed
        time.sleep(0.1)
        self.add_word()

    def init_auto(self):
        global root

        #Initiate the main root window
        root = tk.Tk()
        root.config(background="#151515")
        root.title("Wordle")
        width = 340  # Width
        height = 720  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        #Center the window
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        #Aesthetics fow window
        for x in range(7):
            l = Label(
                root, 
                text=" ",
                font=("Calibri", 30), 
                background="#151515"
            )
            l.grid(row=0, column=x, sticky=N + S + E + W, padx=10, pady=10)

        label1 = Label(
            root,
            text=self.word_to_guess,
            font=("Calibri", 30),
            justify="center",
            anchor=CENTER,
            background="#151515",
            foreground="#f5f5f5",
        )
        label1.grid(row=0, columnspan=7, sticky=N + S + E + W, padx=30, pady=10)

        self.add_word()

        #If the game is finished
        #ask for another one
        if self.word == "🟩🟩🟩🟩🟩":
            again = Label(
                root,
                text="Again?",
                font=("", 15),
                foreground="#f1f1f1",
                background="#252525",
                width=10,
                anchor="center",
            )
            again.bind(
                "<Button-1>",
                lambda self: [
                    root.destroy(),
                    Process(target=class_bot.auto).start(),
                    Process(target=Gui).start(),
                ],
            )
            again.grid(row=self.no_row + 1, columnspan=7, padx=10, pady=15)
            root.update()

        root.mainloop()


if __name__ == "__main__":

    #Gui process
    gui = Process(target=Gui)
    #Bot process
    bot = Process(target=class_bot.auto)

    gui.start()
    bot.start()

    bot.join()
    gui.join()
