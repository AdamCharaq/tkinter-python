from tkinter import *
from tkinter import messagebox
import csv
fenetre = Tk()
fenetre.geometry("1600x1200")
fenetre.config(bg="wheat")
#phptofenetre
photo = PhotoImage(file="10370774_0(1).png")
arriereplan = Label(fenetre, image=photo,bg="wheat")
arriereplan.place(rely=0.0, relx=0.4)
mon = PhotoImage(file="one-hundred-dollar-bill-floating.png")
arriereplan1 = Label(fenetre, image=mon,bg="wheat")
arriereplan1.place(x=300,y=0)
riffle = PhotoImage(file="M16-Rifle(1).png")
m_sixteen = Label(fenetre, image=riffle, bg="wheat")
m_sixteen.place(x=1060,y=10)
bullet = PhotoImage(file="long-range-bullet-isolated-white(1).png")
sixteen_bull = Label(fenetre, image=bullet,bg="wheat")
sixteen_bull.place(relx=0.88,rely=0.02)
# Partie haute avec pack()
lb1 = Label(fenetre, text="Tu ne tires pas… mais tu paies pour chaque tir", font=("Anton", 30), fg="red",bg="wheat")
lb1.place(relx=0.3,rely=0.0)

#zone
zone_gr = Listbox(fenetre,bg="white",font=("courrier",20))
zone_gr.place(relx=0.038, rely=0.714,height=224, width=1200)

# Partie basse avec grid() dans un Frame
frame1 = Frame(fenetre,bg="wheat")
frame1.place(relx=0.0, rely=0.243,width=900)

lb = Label(frame1, text="Entreprise mere", height=2,font=("courrier",20),bg="wheat")
lb.grid(row=0, column=0)
inputo = Entry(frame1,font=("Anton",25))
inputo.grid(row=0, column=1,ipady=5, ipadx=50)
lb2 = Label(frame1, text="Entreprise", font=("courrier",20), pady=20, padx=30,bg="wheat")
lb2.grid(row=1, column=0)
input2 = Entry(frame1, font=("Anton",25))
input2.grid(row=1, column=1,ipady=5, ipadx=50)
image2 = PhotoImage(file="4091968(1).png")
icon2 = Label(frame1, image=image2)
icon2.grid(row=1,column=2, padx=30)
lb3 = Label(frame1, text="R.B",font=("courrier",20),pady=20, padx=30,bg="wheat")
lb3.grid(row=2,column=0)
input3 = Entry(frame1,font=("Anton",25))
input3.grid(row=2, column=1,ipady=5, ipadx=50)
image3 =PhotoImage(file="2gPEsuvM7CKQ9hXIJNKl4v2Gesl-mobi.png")
icon3 = Label(frame1,image=image3)
icon3.grid(row=2,column=2,padx=30)
lb_soustitre = Label(frame1,text="(Raison a boycotter)", font=("courrier",13),bg="wheat")
lb_soustitre.grid(row=3,column=0)
lb4 = Label(frame1,text="P.F", font=("courrier",20),pady=27,bg="wheat")
lb4.grid(row=4,column=0)
input4 = Entry(frame1,font=("Anton",25))
input4.grid(row=4, column=1, ipady=5, ipadx=50)
image4 =PhotoImage(file="pngtree-cartoon-industrial-machi.png")
icon4 = Label(frame1,image=image4)
icon4.grid(row=4,column=2,padx=30)
lb_soustitre1 = Label(frame1,text="(Produit qui fabriaue)", font=("courrier",13),bg="wheat")
lb_soustitre1.grid(row=5,column=0)

input_search = Entry(frame1,bg="white")
input_search.grid(row=6, column=2)
btnsearch = Button(frame1,text="recherche",bg="#4CAF50",command=lambda: recherche())
btnsearch.grid(row=6, column=3)
#button
button_frame = Frame(frame1,bg="wheat")
button_frame.grid(row=6, column=0, columnspan=2)
button_existedeja = Button(button_frame,text="existe deja", width=7, height=2, command=lambda: existe_deja())
button_existedeja.pack(side=LEFT, padx=10)
but1 = Button(button_frame, text="Ajouter", width=7, height=2 , command=lambda: ajouter())
but1.pack(side=LEFT, padx=10)

but2 = Button(button_frame, text="Affiche", width=7, height=2, command=lambda: afficher())
but2.pack(side=LEFT, padx=10)

but3 = Button(button_frame, text="supprimer", width=10, height=2,command=lambda: supprimer())
but3.pack(side=LEFT, padx=10)

but4 = Button(button_frame, text="effacer", width =7, height=2,command=lambda: effacer())
but4.pack(side=LEFT, padx=10)


#fonction_button_ajouter
def ajouter():
    valeur = False
    if input2.get() == "" or input3.get() == "" or input4.get() == "":
      messagebox.showwarning('WARNING','remplis les champs')
    else:
     resulat = input2.get(),input3.get(),input4.get()
     file_csv = open("listeboycott.csv", "a")
     file_csv.write(f"{resulat[0]},{resulat[1]},{resulat[2]}\n")
     file_csv.close()
     for i in range(1):
       input2.delete(0,END)
       input3.delete(0, END)
       input4.delete(0, END)
       inputo.delete(0,END)
     zone_gr.insert(END,f"{resulat[0]},{resulat[1]},{resulat[2]}")
     with open("listeboycott.csv", "r") as fichier_bo:
         lire = list(csv.reader(fichier_bo))
     for element in lire:
         if input2.get() == element[0]:
             valeur = True
             break
     if valeur:
         messagebox.showinfo("important", "cet entreprise est deja dans la liste")
     else:
         messagebox.showinfo("important", "cet emtreprise n est pas la liste de boycott")

def supprimer():
  if zone_gr.size() == 0:
    messagebox.showinfo("important","y a rien pour sypprimer")
  else:
      zone_gr.delete(END, END)

def afficher():
    with open("listeboycott.csv","r") as boycott:
       ligne = list(csv.reader(boycott))
    for element in reversed(ligne):
       zone_gr.insert(END,element)
def effacer():
  if zone_gr.size() == 0:
    messagebox.showinfo("important","y a rien pour sypprimer")
  else:
    zone_gr.delete(0,END)

def recherche():
  with open("listeboycott.csv","r") as fichier_boy:
    lecture = list(csv.reader(fichier_boy))
    for element in lecture:
      if input_search.get() == element[0]:
        zone_gr.insert(END,f"{element[0]},{element[1]},{element[2]}")


fenetre.mainloop()