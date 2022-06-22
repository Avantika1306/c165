from tkinter import *
from tkinter import ttk 
from  PIL import ImageTk,Image
root=Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="Orchid1")
labelplanet=Label(root,text="Planet:",bg="Orchid2")
labelplanet.place(relx=0.2,rely=0.1,anchor=CENTER)
labelplanetname=Label(root,font=("courier",18,"bold"),bg="Orchid3")
labelplanetname.place(relx=0.5,rely=0.25,anchor=CENTER)
labelplanetimage=Label(root,bg="gold",highlightthickness=5,borderwidth=2,relief=SOLID)
labelplanetimage.place(relx=0.5,rely=0.5,anchor=CENTER)
labelgravityradius=Label(root,font=("Casttellar",18,"bold"))
labelgravityradius.place(relx=0.5,rely=0.8,anchor=CENTER)
labelinfo=Label(root,bg="Orchid4",wraplength="500")
labelinfo.place(relx=0.5,rely=0.9,anchor=CENTER) 
listplanets=["venus","earth"]
selectedval=StringVar()
dropdown=ttk.Combobox(root,values=listplanets,textvariable=selectedval)
dropdown.place(relx=0.5,rely=0.1,anchor=CENTER)
venus=ImageTk.PhotoImage(Image.open("venus.jpg"))
earth=ImageTk.PhotoImage(Image.open("earth.jpg"))
def showPlanetinfo():
    planet=selectedval.get()
    if planet == "venus":
        labelplanetname["text"]="venus"
        labelplanetimage["image"]=venus
        labelgravityradius["text"]="gravity:8.87m/s^2\nradius=6051.8km"
        labelinfo["text"]="Venus is the second planet from the Sun and is named after the Roman goddess of love and beauty. As the brightest natural object in Earth's night sky after the Moon, Venus can cast shadows and can be visible to the naked eye in broad daylight"
  
    elif planet == "earth":
        labelplanetname["text"]="earth"
        labelplanetimage["image"]=earth
        labelgravityradius["text"]="gravity:9.8m/s^2\nradius=6371km"
        labelinfo["text"]="Earth is the third planet from the Sun and the only astronomical object known to harbor life. While large volumes of water can be found throughout the Solar System, only Earth sustains liquid surface water. About 71% of Earth's surface is made up of the ocean, dwarfing Earth's polar ice, lakes, and rivers. "
    
    
button1=Button(root,text="Show Planet Info",command=showPlanetinfo)
button1.place(relx=0.5,rely=0.18,anchor=CENTER)


root.mainloop()