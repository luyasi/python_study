import tkinter

win = tkinter.Tk()

win.title("place")
win.geometry("400x400+400+40")

label1 = tkinter.Label(win, text="hon", bg="red")
label2 = tkinter.Label(win, text="lv", bg="green")
label3 = tkinter.Label(win, text="huang", bg="yellow")
button1 = tkinter.Button(win, text="按钮")
label1.place(x=10, y=10)
label2.place(x=50, y=10)
label3.place(x=100, y=10)
button1.place(x=200, y=40)

win.mainloop()
