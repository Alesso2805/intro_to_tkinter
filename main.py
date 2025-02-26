import tkinter
import turtle

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

tim = turtle.Turtle()
tim.write("I am a Turtle", font=("Arial", 24, "bold"))

while True:
    window.mainloop()
