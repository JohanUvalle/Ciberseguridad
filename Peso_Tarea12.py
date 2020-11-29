import tkinter



ventana= tkinter.Tk()
ventana.geometry("400x420")

LblPeso=tkinter.Label(ventana)
LblPeso.pack()
LblPeso["text"]=("Ingresa tu peso")

cajaTexto=tkinter.Entry(ventana)
cajaTexto.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack()

def Tierra():
  masa =cajaTexto.get()
  if masa=="":
    masa= 0
  peso = (int(masa)*9.8)
  etiqueta["text"] ="Tu peso en 'Newtons' en el planeta Tierra es " + str(peso) + "kg/ms^2"

def Mercurio():
  masa = (cajaTexto.get())
  if masa=="":
    masa= 0
  peso = (int(masa)*3.7)
  etiqueta["text"] ="Tu peso en 'Newtons' en el planeta Mercurio es " + str(peso) + "kg/ms^2"

def Venus():
  masa = (cajaTexto.get())
  if masa=="":
    masa= 0
  peso = (int(masa)*8.87)
  etiqueta["text"] ="Tu peso en 'Newtons' en el planeta Venus es " + str(peso) + "kg/ms^2"

def Marte():
  masa = (cajaTexto.get())
  if masa=="":
    masa= 0
  peso = (int(masa)*3.71)
  etiqueta["text"] ="Tu peso en 'Newtons' en el planeta Marte es de " + str(peso) + "kg/ms^2"

def Jupiter():
  masa = (cajaTexto.get())
  if masa=="":
    masa= 0
  peso = (int(masa)*24.79)
  etiqueta["text"] ="Tu peso en 'Newtons' en el planeta Jupiter es " + str(peso) + "kg/ms^2"

def Saturno():
  masa = (cajaTexto.get())
  if masa=="":
    masa= 0
  peso = (int(masa)*10.44)
  etiqueta["text"] ="Tu peso en 'Newtons' en el planeta Saturno es " + str(peso) + "kg/ms^2"

LblPlaneta=tkinter.Label(ventana)
LblPlaneta.pack()
LblPlaneta["text"]=("Seleccione al planeta de su interes")

boton1 = tkinter.Button(ventana, text = "Tierra", command = Tierra)
boton1.pack()

bntMercurio = tkinter.Button(ventana, text = "Mercurio", command=Mercurio, activeforeground="#fff", activebackground= "#000")
bntMercurio.pack()

bntVenus = tkinter.Button(ventana, text = "Venus", command=Venus)
bntVenus.pack()

bntMarte = tkinter.Button(ventana, text = "Marte", command=Marte)
bntMarte.pack()


btnJupiter = tkinter.Button(ventana, text = "Jupiter", command = Jupiter)
btnJupiter.pack()

bntSaturno = tkinter.Button(ventana, text = "Saturno", command=Saturno)
bntSaturno.pack()



ventana.mainloop()


