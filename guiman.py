from tkinter import*
from tkinter.ttk import *

dire=''

def gu(L):

    def upd():

        global dire

        dire='u'

    def downd():

        global dire

        dire='d'

    def leftd():

        global dire

        dire='l'

    def rightd():

        global dire

        dire='r'

    root=Tk()

    #Various images being assigned to variables.

    wall= PhotoImage(file= r"wall.png")

    tile= PhotoImage(file= r"tile.png")

    rat= PhotoImage(file= r"rat.png")

    cheese= PhotoImage(file= r"cheese.png")

    up= PhotoImage(file= r"up.png")

    down= PhotoImage(file= r"down.png")

    left= PhotoImage(file= r"left.png")

    right= PhotoImage(file= r"right.png")

    inde=-1

    ind2=-1

    for i,j in enumerate (L):

        ind2+=1

        for k in j:

            inde=inde+1

            if k==0:
                 Button(root,text ='Click Me!', image=wall).grid(row=ind2,column=inde)

            if k==1:
                 Button(root,text='Click Me!', image=tile).grid(row=ind2,column=inde)

            if k==2:
                Button(root,text='Click Me!', image=rat).grid(row=ind2,column=inde)

            if k==4:
                Button(root,text='Click Me!', image=cheese).grid(row=ind2,column=inde)

        inde=-1

    Button(root,text='left', image=left,command = lambda: [leftd(),root.destroy()]).grid(row=11,column=12)

    Button(root,text='Up', image=up,command = lambda: [upd(),root.destroy()]).grid(row=10,column=13)

    Button(root,text='right', image=right,command = lambda: [rightd(),root.destroy()]).grid(row=11,column=14)

    Button(root,text='down', image=down,command = lambda: [downd(),root.destroy()]).grid(row=11,column=13)

    mainloop()

    #We return dire so that we can see which direction the user wishes to move in.

    return dire
