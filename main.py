from tkinter import *

root = Tk()

root.config(padx=50, pady=50,bg="white")
root.title("Saved Passwords")
#window.minsize(width=500, height=500)

canvas = Canvas(height=200, width=200,bg="white")
imag = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=imag)
canvas.grid(row=0,column=1)

def showpassword():
    i=1
    f = open("data.txt", "r")
    passwor = f.readlines()
    for da in passwor:
        pas = da
        Label(root,text=pas,bg="white").grid(row=i,column=1)
        i=i+1
    f.close()

showpassword()


root.mainloop()

