from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if not website or not email or not password:
        messagebox.showwarning(title="Oops!", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=(f"\nEmail: {email} \nPassword: {password} "
                   f"\nIs it ok to save?"))
        if is_ok:
            try:
                with open("./output/data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("./output/data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("./output/data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("./output/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(message="No details for the website exists.")

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

website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@gmail.com")

pass_entry = Entry(width=28)
pass_entry.grid(row=3, column=1)

search_btn = Button(text="Search", bg="white", width=16)
search_btn.grid(row=1, column=2)
search_btn.config(padx=1, pady=0, command=find_password)

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
