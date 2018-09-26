import tkinter

win = tkinter.Tk()

win.title = ("button")

win.geometry("500x500+500+40")

button1 = tkinter.Button(win,
                         text="quit",  # button上显示的文本
                         width=10,
                         height=1,  # button的大小
                         command=win.quit)  # button按钮的链接功能
button1.pack()


def print_func():
    print("hello someone!")


button2 = tkinter.Button(win,
                         text="print",
                         width=10,
                         height=1,
                         command=print_func)
button2.pack()

win.mainloop()
