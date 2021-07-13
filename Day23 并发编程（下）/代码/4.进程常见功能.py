import os
import time
import threading
import multiprocessing


def func():
    time.sleep(3)


def task(arg):
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    print(os.getpid(), os.getppid())
    print("线程个数", len(threading.enumerate()))
    time.sleep(2)
    print("当前进程的名称：", multiprocessing.current_process().name)


if __name__ == '__main__':
    print(os.getpid())
    multiprocessing.set_start_method("spawn")
    p = multiprocessing.Process(target=task, args=('xxx',))
    p.name = "哈哈哈哈"
    p.start()

    print("继续执行...")
