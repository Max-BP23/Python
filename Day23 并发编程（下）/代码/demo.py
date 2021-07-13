import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor


def task(num):
    print("执行", num)
    time.sleep(2)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)
