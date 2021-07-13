import multiprocessing
import time

"""
def task():
    print(name)
    name.append(123)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver
    name = []

    p1 = multiprocessing.Process(target=task)
    p1.start()

    time.sleep(2)
    print(name)  # []
"""
"""
def task():
    print(name) # [123]


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver
    name = []
    name.append(123)

    p1 = multiprocessing.Process(target=task)
    p1.start()
"""

"""
def task():
    print(name)  # []


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # fork、spawn、forkserver
    name = []
    
    p1 = multiprocessing.Process(target=task)
    p1.start()

    name.append(123)
    
"""

"""
def task():
    print(name)


if __name__ == '__main__':
    multiprocessing.set_start_method("forkserver")  # fork、spawn、forkserver
    name = []

    p1 = multiprocessing.Process(target=task)
    p1.start()
"""


def task(data):
    print(data)
    data.append(999)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # fork、spawn、forkserver
    name = []

    p1 = multiprocessing.Process(target=task, args=(name,))
    p1.start()

    time.sleep(2)
    print(name)