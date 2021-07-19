from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

YELLOW = "#D9DD6B"
CITRUS = "#ECEFA4"

# ----------------------------- CONFIG WINDOW --------------------------------------------#


def open_config_window():

    def save_default(x):
        with open("config.txt", "w") as data:
            data.write(x)
        setting_default()

    def click_apply():
        save_default(default_email.get())

    config_window = Toplevel(root)
    config_window.title("Config")
    config_window.config(padx=20, pady=20, bg=CITRUS)

    apply_button = Button(config_window, text="Apply", command=click_apply, width=10)
    apply_button.grid(row=1, column=1)

    default_email = Entry(config_window, width=22)
    default_email.grid(row=1, column=0)
    default_email.focus()

    config_info = Label(config_window, text="Set your default Email/Username", bg=CITRUS)
    config_info.grid(row=0, column=0, columnspan=2)
    pass


# ----------------------------- PASSWORD GENERATOR -------------------------------#

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [(random.choice(letters)) for _ in range(random.randint(8, 10))]
    password_list += [(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    password_list += [(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete("0", "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----------------------------- SAVE PASSWORD -------------------------------#


def save():

    web = web_name_entry.get()
    user_mail = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "email": user_mail,
            "password": password
        }
    }

    if web == "" or password == "" or user_mail == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data:
                # Reading old data
                data_file = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        else:
            # Updating old data with new data
            data_file.update(new_data)
            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(data_file, data, indent=4)

        finally:
            web_name_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Info", message="Done")
# ------------------------------ FIND PASSWORD ---------------------------------#


def search_website():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="No Data File Found!\nCreate data file first")

    else:
        if web_name_entry.get() in data:
            email_data = data[web_name_entry.get()]["email"]
            password_data = data[web_name_entry.get()]["password"]
            messagebox.showinfo(title=web_name_entry.get(),
                                message=f"Email/User_name: {email_data}\nPassword: {password_data}")
            pyperclip.copy(password_data)
        else:
            messagebox.showinfo(title="Error",
                                message="No information about this website")


# ----------------------------- UI SETUP -------------------------------#

root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50, bg=CITRUS)

canvas = Canvas(width=130, height=200, bg=CITRUS, highlightthickness=0)
background_photo = PhotoImage(file="logo.png")
canvas.create_image(60, 94, image=background_photo)
canvas.grid(row=0, column=1)

# labels
web_name_label = Label(text="Website:", font=("Arial", 10, "normal"), bg=CITRUS)
web_name_label.grid(row=1, column=0, sticky="E")
email_username_label = Label(text="Email/Username:", font=("Arial", 10, "normal"), bg=CITRUS)
email_username_label.grid(row=2, column=0, sticky="E")
password_label = Label(text="Password:", font=("Arial", 10, "normal"), bg=CITRUS)
password_label.grid(row=3, column=0, sticky="E")

# entries
web_name_entry = Entry(width=22)
web_name_entry.grid(row=1, column=1, columnspan=2, sticky="W")
web_name_entry.focus()
email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="W")


def setting_default():
    with open("config.txt", "r") as config_file:
        default_data = config_file.read()
    email_username_entry.delete("0", "end")
    email_username_entry.insert(0, default_data)


setting_default()

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1, sticky="W")

# buttons
generate_password_button = Button(width=16, text="Generate Password",
                                  font=("Arial", 8, "normal"), command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="E")
add_button = Button(width=39, text="Add", font=("Arial", 8, "normal"), command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")
gear_photo = PhotoImage(file="gear.png")
config_button = Button(image=gear_photo, command=open_config_window)
config_button.grid(row=0, column=2, sticky="NE")
search_button = Button(width=16, text="Search",
                       font=("Arial", 8, "normal"), command=search_website)
search_button.grid(row=1, column=2, sticky="E")

mainloop()
