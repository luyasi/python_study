import os

Python_path = "D:/python学习/代码"


def Getfile(Python_path):
    Find_path = os.listdir(Python_path)
    # 拼接文件
    for Path in Find_path:
        Pyfile_path = os.path.join(Python_path, Path)
        if os.path.isfile(Pyfile_path) and Pyfile_path.endswith(".py"):
            print(Pyfile_path)
        elif os.path.isfile(Pyfile_path) and not Pyfile_path.endswith(".py"):
            pass
        else:
            Getfile(Pyfile_path)


Getfile(Python_path)
