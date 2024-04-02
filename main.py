import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_time = 3000
words_to_learn_filename = "data/words_to_learn.csv"

def get_words_to_learn():
    with open(words_to_learn_filename, "r") as file:
        data = pd.read_csv(file)
        return data.to_dict(orient="records")

words_to_learn = get_words_to_learn()
    
def get_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(flip_time, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

def learn_word():
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv(words_to_learn_filename, index=False)
    get_next_card()

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(flip_time, flip_card)

canvas = tk.Canvas(window, width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_word_button_icon = tk.PhotoImage(file="images/wrong.png")
unknown_word_button = tk.Button(image=unknown_word_button_icon, highlightthickness=0, command=get_next_card)
unknown_word_button.grid(row=1, column=0)

known_word_button_icon = tk.PhotoImage(file="images/right.png")
known_word_button = tk.Button(image=known_word_button_icon, highlightthickness=0, command=learn_word)
known_word_button.grid(row=1, column=1)

get_next_card()
window.mainloop()
