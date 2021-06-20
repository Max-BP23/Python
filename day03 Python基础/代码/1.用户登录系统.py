#请实现一个用户登录系统，如果密码错误则反复提示让用户重新输入，直到输入正确才停止

print("开始运行路飞系统")

flag = True
while flag:
    user = input("请输入用户名:")
    pwd = input("请输入用户密码:")
    if user == "wupeiqi" and pwd == "luffy":
        print("登录成功")
        flag = False #成功后需要结束循环
    else:
        print("用户名或密码错误")

print("系统结束")