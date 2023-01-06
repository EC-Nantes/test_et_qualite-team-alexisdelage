import tkinter as tk
import numpy as np

fenetre=tk.Tk()

hauteur=600
longueur=600

Canvas=tk.Canvas(fenetre,width=longueur,height=hauteur,bg='white')

n=3
l=hauteur/3

table = np.zeros((n,n))
player = 1

def draw(table):
    for i in range(n):
        for j in range(n):
            if table[i][j]==0:
                Canvas.create_oval(i*l+5,j*l+5,(i+1)*l-5,(j+1)*l-5,fill="white")
            if table[i][j]==1:
                Canvas.create_oval(i*l+6,j*l+6,(i+1)*l-6,(j+1)*l-6,fill="red")
            if table[i][j]==-1:
                Canvas.create_oval(i*l+6,j*l+6,(i+1)*l-6,(j+1)*l-6,fill="yellow")

                                   
def clic(event):
    global player
    global table
    x=int(int(event.x)//l)
    y=int(int(event.y)//l)
    table[x][y]=player
    player=-player
    draw(table)
                                   
draw(table)
Canvas.bind("<Button-1>",clic)
Canvas.pack()
fenetre.mainloop()