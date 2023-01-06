import tkinter as tk
import numpy as np

fenetre=tk.Tk()

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

def detect(X):
    for i in range(3):
        if X[i][0]==X[i][1] and X[i][1]==X[i][2] and X[i][0]!=0:
            return X[i][0]
    for j in range(3):
        if X[0][j]==X[1][j] and X[1][j]==X[2][j] and X[0][j]!=0:
            return X[0][j]
    if X[0][0]==X[1][1] and X[1][1]==X[2][2] and X[0][0]!=0:
        return X[0][0]
    if X[0][2]==X[1][1] and X[1][1]==X[2][0] and X[0][2]!=0:
        return X[0][2]
    return 0

def clic(event):
    global player
    global table
    x=int(int(event.x)//l)
    y=int(int(event.y)//l)
    if table[x][y]==0:
        table[x][y]=player
        player=-player
        draw(table)
        winner = detect(table)
        if winner !=0:
            table = np.zeros((n,n))
            Canvas.delete("all")
            Canvas.create_text(300, 300, text=f"The winner is player {'X' if winner==1 else 'O'} !", fill="black")
            button = tk.Button(Canvas,text="reset",command = reset())
            button.pack()

def reset():
    print(1)
    Canvas.delete("all")
    table = np.zeros((n,n))
    draw(table)

draw(table)
Canvas.bind("<Button-1>",clic)
Canvas.pack()
fenetre.mainloop()