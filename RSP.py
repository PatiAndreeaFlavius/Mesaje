from tkinter import *
#main fereastra
root= Tk()
root.title("Rock Scissors Paper")                                   #titlu fereastra
root.configure(background= "purple")

#etichetele
user_indicator = Label(root, font=50, text ="EU",bg="purple", fg="white")
computer_indicator = Label(root, font=50, text="COMPUTER",bg="purple", fg="white")
user_indicator.grid(row=0 , column=3 )
computer_indicator.grid(row=0 , column=1 )

#####pt sccor
jucatorScor = Label(root,text =0, font =100,bg="purple", fg="white")
computerScor = Label(root, text=0,font =100,bg="purple", fg="white" )
computerScor.grid(row=1,column=1)
jucatorScor.grid(row=1,column=3)
#mesajele
mesaje = Label(root,font =50, bg="purple", fg="white")                     #, text = "Ai pierdut!")
mesaje.grid(row=3, column=2)

#actualizarea mesajului
def actualiz_Mesaj(x):
    mesaje ['text'] = x

#actualizarea scorului meu

def actualiz_Iscor():                                                       #scorul jucatorului
     scor = int(jucatorScor["text"])
     scor = scor+ 1
     jucatorScor["text"] = str(scor)


root.mainloop()