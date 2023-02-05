import tkinter as tk
import pandas as pd

data = pd.read_csv("./data/ro_en_1-1999.csv")

BACKGROUND_COLOR = "#B1DDC6"
piece = data.sample()

root = tk.Tk()
root.title("Flash Cards")
root.config(bg=BACKGROUND_COLOR)

flip_timer = root.after(99999, print)


def flip_card():
    global piece, flip_timer
    match canvas.itemcget(title, "text"):
        case "Romanian":
            canvas.itemconfig(title, text="English", fill="white")
            canvas.itemconfig(card, image=canvas_img_back)
            canvas.itemconfig(word, text=piece.at[piece.index[0], "en"], fill="white")
        case "English":
            canvas.itemconfig(title, text="Romanian", fill="black")
            canvas.itemconfig(word, text=piece.at[piece.index[0], "ro"], fill="black")
            canvas.itemconfig(card, image=canvas_img_front)
        case _:
            canvas.itemconfig(title, text="Romanian")
            canvas.itemconfig(word, text=piece.at[0, "ro"])
    flip_timer = root.after(3000, flip_card)


def show_word():
    global piece, flip_timer
    root.after_cancel(flip_timer)
    piece = data.sample()
    canvas.itemconfig(title, text="Romanian", fill="black")
    canvas.itemconfig(word, text=piece.at[piece.index[0], "ro"], fill="black")
    canvas.itemconfig(card, image=canvas_img_front)
    flip_timer = root.after(3000, flip_card)


def clear_word():
    global piece, data
    data = data.drop(index=piece.index[0])
    show_word()


canvas_img_front = tk.PhotoImage(file="./images/card_front.png")
canvas_img_back = tk.PhotoImage(file="./images/card_back.png")

button_right_img = tk.PhotoImage(file="./images/right.png")
button_wrong_img = tk.PhotoImage(file="./images/wrong.png")

canvas = tk.Canvas(root, width=800, height=526, background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
card = canvas.create_image(400, 263, image=canvas_img_front)
canvas.grid(column=0, row=0, columnspan=2, pady=50, padx=50)

title = canvas.create_text(400, 140, text="Title", font=("URW Bookman", 19, "italic"))
word = canvas.create_text(400, 300, text="Word", font=("URW Bookman", 40, "bold"))

button_right = tk.Button(root, image=button_right_img, highlightthickness=0, command=clear_word)
button_right.grid(column=0, row=1, pady=25)

button_wrong = tk.Button(root, image=button_wrong_img, command=show_word)
button_wrong.grid(column=1, row=1, pady=25)


show_word()

root.mainloop()
