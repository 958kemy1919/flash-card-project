from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

random_card = {}

def next_card():
    global random_card,timer
    window.after_cancel(timer)
    random_card = random.choice(to_learn)
    canvas.itemconfig(text_title,text = "French",fill="black")
    canvas.itemconfig(text_word,text = random_card["French"],fill="black")
    canvas.itemconfig(backgrund_color,image=card_front_img)
    timer = window.after(3000,translate)

def translate():
    global random_card
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_word, text=random_card["English"], fill="white")
    canvas.itemconfig(backgrund_color, image=card_back_img)


def to_known():
    to_learn.remove(random_card)
    new_file = pandas.DataFrame(to_learn)
    new_file.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer = window.after(3000,next_card)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_png = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
backgrund_color = canvas.create_image(400,263,image=card_front_img)
text_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
text_word = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_button = Button(image=wrong_png,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

right_button = Button(image=right_img,highlightthickness=0,command=to_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()
