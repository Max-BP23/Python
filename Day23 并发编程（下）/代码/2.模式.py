import multiprocessing
import threading


def task(fb, lk):
    ile_object = open('x1.txt', mode='a+', encoding='utf-8')
    lock = threading.RLock()


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # fork、spawn、forkserver

    name = []
    file_object = open('x1.txt', mode='a+', encoding='utf-8')
    lock = threading.RLock()

    p1 = multiprocessing.Process(target=task, args=(file_object, lock,))
    p1.start()
    p1.join()
