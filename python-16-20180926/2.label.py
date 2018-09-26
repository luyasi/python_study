""""""
"""Tkinter label标签"""

import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("Tkinter")  # 设置窗口标题

window.geometry("500x500+500+40")  # 设置主窗口大小和屏幕边距

label = tkinter.Label(window,
                      text="hello python",  # 标签文本内容，一般比较短
                      # bg = "red",   #标签背景颜色
                      fg="blue",  # 标签文本颜色
                      font=("宋体", 20),  # 标签文本字体和大小
                      height=2,  # 标签高度
                      width=15,  # 标签宽度
                      wraplength=100,  # 标签问题多宽之后换行
                      justify="center",  # 标签文本靠中/左/右
                      anchor="nw")  # 标签文本位置
label.pack()
window.mainloop()  # 显示主窗口
