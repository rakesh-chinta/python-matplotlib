from tkinter import*
import time
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
canvas.create_polygon(10,10,10,50,40,30)
for i in range(0,60):
    canvas.move(1,5,5)
    root.update()
    time.sleep(0.1)


root.mainloop()    
