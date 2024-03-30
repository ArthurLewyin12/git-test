import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
 
 
app = customtkinter.CTk()
app.geometry("600x440")
app.title("Login")


"""
def first_fonction():
    app.destroy()
    self=customtkinter.CTk()
    self.geometry('1000x1200')
    self.title("LOG ON")
    text1=customtkinter.CTkLabel(master=self,text='votre connexion a reussi.',font=('Arial',79,'bold'))
    text1.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    
    self.mainloop()
"""

def connect():
    Username=entry1.get()
    Password=entry2.get()

    if Username == 'Admin' and Password =='my_password' :
        scren=customtkinter.CTkToplevel(app)
        scren.geometry("1000x1200")
        scren.title("Log on")
        
        text2=customtkinter.CTkLabel(master=scren,text='Votre connexion a reussi ',font=("Arial",80,"bold"))
        text2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        
        scren.mainloop()
    
    elif Username !='Admin' and Password == 'my_password' :
        messagebox.showerror("Invalide","Nom d'utilisateur invalide")
    
    elif Username == 'admin' and Password != 'my_password' :
        messagebox.showerror("Invalide","Mot de passe invalide")
    
    elif Username != 'admin' and Password != 'my_password' :
        messagebox.showerror("Invalide","nom d'utilisateur et mot de passe incorrect")
        

img1=ImageTk.PhotoImage(Image.open("Hacker.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()


my_frame=customtkinter.CTkFrame(master=l1,width=320,height=360,border_width=2,corner_radius=15)
my_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=my_frame,text="Log into your account",font=("Century Gothic",20,"bold"))
l2.place(x=50,y=45)

entry1=customtkinter.CTkEntry(master=my_frame,width=220,placeholder_text="Username")
entry1.place(x=50,y=110)

entry2=customtkinter.CTkEntry(master=my_frame,width=220,placeholder_text="Password")
entry2.place(x=50,y=165)



l3=customtkinter.CTkLabel(master=my_frame,text="Forgot your password?",font=("Century Gothic",12))
l3.place(x=90,y=255)

button1=customtkinter.CTkButton(master=my_frame,cursor='hand2',command=connect,width=220,text='login',corner_radius=6)
button1.place(x=50,y=220)

img2=customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20,20)))
img3=customtkinter.CTkImage(Image.open("124010.png").resize((20,20)))

button2=customtkinter.CTkButton(master=my_frame,image=img2,width=100,height=20,cursor='hand2',text='Google',corner_radius=2,compound="left",text_color='black',fg_color='white',hover_color="#A4A4A4")
button2.place(x=50,y=290)


button3=customtkinter.CTkButton(master=my_frame,image=img3,width=100,height=20,cursor='hand2',text='Facebook',corner_radius=2,compound="left",text_color='black',fg_color="white",hover_color="#A4A4A4")
button3.place(x=170,y=290)





app.mainloop()
