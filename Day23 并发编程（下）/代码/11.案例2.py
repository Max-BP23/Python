import os
import time
from concurrent.futures import ProcessPoolExecutor


def task(file_name):
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
    time.sleep(1)
    return {"total": total_count, 'ip': ip_count}


def outer(info, file_name):
    def done(res, *args, **kwargs):
        info[file_name] = res.result()

    return done


def run():
    # 根据目录读取文件并初始化字典
    """
        1.读取目录下所有的文件，每个进程处理一个文件。
    """
    info = {}

    pool = ProcessPoolExecutor(4)

    for file_name in os.listdir("files"):
        fur = pool.submit(task, file_name)
        fur.add_done_callback(outer(info, file_name))  # 回调函数：主进程

    pool.shutdown(True)
    for k, v in info.items():
        print(k, v)


if __name__ == '__main__':
    run()

