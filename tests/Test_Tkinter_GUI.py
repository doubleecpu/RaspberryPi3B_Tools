from tkinter import*

master=Tk()
hsize = 1920
vsize = 720
master.geometry(str(hsize) + "x" + str(vsize))

frame1=Frame(master, width=(hsize*.5), height=(vsize*.5), background="Blue")
frame1.grid(row=0, column=0)

frame2=Frame(master, width=(hsize*.5), height=(vsize*.5), background="Red")
frame2.grid(row=1, column=0)

frame3=Frame(master,  width=(hsize*.5), height=(vsize*.5), background="Green")
frame3.grid(row=0, column=1)

frame4=Frame(master, width=(hsize*.5), height=(vsize*.5), background="Yellow")
frame4.grid(row=1, column=1)

master.mainloop()
