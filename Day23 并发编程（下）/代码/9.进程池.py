import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


def task(num):
    print("子任务", multiprocessing.current_process().pid)
    print("执行", num)
    time.sleep(2)
    return num


def done(res):
    print(multiprocessing.current_process().pid)
    time.sleep(1)
    print(res.result())
    time.sleep(1)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)
    for i in range(10):
        fur = pool.submit(task, i)
        fur.add_done_callback(done)  # done的调用由主进程处理（与线程池不同）

    print(multiprocessing.current_process().pid)
    pool.shutdown(True)
