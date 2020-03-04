from tkinter import *
import time
myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=600, background="sky blue")
screen.pack()


rocketx1= 0
rockety1 = 250

rocketx2 = 300
rockety2 = 350


xNose = rocketx2 + 60
yNose = (rockety1 + rockety2)/2

textx = (rocketx1 + rocketx2)/2
texty = (rockety2 + rockety1)/2




while True:
    while rocketx1 < 1000:
        rocketx1 += 5
        rocketx2 += 5
        xNose = rocketx2 + 60
        yNose = (rockety1 + rockety2)/2
        textx = (rocketx1 + rocketx2)/2
        texty = (rockety2 + rockety1)/2

        body = screen.create_rectangle(rocketx1, rockety1, rocketx2, rockety2, fill="blue")
        head = screen.create_polygon(rocketx2, rockety1, rocketx2, rockety2, xNose,yNose, fill="red")
        text = screen.create_text(textx, texty, text="Daniel Yu", fill="white", font="30")
        flame = screen.create_polygon(rocketx1, rockety1, rocketx1, rockety2, rocketx1- 100, rockety2, rocketx1-70, rockety2 - 30, rocketx1 - 90, rockety2 - 50, rocketx1, rockety1 , fill="orange")
        screen.update()
        time.sleep(0.03)
        screen.delete(body, head, text, flame)

    time.sleep(0.1)

    while rocketx2 > 0:
        rocketx1 -= 5
        rocketx2 -= 5
        xNose = rocketx1 - 60
        yNose = (rockety1 + rockety2)/2
        textx = (rocketx1 + rocketx2)/2
        texty = (rockety2 + rockety1)/2

        body = screen.create_rectangle(rocketx1, rockety1, rocketx2, rockety2, fill="blue")
        head = screen.create_polygon(rocketx1, rockety1, rocketx1, rockety2, xNose,yNose, fill="red")
        text = screen.create_text(textx, texty, text="Daniel Yu", fill="white", font="30")
        flame = screen.create_polygon(rocketx2, rockety1, rocketx2, rockety2, rocketx2 + 100, rockety2, rocketx2 + 70, rockety2 - 30, rocketx2 + 90, rockety2 - 50, rocketx2, rockety1 , fill="orange")

        screen.update()
        time.sleep(0.03)
        screen.delete(body, head, text, flame)
    
    time.sleep(0.1)



screen.mainloop()