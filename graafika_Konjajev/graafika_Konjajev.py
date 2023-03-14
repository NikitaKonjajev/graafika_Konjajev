from tkinter import *
k=0
def klikker():
    global k
    k+=1
    nupp.configure(text=k)
    if k%2:
        raam.itemconfigure(pildid,image=pilt)
    else:
        raam.itemconfigure(pildid,image=pilt2)
def text_to_lbl(event):
     text=tekst_kast.get()
     pealkiri.configure(text=text)
     tekst_kast.delete(0,END)
tekst="Aken"
aken=Tk()
aken.geometry("700x700")
aken.title(tekst)
aken.iconbitmap("unnamed.ico")

pealkiri=Label(aken,
               text="Tkinter põhi elemendid",
               bg="yellow",
               fg="#0d010b",
               font="Chiller 20",
               height=3,
               width=25)
nupp=Button(aken, 
            text="Vajuta mind",
            bg="purple",
            fg="#0d010b",
            font="Chiller 20",
            activebackground="red",
            activeforeground="white",
            height=3,
            width=20,
            command=klikker)
raam=Canvas(aken,
            width=600,
            height=600)
    #        bg="black",)
pilt=PhotoImage(file="pilt1.png")
pilt2=PhotoImage(file="pilt2.png")
pildid=raam.create_image(2,2,image=pilt,anchor=NW)
tekst_kast=Entry(aken,
                 fg="Lightblue",
                 bg="grey",
                 font="Chiller 20",
                 width=20,
                 justify=CENTER)
tekst_kast.bind("<Return>",text_to_lbl)

pealkiri.pack()
tekst_kast.pack()#side=LEFT,RIGHT
nupp.pack()
raam.pack()
aken.mainloop()
