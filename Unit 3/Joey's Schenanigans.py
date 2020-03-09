from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=600, height=600, background="sky blue")
screen.pack()


screen.create_oval(100,100,200,200, fill="#674E27", outline="#674E27")
screen.create_oval(200,100,300,200, fill="#674E27", outline="#674E27")
screen.create_rectangle(150,150,250,500, fill="#674E27", outline="#674E27")
screen.create_arc(150,450,250,550, fill="#674E27", outline="pink", extent=180,start=180)

screen.mainloop()