import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("Tkinter")  # 设置窗口标题

window.geometry("500x500+500+40")  # 设置主窗口大小和屏幕边距
e = tkinter.Variable
entry = tkinter.Entry(window, textvariable=e)


# print(e)

def func_read():
    with open("e", "a+") as f:
        content = f.read()
        return content


def func_write():
    with open("e", "a+") as f:
        content = f.write()
        f.flush()


button1 = tkinter.Button(window, text="读取", command=func_read)
button2 = tkinter.Button(window, text="写入", command=func_write)

text = tkinter.Text(window, width=100, height=20)
str = func_read()
text.insert(tkinter.INSERT, str)

button1.pack()
button2.pack()
entry.pack()
text.pack()

window.mainloop()
