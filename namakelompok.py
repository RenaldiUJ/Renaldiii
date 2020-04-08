from tkinter import*
root = Tk()
root.geometry('300x300')
root.title('Nama Kelompok Comvis 7')
text1 = Label ( root, text = ' Dony Tontiardo ( 1103171215 )')
text2 = Label ( root, text = ' Faiz Adil Khatami ( 1103161154 ) ')
text3 = Label ( root, text = ' Gilang')
text4 = Label ( root, text = ' Oshi Paulina Sancho L ( 1103164009) ')
text5 = Label ( root, text = ' Renaldi Utama Jaya( 1103160112 ) ')
text1.pack()
text2.pack()
text3.pack()
text4.pack()
text5.pack()

topframe = Frame (root)
topframe.pack()
bottomframe = Frame (root)
bottomframe.pack(side = BOTTOM)

button1 = Button(topframe, text =" Back Home ",  fg = "black")
button1.pack()


rooot.mainloop()
