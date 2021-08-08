import pymysql


def register():
    print("用户注册")

    user = input("请输入用户名：")  # alex
    password = input("请输入密码：")  # sb

    # 连接指定数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset="utf8", db="usersdb")
    cursor = conn.cursor()

    # 执行SQL语句（有SQL注入风险，稍后讲解）
    # sql = 'insert into users(name,password)values("alex","sb")'
    sql = 'insert into users(name,password) values("{}","{}")'.format(user, password)

    cursor.execute(sql)
    conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    print("注册成功，用户名：{},密码:{}".format(user, password))


def login():
    print("用户登录")

    user = input("请输入用户名：")
    password = input("请输入密码：")

    # 连接指定数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset="utf8", db="usersdb")
    cursor = conn.cursor()

    # 执行SQL语句（有SQL注入风险，稍后讲解）
    # sql = select * from users where name='wupeiqi' and password='123'
    sql = "select * from users where name='{}' and password='{}'".format(user, password)
    cursor.execute(sql)

    result = cursor.fetchone()  # 去向mysql获取结果
    # None
    # (1,wupeiqi,123)

    # 关闭数据库连接
    cursor.close()
    conn.close()

    if result:
        print("登录成功", result)
    else:
        print("登录失败")


def run():
    choice = input("1.注册；2.登录")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("输入错误")


if __name__ == '__main__':
    run()
