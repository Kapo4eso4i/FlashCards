import tkinter as tk
import pandas as pd

data = pd.read_csv("./data/ro_en_1-1999.csv")

BACKGROUND_COLOR = "#B1DDC6"


def show_word():
    piece = data.sample(ignore_index=True)


def flip_card(piece):
    match canvas.itemcget(title, "text"):
        case "Romanian":
            canvas.itemconfig(title, "English")
            canvas.itemconfig(word, text=piece.at[0, "en"])
        case "English":
            canvas.itemconfig(title, "Romanian")
            canvas.itemconfig(word, text=piece.at[0, "ro"])


root = tk.Tk()
root.title("Flash Cards")
root.config(bg=BACKGROUND_COLOR)

canvas_img_front = tk.PhotoImage(file="./images/card_front.png")
canvas_img_back = tk.PhotoImage(file="./images/card_back.png")

button_right_img = tk.PhotoImage(file="./images/right.png")
button_wrong_img = tk.PhotoImage(file="./images/wrong.png")

canvas = tk.Canvas(root, width=800, height=526, background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
canvas.create_image(400, 263, image=canvas_img_back)
canvas.grid(column=0, row=0, columnspan=2, pady=50, padx=50)

title = canvas.create_text(400, 140,text="Title", font=("URW Bookman", 19, "italic"))
word = canvas.create_text(400, 300, text="Word", font=("URW Bookman", 40, "bold"))

button_right = tk.Button(root, image=button_right_img, highlightthickness=0, command=show_word)
button_right.grid(column=0, row=1, pady=25)

button_wrong = tk.Button(root, image=button_wrong_img)
button_wrong.grid(column=1, row=1, pady=25)


root.mainloop()

