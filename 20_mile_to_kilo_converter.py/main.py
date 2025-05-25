from tkinter import *

def miles_to_km():
    miles =float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
