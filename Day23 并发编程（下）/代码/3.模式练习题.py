import multiprocessing
import threading
import time

def func():
    print("来了")
    with lock:
        print(666)
        time.sleep(1)

def task():
    # 拷贝的锁也是被申请走的状态
    # 被谁申请走了? 被子进程中的主线程申请走了
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    time.sleep(2)
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []
    lock = threading.RLock()
    lock.acquire()
    # print(lock)
    # lock.acquire() # 申请锁
    # print(lock)
    # lock.release()
    # print(lock)
    # lock.acquire()  # 申请锁
    # print(lock)

    p1 = multiprocessing.Process(target=task)
    p1.start()