from tkinter import *

raiz=Tk()
raiz.geometry("310x350")
raiz.title('Paleta de colores')
raiz.resizable(0,0)

raiz.config(background='#467fb1')

rojo="00"
verde="00"
azul="00"
mezcla="#0000"
def modificRojo(valor):
	global rojo
	valor="%x" %int(valor)
	if len(valor)<2:
		valor='0'+valor
	rojo=valor
	pintar()

def modificVerde(valor):
	global verde
	valor="%x" %int(valor)
	if len(valor)<2:
		valor='0'+valor
	verde=valor
	pintar()

def modificAzul(valor):
	global azul
	valor="%x" %int(valor)
	if len(valor)<2:
		valor='0'+valor
	azul=valor
	pintar()

def pintar():
	global mezcla
	mezcla='#'+rojo+verde+azul
	fuenteR="%x" %int(255-r.get())
	if len(fuenteR)<2:
		fuenteR='0'+fuenteR
	fuenteG="%x" %int(255-g.get())
	if len(fuenteG)<2:
		fuenteG='0'+fuenteG
	fuenteB="%x" %int(255-b.get())
	if len(fuenteB)<2:
		fuenteB='0'+fuenteB
	fuente='#'+fuenteR+fuenteG+fuenteB
	
	valor.config(text="Copiar código\n"+mezcla,bg=mezcla,fg=fuente)

def copiar():
	raiz.clipboard_clear()
	raiz.clipboard_append(mezcla)

r=Scale(raiz,from_=0,to=255,orient='horizontal',activebackground="Red",command=modificRojo)
r.grid(row=0,column=0,padx=5,pady=5,sticky='we')
g=Scale(raiz,from_=0,to=255,orient='horizontal',activebackground="Green",command=modificVerde)
g.grid(row=1,column=0,padx=5,pady=5,sticky='we')
b=Scale(raiz,from_=0,to=255,orient='horizontal',activebackground="Blue",command=modificAzul)
b.grid(row=2,column=0,padx=5,pady=5,sticky='we')
valor=Button(raiz,text="Copiar código\n"+mezcla,font=('Arial Black',20),width=15,command=copiar)
valor.config(fg="white",bg='black',relief='sunken',height=4)
valor.grid(row=3,column=0,padx=5,pady=5)

raiz.mainloop()