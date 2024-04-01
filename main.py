import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(window, width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_frond_img = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_frond_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = tk.PhotoImage(file="images/wrong.png")
button = tk.Button(image=cross_img, highlightthickness=0)
button.grid(row=1, column=0)

check_img = tk.PhotoImage(file="images/right.png")
unknown_word_button = tk.Button(image=cross_img, highlightthickness=0)
unknown_word_button.grid(row=1, column=0)

btn_right_img = tk.PhotoImage(file="images/right.png")
known_word_button = tk.Button(image=btn_right_img, highlightthickness=0)
known_word_button.grid(row=1, column=1)

window.mainloop()
