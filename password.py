from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle



def generate_password(password_entry):
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

def save(website_entry, email_entry, password_entry):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0 or not "@" in email:
        messagebox.showinfo(title="Oops", message="Something is wrong with your entry")
    else:
            
        isok = messagebox.askokcancel(title="Confirm details", message=f"Website: {website} \nEmail: {email} \npassword: {password} \nProceed and save?")
        if isok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website}  |  {email}  |  {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    
            showpass()
                

def showpass():
    from main import showpassword
    showpassword()





# window design
def password_manager():
    window = Tk()

    window.config(padx=50, pady=50,bg="white")
    window.title("Password Manager")
    window.minsize(width=500, height=300)

    canvas = Canvas(height=200, width=200,bg="white")
    imag = PhotoImage(file="logo.png")
    canvas.create_image(100,100,image=imag)
    canvas.grid(row=0, column=1,pady=10)


    #labels
    website_label = Label(text="Website : ",bg="white")
    website_label.grid(row=1,column=0)
    email_label= Label(text="Email/Username : ",bg="white")
    email_label.grid(row=2,column=0)
    password_label=Label(text="Password : ",bg="white")
    password_label.grid(row=3,column=0)

    #Entries

    website_entry = Entry(width=56)
    website_entry.grid(row=1,column=1,columnspan=2,pady=4)
    website_entry.focus()
    email_entry=Entry(width=56)
    email_entry.grid(row=2,column=1,columnspan=2,pady=4)
    email_entry.insert(0, "mohitsaini@gmail.com")
    password_entry = Entry(width=37)
    password_entry.grid(row=3,column=1,pady=4)

    #Buttons
    generate_passwordd = Button(text="Generate Password",bg="lavender",activebackground="sky blue",command=lambda : generate_password(password_entry))
    generate_passwordd.grid(row=3,column=2,pady=4)
    add_button = Button(text="Add Password",width=47,bg="lavender",activebackground="sky blue", command=lambda : save(website_entry,email_entry,password_entry))
    add_button.grid(row=4,column=1,columnspan=2,pady=10)

    #window.grid_rowconfigure(2,minsize=10)
    generatelist = Button(text = "Saved Passwords", bg="sky blue", activebackground="lavender",command=showpass)
    generatelist.grid(row=5,column=1,pady=10)

    window.mainloop()

password_manager()
    