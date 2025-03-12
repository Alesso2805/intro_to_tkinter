import tkinter
from tkinter import Entry

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button = tkinter.Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

button = tkinter.Button(text="Button", command=button_clicked)
button.grid(column=2, row=0)

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=4)




while True:
    window.mainloop()
