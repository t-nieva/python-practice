from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

BG_COLOR = "#FEF9E1"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password =  [choice(letters) for _ in range(randint(8, 10))]
    password +=  [choice(numbers) for _ in range(randint(2, 4))]
    password +=  [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password)
    random_pass_str = ''.join(password)
    pass_entry.delete(0,END)
    pass_entry.insert(0, random_pass_str)
    pyperclip.copy(random_pass_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    details_msg = (f"There are the details entered: "
                   f"\nWebsite: {website} "
                   f"\nEmail: {email} "
                   f"\nPassword: {password} "
                   f"\nIs it ok to save?")
    validation_msg = "Please don't leave any field empty!"
    if not website or not email or not password:
        messagebox.showwarning(title="Oops!", message=validation_msg)
    else:
        is_ok = messagebox.askokcancel(title=website, message=details_msg)
        if is_ok:
            with open("./output/data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

website_label = Label(text="Website:", bg=BG_COLOR)
website_label.grid(row=1, column=0)
website_label.config(pady=10)

email_label = Label(text="Email/Username:", bg=BG_COLOR)
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:", bg=BG_COLOR)
pass_label.grid(row=3, column=0)
pass_label.config(pady=10)

website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@gmail.com")

pass_entry = Entry(width=28)
pass_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", background="white")
generate_btn.grid(row=3, column=2)
generate_btn.config(padx=1, pady=0, command=generate_password)

add_btn = Button(text="Add", background="white", width=45,)
add_btn.grid(row=4, column=1, columnspan=2)
add_btn.config(pady=0, padx=0, command=save)

canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

window.mainloop()
