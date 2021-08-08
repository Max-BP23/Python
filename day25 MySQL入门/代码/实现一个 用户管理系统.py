import pymysql

def register():
    print("用户注册>>")
    user = input("请输入用户名:")
    password = input("请输入密码:")

    # 指定连接数据
    coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',charset='utf8',db='usersdb')
    cursor=coon.cursor()

    # 执行SQL语句
    sql = "insert into users(name,password) values('{}','{}')".format(user,password)

    cursor.execute(sql)
    coon.commit()

    # 关闭数据
    cursor.close()
    coon.close()

    print('注册成功,用户名{},密码{}'.format(user,password))

def login():
    print('用户登录>>')
    user = input("请输入用户名:")
    password = input("请输入密码:")

    # 链接指定数据
    coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',charset='utf8',db='usersdb')
    cursor=coon.cursor()

    # 执行sql语句
    sql = "select * from users where name='{}' and password='{}'".format(user,password)
    cursor.execute(sql)
    coon.commit()

    result = cursor.fetchone()

    cursor.close()
    coon.close()

    if result:
        print("登录成功",result)
    else:
        print("登录失败")

def run():
    choice = input("请输入功能序号(1.注册,2.登录):")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("错误输入")

if __name__ == '__main__':
    run()

