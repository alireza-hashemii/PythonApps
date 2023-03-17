from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Python Music Player")

textlabel = Label(window,text="This is a play Button")
textlabel.pack()

def something():
    print("i am being clicked")

photo = PhotoImage(file='file.png')
Play_Button = Button(window,image=photo,command=something)
Play_Button.pack()
window.mainloop()