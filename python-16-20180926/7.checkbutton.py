import tkinter

win = tkinter.Tk()

win.title("checkbutton")
win.geometry("400x400+400+40")


def func():
    message = ""
    if result1.get():
        message += "苹果\n"
    if result2.get():
        message += "梨子\n"
    if result3.get():
        message += "桃子\n"
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


result1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="苹果", variable=result1, command=func)
check1.pack()

result2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="梨子", variable=result2, command=func)
check2.pack()

result3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="桃子", variable=result3, command=func)
check3.pack()

text = tkinter.Text(win, width=50, height=10)
text.pack()

win.mainloop()
