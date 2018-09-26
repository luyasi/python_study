import tkinter

win = tkinter.Tk()

win.title("grid")
win.geometry("400x400+400+40")

label1 = tkinter.Label(win, text="红", bg="red")
label2 = tkinter.Label(win, text="粉", bg="pink")
label3 = tkinter.Label(win, text="紫", bg="purple")
label4 = tkinter.Label(win, text="黄", bg="yellow")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=40, column=30)
label4.grid(row=40, column=40)

win.mainloop()
