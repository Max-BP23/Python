import threading
import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=5,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=3,  # 链接池中最多闲置的链接，0和None不限制
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='blog',
    charset='utf8'
)


class Connect(object):
    def __init__(self):
        self.conn = conn = POOL.connection()
        self.cursor = conn.cursor(pymysql.cursors.DictCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def exec(self, sql, *args, **kwargs):
        params = args or kwargs
        # 执行SQL受影响的行数
        row = self.cursor.execute(sql, params)
        self.conn.commit()
        return row

    def fetch_one(self, sql, *args, **kwargs):
        params = args or kwargs

        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        return result

    def fetch_all(self, sql, *args, **kwargs):
        params = args or kwargs
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        return result
