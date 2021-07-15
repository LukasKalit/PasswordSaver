import tkinter
from tkinter import *

YELLOW = "#D9DD6B"
CITRUS = "#ECEFA4"
RED = "#D54C4C"
MAROON = "#8D2828"


root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20, bg=CITRUS)

canvas = Canvas(width=200, height=200, bg=CITRUS, highlightthickness=0)
background_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=background_photo)
canvas.grid(row=0, column=1)

label = Label(text="Website")


# ----------------------------- PASSWORD GENERATOR -------------------------------#

# ----------------------------- SAVE PASSWORD -------------------------------#

# ----------------------------- UI SETUP -------------------------------#

root.mainloop()
