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

def detect(t):
    for i in range(3):
        if t[i][0]==t[i][1] and t[i][1]==t[i][2] and t[i][0]!=0:
            return t[i][0]
    for j in range(3):
        if t[0][j]==t[1][j] and t[1][j]==t[2][j] and t[0][j]!=0:
            return t[0][j]
    if t[0][0]==t[1][1] and t[1][1]==t[2][2] and t[0][0]!=0:
        return t[0][0]
    if t[0][2]==t[1][1] and t[1][1]==t[2][0] and t[0][2]!=0:
        return t[0][2]
    return 0

def clic(event):
    global player
    global table
    x=int(int(event.x)//l)
    y=int(int(event.y)//l)
    if x<=2 and x>=0 and y<=2 and y>=0 and table[x][y]==0:
        table[x][y]=player
        player=-player
        draw(table)
        winner = detect(table)
        if winner !=0:
            table = np.zeros((n,n))
            Canvas.delete("all")
            Canvas.create_text(300, 300, text=f"The winner is player {'X' if winner==1 else 'O'} !", fill="black",font=('Helvetica 30 bold'))


def reset():
    Canvas.delete("all")
    table = np.zeros((n,n))
    draw(table)

draw(table)

button = tk.Button(fenetre,text="reset",command=reset)
button.pack()

exit_button = tk.Button(fenetre,text='Exit',command=lambda: fenetre.quit())
exit_button.pack()

Canvas.bind("<Button-1>",clic)
Canvas.pack()
fenetre.mainloop()