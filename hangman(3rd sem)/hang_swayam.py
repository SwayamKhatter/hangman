from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
from word_list import word_list1
from word_list import hint_list_1
from word_list import word_list2
from word_list import hint_list_2
from word_list import word_list3
from word_list import hint_list_3
import random


word_easy=word_list1  
word_medium=word_list2
word_hard=word_list3

window=Tk()
window.title("Hangman")

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"),        PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

#Select Level screen GUI
level=Tk()
level.geometry("300x280")
canvas=Canvas(level, width=1000, height=750, bg="Pink")
canvas.create_text(150, 50, text="  Select Level:\nfor New Game", fill="Black", font=("Helvitica 20 bold"))
b1=Button(level, text="Easy", command=lambda:easy(),font=("Helvetica 12 bold"), bg="green")
b2=Button(level, text="Medium", command=lambda:medium(),font=("Helvetica 12 bold"), bg="yellow")
b3=Button(level, text="Hard", command=lambda:hard(),font=("Helvetica 12 bold"), bg="red")
b1.place(x=124, y=100)
b2.place(x=112, y=140)
b3.place(x=124, y=180)
canvas.pack()


#function to start the new game
def newGame():
    if (b1 is set):
        easy()
    elif (b2 is set):
        medium()
    elif(b3 is set):
        hard()

#function to be executed if the user select Easy level
def easy():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_easy)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    hint1=hint_list_1.get(the_word)
    messagebox.showinfo("Hint of this word is: ", hint1)

    
#function to be executed if the user select Medium level
def medium():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_medium)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    hint2=hint_list_2.get(the_word)
    messagebox.showinfo("Hint of this word is: ", hint2)


#function to be executed if the user select Hard level
def hard():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_hard)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    hint3=hint_list_3.get(the_word)
    messagebox.showinfo("Hint of this word is: ", hint3)


def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    newGame()
        else:
                numberOfGuesses+=1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==11:
                 messagebox.showwarning("GAME OVER", f"The word was: {the_word_withSpaces}")

# #function to display hint
# def Hint():
#     while hint_btn is set:
#         if (newGame is easy):
#             messagebox.showinfo("HINT", f"The HINT for the word is {hint1}")
#         elif (newGame is medium):
#             messagebox.showinfo("HINT", f"The HINT for the word is {hint2}")
#         elif(newGame is hard):
#             messagebox.showinfo("HINT", f"The HINT for the word is {hint3}")
            
  
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

#Displaying all the alphabets on the screen
lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), bg="sky blue", width=4).grid(row=1+n//9, column=n%9)
    n+=1

#hint button
hint_btn=Button(window, text="Hint", command=lambda:Hint(),font=("Helvetica 14 bold"), bg="violet").grid(row=3, column=8)

newGame()    
window.mainloop()