import tkinter


def miles_to_km_conversion():
    miles_to_km = round(float(text_input.get()) * 1.60934, 1)
    to_km_label.config(text=miles_to_km)


# Window
window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=25, pady=25)
# window.minsize(width=500, height=300)

# Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

to_km_label = tkinter.Label(text="0", font=("Arial", 12))
to_km_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate", command=miles_to_km_conversion)
button.grid(column=1, row=2)

# Text entry, 1 line
text_input = tkinter.Entry(width=5)
text_input.insert(tkinter.END, string=0)
text_input.grid(column=1, row=0)


window.mainloop()
