import csv
from tkinter import *
from tkinter import messagebox
import subprocess

root = Tk()
root.title("Login Page")
root.geometry("1600x1280")
photo = PhotoImage(file="400381301_122094504986114309_337.png")
label_image = Label(root, image=photo)
label_image.place(relx=0.0, rely=0.13)
frame1 = Frame(root,width=400,height=400,bg="white")
frame1.place(relx=0.7, rely=0.3)
Label(frame1, text="Nom utilisateur :",font=("verdana",23)).place(relx=0.24,rely=0.045)
username_entry = Entry(frame1)
username_entry.place(relx=0.23,rely=0.23)


Label(frame1, text="Mot de passe :",font=("verdana",23)).place(relx=0.26,rely=0.4)
password_entry = Entry(frame1, show="*")
password_entry.place(relx=0.23,rely=0.65)

bt1= Button(frame1, text="Se connecter",height=3,command=lambda: comaprer_existance())
bt1.place(relx=0.24,rely=0.87)
bt2 = Button(frame1, text="Creer compte",height=3, command=lambda: vers_page_creer())
bt2.place(relx=0.48,rely=0.87)
#def ajouter():
#    resultat = (username_entry.get(),password_entry.get())
#    fichier_csv = open("ajout_informationlogin.csv","a")
#    fichier_csv.write(f"{resultat[0]},{resultat[1]}")
#    fichier_csv.close()

def comaprer_existance():
 trouve = False
 with open("ajout_informationlogin.csv","r") as fichier:
    lire = list(csv.reader(fichier))
 for element in lire:
     if username_entry.get() == element[0] and password_entry.get() == element[1]:
         trouve = True
         break

 if trouve:
    root.destroy()
    subprocess.Popen(["python", "projetpoo.py"])
 else:
     messagebox.showerror("Erreur", "Remplir les caes")

def vers_page_creer():
    root.destroy()
    subprocess.Popen(["Python","signup.py"])

root.mainloop()


