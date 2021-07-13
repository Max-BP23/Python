import multiprocessing

if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    for i in range(count - 1):
        p = multiprocessing.Process(target=xxxx)
        p.start()
