import csv
from tkinter import *
from tkinter import messagebox
import subprocess
root = Tk()
root.title("Inscription")
root.geometry("1600x1280")

image = PhotoImage(file="400381301_122094504986114309_337.png")
label_image = Label(root, image=image)
label_image.place(x=500,y=50,width=1056)
frame1 = Frame(root, width=400, height=400, bg="white")
frame1.place(relx=0.07, rely=0.24)
Label(frame1, text="Nom utilisateur :",font=("verdana",23),bg="white").place(relx=0.25,rely=0.045)
username_entry = Entry(frame1)
username_entry.place(relx=0.23,rely=0.23)


Label(frame1, text="Mot de passe :",font=("verdana",23),bg="white").place(relx=0.26,rely=0.4)
password_entry = Entry(frame1, show="*")
password_entry.place(relx=0.23,rely=0.6)

bt1= Button(frame1, text="creer compte",height=3,command=lambda: ajouter())
bt1.place(relx=0.23,rely=0.8)
bt2 = Button(frame1, text="connexion", height=3,command=lambda: vers_page_conex())
bt2.place(relx=0.488,rely=0.8)

def ajouter():
  if username_entry.get() == "" and password_entry.get() == "":
    messagebox.showerror("important","vous devez remplir les cases")
  else:
    with open("ajout_informationlogin.csv","r") as fich:
      liste_log = list(csv.reader(fich))
    for element in liste_log:
      if username_entry.get() == element[0] and password_entry.get() == element[1]:
        messagebox.showerror("error","ce nom d utilisateur ou bien ce mot de passe sont deja existe")
      elif username_entry.get() == element[0] :
        messagebox.showerror("error", "ce nom existe deja")
      elif password_entry.get() == element[1] :
        messagebox.showerror("error","ce mot de passe existe deja")
    with open("ajout_informationlogin.csv", "a",newline="") as fichier_csv:
      reader = csv.writer(fichier_csv)
      reader.writerow([username_entry.get(),password_entry.get()])
      messagebox.showinfo("important", "vous avez crrer compte avec succes")

def vers_page_conex():
  root.destroy()
  subprocess.Popen(["python", "pagelogin.py"])
root.mainloop()