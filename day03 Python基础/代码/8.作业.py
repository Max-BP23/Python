# 实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使用字符串格式化）。
# 方法一
# print("开始")
# i = 1 #或者i=0 下面i<3, format是4-i
# while i < 4:
#     i += 1
#     user = input("请输入用户名:")
#     pwd = input("请输入密码:")
#     if user == "wupeiqi" and pwd == "luffy":
#         print("成功")
#         break
#     else:
#         message = "用户名或者密码错误,剩余错误次数为{}次".format(4 - i)
#         print(message)
#
# 方法二
# i=3
# while i>0: #这边需要设置大于了
#     i -= 1
#     user = input("请输入用户名:")
#     pwd = input("请输入密码:")
#     if user == "wupeiqi" and pwd == "luffy":
#         print("成功")
#         break
#     else:
#         message = "用户名或者密码错误,剩余错误次数为{}次".format(i)
#     print(message)


# 猜年龄游戏
# 要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。
# i = 0
# while i < 3:
#     i += 1
#     age = int(input("请输入年龄:"))
#     if age == 73:
#         print("恭喜你猜对了")
#         break
#     else:
#         print("猜错了")
# print("程序结束")


# 猜年龄游戏升级版
# 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
i = 0
while i < 3:
    i += 1
    age = input("请输入年龄:")
    if age == 73:
        print("猜对了")
        break
    else:
        print("猜错了")

    if i == 3:
        choice = input("请问会否还想继续玩?请输入Y or N:")
        if choice == "N":
            break
        elif choice == "Y":
            i = 0
            continue
        else:
            print("输入有误")

print("程序结束")


