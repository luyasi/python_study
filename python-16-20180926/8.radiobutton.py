import tkinter

win = tkinter.Tk()
win.title("radiobutton")
win.geometry("400x400+400+40")


def func():
    print(result.get())


result = tkinter.StringVar()
radio1 = tkinter.Radiobutton(win, text="苹果", value="a", variable=result, command=func)
radio1.pack()

radio2 = tkinter.Radiobutton(win, text="梨子", value="b", variable=result, command=func)
radio2.pack()
win.mainloop()
