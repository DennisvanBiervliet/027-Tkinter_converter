from tkinter import *


def calculate():
    entry_miles = float(miles_entry.get())
    km = round(entry_miles * 1.6093, 2)
    calculated_label.config(text=km)


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels (1 - 4)
miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculated_label = Label(text="0")
calculated_label.config(padx=5, pady=5)
calculated_label.grid(column=1, row=1)

# Entry
miles_entry = Entry()
miles_entry.config(width=5)
miles_text = miles_entry.get()

miles_entry.grid(column=1, row=0)

# Button
calculate_button = Button()
calculate_button.config(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()