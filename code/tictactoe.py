import tkinter as tk
import numpy as np

fenetre=tk.Tk()

size=600
size=600

Canvas=tk.Canvas(fenetre,width=size,height=size,bg='white')

n=3
l=size/3

table = np.zeros((n,n))
player = 1

def draw(table):
    for i in range(n-1):
        Canvas.create_line((i+1)*l,0,(i+1)*l,size*l)
        Canvas.create_line(0,(i+1)*l,size*l,(i+1)*l)
    for i in range(n):
        for j in range(n):
            if table[i][j]==1:
                Canvas.create_line(l*i+30,l*j+30,l*i+170,l*j+170)
                Canvas.create_line(l*i+170,l*j+30,l*i+30,l*j+170)
            if table[i][j]==-1:
                Canvas.create_oval(i*l+6,j*l+6,(i+1)*l-6,(j+1)*l-6,fill="white")

                                   
def clic(event):
    global player
    global table
    x=int(int(event.x)//l)
    y=int(int(event.y)//l)
    if table[x][y]==0:
        table[x][y]=player
        player=-player
        draw(table)
                                   
draw(table)
Canvas.bind("<Button-1>",clic)
Canvas.pack()
fenetre.mainloop()