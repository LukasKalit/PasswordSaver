from tkinter import *

YELLOW = "#D9DD6B"
CITRUS = "#ECEFA4"
RED = "#D54C4C"
MAROON = "#8D2828"

with open("config.txt", "r") as settings:
    data_settings = settings.read()


def gen_password():
    pass


def add_password():
    save(web_name_entry.get(), email_username_entry.get(), password_entry.get())
    pass


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


# ----------------------------- SAVE PASSWORD -------------------------------#


def save(web, user_mail, password):

    data_string = f"{web} | {user_mail} | {password} \n"
    with open("Your_passwords.txt", "a") as data:
        data.write(data_string)


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
web_name_entry = Entry(width=40)
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
                                  font=("Arial", 8, "normal"), command=gen_password)
generate_password_button.grid(row=3, column=2,  sticky="E")
add_button = Button(width=39, text="Add", font=("Arial", 8, "normal"),
                    command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")
gear_photo = PhotoImage(file="gear.png")
config_button = Button(image=gear_photo, command=open_config_window)
config_button.grid(row=0, column=2, sticky="NE")

mainloop()
