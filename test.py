from tkinter import*
root = Tk()
root.geometry('300x300')
root.title('Aplikasi Deteksi Buku')
text1 = Label ( root, text = ' Tugas Besar Computer Vision A  ')
text1.pack()

photo = PhotoImage(file='1.png')
labelphoto = Label(root, image = photo)
labelphoto.pack()

topframe = Frame (root)
topframe.pack()
bottomframe = Frame (root)
bottomframe.pack(side = BOTTOM)

button1 = Button(topframe, text =" Take Foto",  fg = "black")
button2 = Button(topframe, text =" Keterangan ",  fg = "black")
button3 = Button(topframe, text =" Nama Kelompok ",  fg = "red")

button1.pack()
button2.pack()
button3.pack()

text2 = Label ( root, text = ' #COMVIS7 ')
text2.pack()

rooot.mainloop()
