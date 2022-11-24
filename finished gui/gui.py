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

#k1 = 3
k2 = 3
word = ''

#tkinter interfata
# root = tk.Tk()
# root.title("Wordle Game")
# root.geometry('800x800')
word_to_guess = random.choice(words)
print(word_to_guess)

'''def clear():
    for widgets in root:
        widgets.destroy()
  '''
#def color1():
#     global k1
#     word=e1.get()
#     if word in words:
#         if not word == word_to_guess:
#             for i in range (5):
#                     label = Label(test1, text=word[i].upper(), relief=GROOVE)
#                     label.grid(row=k1, column=i , padx=10, pady=10)
#                     if word[i] == word_to_guess[i]:
#                         label.config(foreground = 'green')
#                     elif word[i] in word_to_guess:
#                         label.config(foreground = 'yellow')
#                     else:
#                         label.config(foreground= 'white')
#     e1.delete(0, 'end')
#     k1 += 1

def wait_for_response():
    global word
    output_txt = open('output.txt','r',encoding='utf-8')
    word = output_txt.read()
    output_txt.seek(0)
    while word == output_txt.read():
        time.sleep(0.5)
        output_txt.seek(0)
        print(output_txt.read())
        word = output_txt.read()
        
        output_txt = open('output.txt','r',encoding='utf-8')
    
    output_txt.close()


def color2():
    global k2
    global pattern,word
    f=open('output.txt','r+')
    f.seek(0)
    word=f.read()
    pattern=''
    
    for i in range (5):
        label = Label(test2, text=word[i].upper(), relief=GROOVE)
        
        if word[i] == word_to_guess[i]:
            label.config(background = 'green')
            pattern+='🟩'
        elif word[i] in word_to_guess:
            label.config(background = 'yellow')
            pattern+='🟨'
        else:
            label.config(background = 'white')
            pattern+='⬜'
        label.config(foreground='black',font=('Aial',30),width=2,justify='center',anchor='center')
        label.grid(row=k2, column=i , padx=10, pady=10)
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
    
    time.sleep(0.3)
    color2()
    


    



# def instantiate_manual():
    # root.destroy()
    # global test1
    # test1 = tk.Tk()
    # global e1
    # e1 = Entry(test1, width=50)
    # e1.grid(column = 0, row=1, columnspan=10)
    # button_go=Button(test1, text='GO!', command= color1)
    # button_go.grid(column = 10, row=1)
    # test1.geometry("800x800")
    # test1.title("Manual Mode")
    # label1=Label(test1, text = 'Enter the word...', font= ('Times New Roman', 30), justify = CENTER, anchor=CENTER)
    # label1.grid(row=0, column=5 ,columnspan = 15, sticky=N+S+E+W)
    # test1.mainloop() 
def instantiate_auto():
    # root.destroy()
    global test2
    test2 = tk.Tk()
    test2.config(background='black')
    print('====',word_to_guess)

    test2.title("Wordle")
    label1=Label(test2, text = 'Entry', font= ('Times New Roman', 30), justify = 'center', anchor=CENTER,background='black',foreground='white')
    label1.grid(row=0, columnspan=5, sticky=N+S+E+W)

    color2()

    
    # test2.geometry("720x720")
   
    test2.mainloop()

#Butoane meniu
# label1 = Label(root, text = 'Wordle Game', font=('Times New Roman', 40, 'bold')).pack(padx=30, pady=100)
# #button1 = Button(root, text = "Manual", command =  instantiate_manual).pack()
# button2 = Button(root, text = "Auto", command = instantiate_auto).pack()
instantiate_auto()

# root.mainloop()

