import tkinter

win = tkinter.Tk()
win.title("text")
win.geometry("500x500+500+40")

text = tkinter.Text(win,
                    width=50,
                    height=20)

text_value = "被伤过的心还可以爱谁？"
text.insert(tkinter.INSERT, text_value)
text.pack()


def print_func():
    print(text.get(0.0, tkinter.END))


button = tkinter.Button(win, text="print", command=print_func)
button.pack()
win.mainloop()
