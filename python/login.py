from tkinter import *

def login():
    input_key=login_key.get()
    if input_key=="22411840":
        login_button.pack_forget()
        login_key.pack_forget()


tk = Tk() 
tk.geometry("400x240")

login_key=Entry(tk,width=10)
login_key.pack()

login_button=Button(tk,text="로그인",command=login)
login_button.pack()

tk.mainloop()