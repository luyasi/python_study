import tkinter

win = tkinter.Tk()

win.title("entry")

win.geometry("500x500+500+40")
var = tkinter.Variable()
entry = tkinter.Entry(win, show="*", textvariable=var)
entry.pack()


def print_func():
    print(var.get())


button = tkinter.Button(win, text="打印", command=print_func)
button.pack()

win.mainloop()
