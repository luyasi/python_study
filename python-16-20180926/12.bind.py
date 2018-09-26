import tkinter

win = tkinter.Tk()

win.title("bind")
win.geometry("400x400+400+40")


def func(event):
    print(event.x, event.y)


button = tkinter.Button(win, text="按钮", width=30, height=10)

button.bind("<Button-1>", func)

button.pack()

win.mainloop()
