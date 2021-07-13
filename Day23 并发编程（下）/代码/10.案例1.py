import os
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager


def task(file_name, count_dict):
    ip_set = set()
    total_count = 0
    ip_count = 0
    file_path = os.path.join("files", file_name)
    file_object = open(file_path, mode='r', encoding='utf-8')
    for line in file_object:
        if not line.strip():
            continue
        user_ip = line.split(" - -", maxsplit=1)[0].split(",")[0]
        total_count += 1
        if user_ip in ip_set:
            continue
        ip_count += 1
        ip_set.add(user_ip)
    count_dict[file_name] = {"total": total_count, 'ip': ip_count}
    time.sleep(1)


def run():
    # 根据目录读取文件并初始化字典
    """
        1.读取目录下所有的文件，每个进程处理一个文件。
    """

    pool = ProcessPoolExecutor(4)
    with Manager() as manager:
        """
        count_dict={
        	"20210322.log":{"total":10000,'ip':800},
        }
        """
        count_dict = manager.dict()

        for file_name in os.listdir("files"):
            pool.submit(task, file_name, count_dict)

        pool.shutdown(True)
        for k, v in count_dict.items():
            print(k, v)


if __name__ == '__main__':
    run()
