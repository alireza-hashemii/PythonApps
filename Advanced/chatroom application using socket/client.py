import socket
import tkinter
from tkinter import *
import threading


def receive():
    while True:
        try:
            msg= sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END,msg)
        except:
            print("There is an unexpected Error occured")

def send():
    msg = my_msg.get()
    my_msg.set("")
    sock.send(bytes(msg,"utf8"))
    if msg=="#quit":
        sock.close()
        window.close()

def on_closing():
    my_msg.set("#quit")
    send()


window = Tk()
window.title("Chatroom application")
window.configure(bg="green")
message_frame = Frame(window,height=100,width=100,bg="red")
message_frame.pack()
my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame,height=15,width=100,bg="red",yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT,fill=Y)
msg_list.pack(side=LEFT,fill=BOTH)
msg_list.pack()

label = Label(window,text="Enter your message",fg="blue",font="Aeria",bg="red")
label.pack()
entry_field = Entry(window,textvariable=my_msg,fg="red",width=50)
entry_field.pack()

send_Button = Button(window,text="send",font="Aerial",fg="white",command=send) 
send_Button.pack()

quit_Button = Button(window,text="Quit",font="Aerial",fg="white",command=on_closing)
quit_Button.pack()


host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))

receive_Thread = threading.Thread(target=receive)
receive_Thread.start()



mainloop()