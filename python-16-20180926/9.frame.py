import tkinter

win = tkinter.Tk()

win.title("frame")
win.geometry("400x400+400+40")

frame = tkinter.Frame(win)
frame.pack()

fram1 = tkinter.Frame(frame)
tkinter.Label(fram1, text="标签1", bg="red").pack(side=tkinter.LEFT)
fram1.pack(side=tkinter.LEFT)

fram2 = tkinter.Frame(frame)
tkinter.Button(fram2, text="按钮1", bg="yellow").pack(side=tkinter.BOTTOM)
fram2.pack(side=tkinter.BOTTOM)

win.mainloop()
