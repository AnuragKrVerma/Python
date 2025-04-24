from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width="500",height="300")
window.config(padx=20,pady=20)

# label
my_label = Label(text="I am a lable", font=("Arial", 24,"bold"))
my_label.place(x=100,y=200)

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    new_text = input_text.get()
    my_label.config(text=new_text)

# label  
button = Button(text="Click", command=button_clicked)
button.grid(column=2,row=2)

# Entry
input_text = Entry(width=10)
input_text.grid(column=3,row=3)


window.mainloop()