from tkinter import *

# initialise a new instance of the tkinter class
print("hello")
window = Tk()

# set the title of the GUI/Interface
window.title("My first GUI program")

# function to specify size of the windowsize
window.minsize(width=500,height=300)

# Label
myLabel = Label(text="This is a Label")

myLabel.config(text="Newtext")

myLabel.pack()
# button has been clicked
def buttton_clicked():
	print("I got clicked")
	myLabel["text"] = input.get()

button = Button(text="click",command=buttton_clicked)

button.pack()

# How to get the input ?
input = Entry()
input.pack()

















window.mainloop()