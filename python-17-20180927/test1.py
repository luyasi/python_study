# import socket
#
# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# sends = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:hello"
#
# sock.sendto(sends.encode("gbk"),("171.0.0.1",2425))
#
# sock.close()

""""""
"""
多任务：计算机同时执行多个任务

单核cpu多任务：程序轮训执行
多核cpu多任务：程序同时执行

实现多任务的方式：
1.多进程方式
2.多线程方式
3.协程方式
4.多进程+多线程
"""

"""不带多进程的程序"""
# import time
#
# def func():
#     while True:
#         print("程序2")
#         time.sleep(2)
#
# if __name__ == '__main__':
#     while True:
#         print("程序1")
#         time.sleep(1)
#         func()

"""多进程优化"""
import time
import os
from multiprocessing import Process

# def func():
#     print("我启动了...")
#
# def foo(str1):
#     # p1 = Process(target=func)
#     # p1.start()
#     while True:
#         print("this is process2-%s-%s-%s"%(os.getpid(),os.getppid(),str1))
#         time.sleep(1.5)
# if __name__ == '__main__':
#     print("主程序启动-%s-%s"%(os.getpid(),os.getppid()))
#     p2 = Process(target=foo,args=("python",))  #args 是一个元组类型
#     p2.start()
#     while True:
#         print("this is process1")
#         time.sleep(1.5)

# def func():
#     print("子程序启动")
#     time.sleep(5)
#     print("子程序结束")
#
# if __name__ == '__main__':
#     print("父程序启动")
#     p1 = Process(target = func)
#     p1.start()
#     p1.join()
#     print("父程序结束")

"""进程池"""
# from multiprocessing import Pool
# import os,time,random
#
# def func_task(name):
#     print("子进程开始%s"%(name))
#     start = time.time()
#     time.sleep(random.choice([1,2,3]))
#     end = time.time()-start
#     print("子进程结束%s，耗时%d"%(name,end))
#
# if __name__ == '__main__':
#     print("父进程开始...")
#     p = Pool()
#     for i in range(5):
#         p.apply_async(func_task,args=(i,))
#     p.close()
#     p.join()
#     print("父进程结束")

"""多线程"""
"""
在进程内部,需要执行多个子任务，那么把进程内的子任务叫线程
线程的内存空间是共享的，每一个线程都共享同一个进程的资源
模块：
1._thread  底层模块
2.threading  高层模块，对_thread进行了二次封装
"""

"""创建多线程"""
# import threading,time
#
# def func(num):
#     print("子线程%s开始..."%(threading.current_thread().name))
#     time.sleep(2)
#     print(num)
#     time.sleep(2)
#     print("子线程%s结束..."%(threading.current_thread().name))
# if __name__ == '__main__':
#     print("主线程%s启动..."%(threading.current_thread().name))
#     t = threading.Thread(target=func,args=(6,))
#     t.start()
#     t.join()
#     print("主线程%s结束"%(threading.current_thread().name))

"""线程的数据共享"""

# import threading
#
# num = 0
# def run(n):
#     global num
#     for i in range(1000000):
#         num += n
#         num -= n
# if __name__ == '__main__':
#     t1 = threading.Thread(target = run,args = (6,))
#     t2 = threading.Thread(target = run ,args = (8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("num = ",num)


"""互斥锁"""
"""加锁是为了确保代码中只能有一个线程从头到尾的执行"""
# import threading
#
# lock = threading.Lock()
# num = 0
#
# def run(n):
#     global num
#     for i in range(1000000):
#         # lock.acquire()
#
#         # num += n
#         # num -= n
#
#         # lock.release()
#         with lock:
#             num += n
#             num -= n
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target = run,args=(6,))
#     t2 = threading.Thread(target = run,args=(9,))
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     print("num = ",num)


"""信号量"""
"""信号量控制线程同时执行的个数"""
# import threading
# import time
#
# sem = threading.Semaphore(2)
#
# def func():
#     with sem:
#         for i in range(5):
#             print("%s--%d"%(threading.current_thread().name,i))
#             time.sleep(1)
#
# if __name__ == '__main__':
#     for i in range(5):
#         t = threading.Thread(target = func)
#         t.start()

"""barrier()凑够数才结束"""
# import threading
# sem = threading.Semaphore(10)
# bar = threading.Barrier(10)
#
# def func():
#     with sem:
#         print("%s--start..."%(threading.current_thread().name))
#         time.sleep(1)
#         bar.wait()
#         print("%s--end..."%(threading.current_thread().name))
#
# if __name__ == '__main__':
#     for i in range(21):
#         t = threading.Thread(target = func)
#         t.start()
