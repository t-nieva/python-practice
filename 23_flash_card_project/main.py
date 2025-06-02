from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FLIP_DELAY_MS = 5000
FONT_NAME = "Ariel"

# FREQUENCY_WORD_LIST_PATH = "data/french_words.csv"
# FOREIGN_LANG = "French"
# TRANSLATION_LANG = "English"

FREQUENCY_WORD_LIST_PATH = "data/english_ukrainian.csv"
FOREIGN_LANG = "English"
TRANSLATION_LANG = "Ukrainian"

current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(FREQUENCY_WORD_LIST_PATH)
to_learn = data.to_dict(orient="records")

# ---------------------------- SAVE PROGRESS ------------------------------- #
def update_data():
    to_learn.remove(current_card)
    if not to_learn:
        if os.path.exists("data/words_to_learn.csv"):
            os.remove("data/words_to_learn.csv")
        canvas.delete(card_title)
        canvas.delete(card_word)
        messagebox.showinfo("Done!", "You learned all the words 🎉")
        window.quit()
        return
    else:
        pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
        next_card()


# ---------------------------- CREATE CARD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=FOREIGN_LANG, fill="black")
    canvas.itemconfig(card_word, text=f"{current_card[FOREIGN_LANG]}", fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    window.after(FLIP_DELAY_MS, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_bg, image=back_img)
    canvas.itemconfig(card_title, text=TRANSLATION_LANG, fill="white")
    canvas.itemconfig(card_word, text=f"{current_card[TRANSLATION_LANG]}", fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(FLIP_DELAY_MS, func=flip_card)

# ---------------------------- FRONT SETUP ------------------------------- #
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text=f"{FOREIGN_LANG}", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTON SETUP ------------------------------- #
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")

btn_right = Button(image=img_right, border=0, bg=BACKGROUND_COLOR, highlightthickness=0,
                   activebackground=BACKGROUND_COLOR)
btn_right.grid(row=1, column=1)
btn_right.config(command=update_data)

btn_wrong = Button(image=img_wrong, border=0, bg=BACKGROUND_COLOR, highlightthickness=0,
                   activebackground=BACKGROUND_COLOR)
btn_wrong.grid(row=1, column=0)
btn_wrong.config(command=next_card)

next_card()

window.mainloop()
