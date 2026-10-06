import tkinter as tk
from tkinter import ttk

def add():
    name = name_entry.get()
    age = age_entry.get()
    genre = genre_entry.get()

    if name == "" or age == "" or genre == "":
        message.config(text="Please complete all fields")
    else:
        table.insert("", "end", values=(name, age, genre))
        message.config(text="Added successfully")

def update():
    selected = table.selection()

    if selected:
        name = name_entry.get()
        age = age_entry.get()
        genre = genre_entry.get()

        table.item(selected, values=(name, age, genre))
        message.config(text="Updated successfully")
    else:
        message.config(text="Select a row first")

def delete():
    selected = table.selection()

    if selected:
        table.delete(selected)
        message.config(text="Deleted successfully")
    else:
        message.config(text="Select a row first")

def clear():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)

    for x in table.get_children():
        table.delete(x)

    message.config(text="")

def exit():
    window.destroy()

def click(event):
    selected = table.selection()

    if selected:
        data = table.item(selected, "values")

        name_entry.delete(0, tk.END)
        name_entry.insert(0, data[0])

        age_entry.delete(0, tk.END)
        age_entry.insert(0, data[1])

        genre_entry.delete(0, tk.END)
        genre_entry.insert(0, data[2])


window = tk.Tk()
window.title("Song Artist Information")
window.geometry("600x450")

title = tk.Label(window, text="Song Artist Information",
                 font=("Arial", 16))
title.pack(pady=10)

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

tk.Label(window, text="Age").pack()
age_entry = tk.Entry(window, width=30)
age_entry.pack(pady=5)

tk.Label(window, text="Genre").pack()
genre_entry = tk.Entry(window, width=30)
genre_entry.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=10,
          command=add).grid(row=0, column=0, padx=3)

tk.Button(button_frame, text="Update", width=10,
          command=update).grid(row=0, column=1, padx=3)

tk.Button(button_frame, text="Delete", width=10,
          command=delete).grid(row=0, column=2, padx=3)

tk.Button(button_frame, text="Clear", width=10,
          command=clear).grid(row=0, column=3, padx=3)

tk.Button(button_frame, text="Exit", width=10,
          command=exit).grid(row=0, column=4, padx=3)

message = tk.Label(window, text="")
message.pack()

table = ttk.Treeview(
    window,
    columns=("Name", "Age", "Genre"),
    show="headings"
)

table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Genre", text="Genre")

table.column("Name", width=200)
table.column("Age", width=100)
table.column("Genre", width=150)

table.pack(pady=10)

table.bind("<ButtonRelease-1>", click)

window.mainloop()

